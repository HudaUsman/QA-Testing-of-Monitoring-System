# test_temperature_monitor.py

from temperature_monitor import check_temperature

def test_normal_temperature():
    assert check_temperature(40) == "NORMAL"

def test_high_temperature_alert():
    assert check_temperature(90) == "ALERT"

def test_threshold_boundary():
    assert check_temperature(80) == "NORMAL"

def test_invalid_temperature():
    assert check_temperature(None) == "ERROR"
