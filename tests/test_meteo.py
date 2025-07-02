import pytest
from meteo import analyse_meteo, save_to_json, fetch_meteo_data
import os
import json

def test_analyse_meteo_retourne_donnees_identiques():
    data = {
        "dates": ["2025-07-02", "2025-07-03"],
        "temp_max": [30.0, 28.0],
        "temp_min": [20.0, 18.0]
    }
    result = analyse_meteo(data)
    assert result == data

def test_save_to_json_cree_fichier(tmp_path):
    result = {"a": 1, "b": 2}
    file_path = tmp_path / "test.json"
    save_to_json(result, str(file_path))
    assert os.path.exists(file_path)
    with open(file_path, "r") as f:
        contenu = json.load(f)
    assert contenu == result

def test_fetch_meteo_data_lit_fichier(tmp_path):
    contenu = {
        "dates": ["2025-07-02"],
        "temp_max": [25.0],
        "temp_min": [15.0]
    }
    file_path = tmp_path / "meteo.json"
    with open(file_path, "w") as f:
        json.dump(contenu, f)
    # On change temporairement le répertoire courant pour tester la lecture
    old_cwd = os.getcwd()
    os.chdir(tmp_path)
    try:
        data = fetch_meteo_data(0, 0)
        assert data == contenu
    finally:
        os.chdir(old_cwd)
