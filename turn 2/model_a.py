import pandas as pd
import pytest

# Dummy data for sensor readings (with some missing values for demonstration)
sensor_data = {
    "Timestamp": pd.date_range(start="2023-07-01", periods=100, freq="1H"),
    "Temperature": [25.5, 24.8, None, 27.3, 28.0, 24.9, 26.5, 27.8, 25.4, 24.6] * 10,
    "Energy_Consumption": [120.5, 118.7, 122.3, 125.6, None, 119.8, 123.4, 127.2, 124.5, 121.8] * 10,
    "CO2_Emissions": [0.8, 0.7, 0.9, 1.0, 0.85, 0.78, None, 1.05, 0.88, 0.79] * 10,
}

df = pd.DataFrame(sensor_data)


def test_for_missing_data():
	"""Test if there are any missing data points in the sensor readings."""
	assert not df.isnull().values.any(), "Missing data points found in the sensor readings!"

@pytest.mark.parametrize("temperature_threshold", [25, 28])
def test_temperature_range(temperature_threshold):
	"""Test if the temperature readings are within the specified range."""
	# Filter out rows with missing Temperature values
	valid_data = df.dropna(subset=["Temperature"])
	assert (valid_data["Temperature"] >= temperature_threshold).all(), f"Temperature exceeds {temperature_threshold} degrees Celsius"

@pytest.mark.parametrize("energy_limit", [120])
def test_energy_consumption_limit(energy_limit):
	"""Test if the energy consumption does not exceed the specified limit."""
	valid_data = df.dropna(subset=["Energy_Consumption"])
	assert (valid_data["Energy_Consumption"] <= energy_limit).all(), f"Energy consumption exceeds {energy_limit} Watts"

@pytest.mark.parametrize("co2_emission_threshold", [1.0])
def test_co2_emission_limit(co2_emission_threshold):
	"""Test if the CO2 emissions do not exceed the specified limit."""
	valid_data = df.dropna(subset=["CO2_Emissions"])
	assert (valid_data["CO2_Emissions"] <= co2_emission_threshold).all(), f"CO2 emissions exceed {co2_emission_threshold} kg/h"


if __name__ == "__main__":
	pytest.main()
