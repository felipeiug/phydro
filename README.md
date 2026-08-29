# phydro

Biblioteca Python para consultar dados do Hidroweb.

## Instalacao

Instale localmente em modo editavel:

```bash
pip install -e .
```

Instale direto do GitHub:

```bash
pip install "git+https://github.com/felipeiug/phydro.git"
```

## Funcoes disponiveis

### `get_stations_list(page_size=1000, show_progress=True, timeout=60)`

Retorna um `geopandas.GeoDataFrame` com a lista de estacoes em `EPSG:4326`.

Exemplo:

```python
from phydro import get_stations_list

stations = get_stations_list()
```

### `get_station_data(cod_estacao, timeout=60)`

Baixa o ZIP da estacao em memoria, extrai os arquivos TXT e retorna um `dict[str, pandas.DataFrame]`.

Cada chave do dicionario e o `tipo` extraido do nome do arquivo no formato `{codigo_estacao}_{tipo}.txt`.

Exemplo:

```python
from phydro import get_station_data

data = get_station_data(48000)

chuvas = data["Chuvas"]
clima = data["Clima"]
```

Para transformar as colunas mensais `Chuva01` ... `Chuva31` ou `Vazao01` ...
`Vazao31` em uma linha por dia:

```python
from phydro import format_chuva_vazao

chuvas_diarias = format_chuva_vazao(chuvas, tipo="chuva")
vazoes_diarias = format_chuva_vazao(data["Vazoes"], tipo="vazao")
```

A coluna `Data` deve identificar o mes de cada linha. Dias que nao existem no
mes sao descartados automaticamente.

## API publica

- `phydro.get_stations_list -> geopandas.GeoDataFrame`
- `phydro.get_station_data -> dict[str, pandas.DataFrame]`

## Contribuindo

Contribuições são bem-vindas. Antes de abrir um PR, consulte o guia em [CONTRIBUTING.md](CONTRIBUTING.md) e siga o padrão de branches, commits e descrição de pull requests.

O template de PR também está disponível em [.github/PULL_REQUEST_TEMPLATE.md](.github/PULL_REQUEST_TEMPLATE.md).
