from phydro import get_stations_list, get_station_data, format_chuva_vazao


def main() -> None:
    # stations = get_stations_list()
    # stations.to_file("teste.shp")

    station_data = get_station_data(58105000)
    vazoes = format_chuva_vazao(station_data["Vazoes"])
    print(vazoes)

if __name__ == "__main__":
    main()
