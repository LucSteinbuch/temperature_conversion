import pytest
from conversion import celsius_to_fahrenheit

def test_celsius_to_fahrenheit():
        assert celsius_to_fahrenheit(20) == 68
        # assert isinstance(celsius_to_fahrenheit(-1000), str)

def test_celsius_to_farenheit_invalid():
  with pytest.raises(TypeError):
    celsius_to_fahrenheit("Invalid")
