import json
import matplotlib.pyplot as plt

# Charge les données météo depuis le fichier meteo.json

def fetch_meteo_data(lat, lon):
    with open("meteo.json", "r") as f:
        data = json.load(f)
    return data

def analyse_meteo(data):
    # Ici, on retourne simplement les données telles quelles
    return data

def save_to_json(result, path):
    with open(path, "w") as f:
        json.dump(result, f, indent=2)

def plot_temperatures(dates, temp_max, temp_min):
    plt.figure(figsize=(10, 5))
    plt.plot(dates, temp_max, label="Température max", color="red", marker="o")
    plt.plot(dates, temp_min, label="Température min", color="blue", marker="o")
    # Ajout de la courbe de moyenne
    temp_moy = [(tmax + tmin) / 2 for tmax, tmin in zip(temp_max, temp_min)]
    plt.plot(dates, temp_moy, label="Température moyenne", color="green", marker="o", linestyle="--")
    plt.xlabel("Date")
    plt.ylabel("Température (°C)")
    plt.title("Températures maximales, minimales et moyennes")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
