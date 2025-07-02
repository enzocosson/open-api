import pytest
from meteo import analyse_meteo


def test_analyse_meteo_retourne_donnees_identiques():
    data = {
        "dates": ["2025-07-02", "2025-07-03"],
        "temp_max": [30.0, 28.0],
        "temp_min": [20.0, 18.0],
    }
    result = analyse_meteo(data)
    assert result == data
