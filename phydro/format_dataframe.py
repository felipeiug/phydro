import pandas as pd


def format_chuva_vazao(
    df: pd.DataFrame,
    tipo: str | None = None,
    coluna_data: str = "Data",
) -> pd.DataFrame:
    """Transforma o formato mensal/largo do Hidroweb em formato diario.

    O dataframe de origem deve ter uma linha por mes e colunas como
    ``Chuva01``...``Chuva31`` ou ``Vazao01``...``Vazao31``.
    """
    if coluna_data not in df.columns:
        raise KeyError(f"A coluna de data '{coluna_data}' nao foi encontrada.")

    tipos_disponiveis = {
        nome: [
            coluna
            for coluna in df.columns
            if coluna.casefold().startswith(prefixo.casefold())
            and coluna[len(prefixo):].isdigit()
        ]
        for nome, prefixo in (("chuva", "Chuva"), ("vazao", "Vazao"))
    }
    if tipo is None:
        encontrados = [nome for nome, colunas in tipos_disponiveis.items() if colunas]
        if len(encontrados) != 1:
            raise ValueError(
                "Nao foi possivel determinar o tipo automaticamente; "
                "informe tipo='chuva' ou tipo='vazao'."
            )
        tipo = encontrados[0]
    elif tipo.casefold() in {"vazao", "vazão"}:
        tipo = "vazao"
    elif tipo.casefold() == "chuva":
        tipo = "chuva"
    else:
        raise ValueError("tipo deve ser 'chuva' ou 'vazao'.")

    prefixo = "Chuva" if tipo == "chuva" else "Vazao"
    colunas_diarias = tipos_disponiveis[tipo]
    if not colunas_diarias:
        raise ValueError(f"Nenhuma coluna diaria '{prefixo}01' ... foi encontrada.")
    colunas_status = [
        coluna
        for coluna in df.columns
        if coluna.casefold().endswith("status")
         and coluna.casefold().startswith(tipo)
    ]
    if not colunas_status:
        raise ValueError("Nenhuma coluna diaria 'Tipo01Status' ... foi encontrada.")

    coluna_codigo = "Codigo" if "Codigo" in df.columns else "EstacaoCodigo"
    coluna_metodo = "MetodoObtencaoChuvas" if tipo == "chuva" else "MetodoObtencaoVazoes"
    colunas_identificadoras = [
        coluna_codigo,
        coluna_data,
        "NivelConsistencia",
        coluna_metodo,
    ]
    colunas_faltantes = [coluna for coluna in colunas_identificadoras if coluna not in df.columns]
    if colunas_faltantes:
        raise KeyError(f"Colunas obrigatorias nao encontradas: {', '.join(colunas_faltantes)}.")

    base = df.copy()
    base[coluna_data] = pd.to_datetime(base[coluna_data], dayfirst=True, errors="coerce")
    if base[coluna_data].isna().any():
        raise ValueError(f"A coluna '{coluna_data}' contem datas invalidas.")

    resultado = base.melt(
        id_vars=colunas_identificadoras,
        value_vars=colunas_diarias,
        var_name="_dia",
        value_name=prefixo,
    )
    status = base.melt(
        id_vars=colunas_identificadoras,
        value_vars=colunas_status,
        var_name="_dia_status",
        value_name="Status",
    )
    resultado["_dia"] = resultado["_dia"].str[len(prefixo):].astype(int)
    status["_dia"] = status["_dia_status"].str[len(tipo):len(tipo)+2].astype(int)
    status = status.drop(columns="_dia_status")
    resultado = resultado.merge(
        status,
        on=colunas_identificadoras + ["_dia"],
        how="left",
    )
    resultado[coluna_data] = pd.to_datetime(
        resultado[coluna_data].dt.strftime("%Y-%m-")
        + resultado["_dia"].astype(str),
        format="%Y-%m-%d",
        errors="coerce",
    )
    resultado = resultado.dropna(subset=[coluna_data])
    resultado = resultado.drop(columns="_dia").sort_values(coluna_data).reset_index(drop=True)
    if coluna_codigo == "EstacaoCodigo":
        resultado = resultado.rename(columns={coluna_codigo: "Codigo"})
    resultado = resultado[
        ["Codigo", coluna_data, prefixo, "Status", "NivelConsistencia", coluna_metodo]
    ]
    return resultado