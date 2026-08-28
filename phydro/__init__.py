"""Python client for selected Hidroweb endpoints."""

from phydro.stations import get_stations_list
from phydro.station_data import get_station_data
from phydro.format_dataframe import format_chuva_vazao

__all__ = [
    "get_stations_list",
    "get_station_data",
    "format_chuva_vazao"
]

__version__ = "0.1.1"
