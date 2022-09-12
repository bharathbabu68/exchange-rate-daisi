# Forex App
A very minimalistic application that lets you get the exchange rate between a pair of currencies and also convert a given amount from one currency to another along with a Streamlit UI. The app also enables you to do this with historic rates. 

## Installation
```bash
pip install pydaisi
```

## Calling

Initialize the Daisi:
```python
import pydaisi as pyd
live_forex_rates = pyd.Daisi("bharathbabu3017/Live Forex Rates")
```

Call the `get_live_exchange_rate` endpoint in Python with `pydaisi`:
```python
live_forex_rates.get_live_exchange_rate(curr1, curr2).value
```

Call the `convert_currencies` endpoint in Python with `pydaisi`:
```python
live_forex_rates.convert_currencies(from_curr, to_curr, amount).value
```

## Running
This app can be tested straight through the Daisi platform [Click here](https://app.daisi.io/daisies/bharathbabu3017/Live%20Forex%20Rates/streamlit)