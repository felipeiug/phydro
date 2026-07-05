from __future__ import annotations

from io import BytesIO, StringIO
from pathlib import PurePosixPath
from zipfile import ZipFile

import pandas as pd
import requests

from phydro.auth import get_headers


def _extract_tipo_from_filename(filename: str, cod_estacao: int | str) -> str:
    stem = PurePosixPath(filename).stem
    prefix = f"{cod_estacao}_"

    if stem.startswith(prefix):
        return stem[len(prefix):]

    return stem


def _find_header_line(text: str) -> int:
    for index, line in enumerate(text.splitlines()):
        if ";" in line and 'EstacaoCodigo' in line:
            return index

    raise ValueError("Nenhuma linha de cabecalho com ';' e 'EstacaoCodigo' foi encontrada no TXT.")


def _read_txt_to_dataframe(file_bytes: bytes) -> pd.DataFrame:
    text = file_bytes.decode("latin-1")
    header_line = _find_header_line(text)

    return pd.read_csv(
        StringIO(text),
        sep=";",
        skiprows=header_line,
        decimal=",",
        encoding="latin-1",
    )


def get_station_data(
    cod_estacao: int | str,
    timeout: int = 60,
) -> dict[str, pd.DataFrame]:
    url = (
        "https://www.snirh.gov.br/hidroweb/rest/api/documento/download/files"
        f"?codigoestacao={cod_estacao}&tipodocumento=txt&forcenewfiles=S"
    )

    resp = requests.get(
        url,
        headers=get_headers(),
        timeout=timeout,
    )
    resp.raise_for_status()

    dataframes: dict[str, pd.DataFrame] = {}
    with ZipFile(BytesIO(resp.content)) as zip_file:
        for filename in zip_file.namelist():
            if not filename.lower().endswith(".txt"):
                continue

            tipo = _extract_tipo_from_filename(filename, cod_estacao)
            dataframes[tipo] = _read_txt_to_dataframe(zip_file.read(filename))

    return dataframes


def get_telemetrica_data(
    cod_estacao: int | str,
    timeout: int = 60,
) -> dict[str, pd.DataFrame]:
    url = (
        "https://www.snirh.gov.br/hidroweb/rest/api/documento/download/files"
        f"?codigoestacao={cod_estacao}&tipodocumento=txt&forcenewfiles=S"
    )

    resp = requests.get(
        url,
        headers=get_headers(),
        timeout=timeout,
    )
    resp.raise_for_status()

    dataframes: dict[str, pd.DataFrame] = {}
    with ZipFile(BytesIO(resp.content)) as zip_file:
        for filename in zip_file.namelist():
            if not filename.lower().endswith(".txt"):
                continue

            tipo = _extract_tipo_from_filename(filename, cod_estacao)
            dataframes[tipo] = _read_txt_to_dataframe(zip_file.read(filename))

    return dataframes
