from meteo import fetch_meteo_data, analyse_meteo, save_to_json, plot_temperatures

if __name__ == "__main__":
    # Paris : lat=48.85, lon=2.35
    data = fetch_meteo_data(48.85, 2.35)
    result = analyse_meteo(data)
    save_to_json(result, "meteo.json")
    print("Résultats sauvegardés dans meteo.json")
    plot_temperatures(result["dates"], result["temp_max"], result["temp_min"])
