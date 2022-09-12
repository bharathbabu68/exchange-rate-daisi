from forex_python.converter import CurrencyRates


def get_live_exchange_rate(curr1, curr2):
    '''
    This function returns the live exchange rate between a pair of currencies

    Parameters:
    - curr1 (string) : First currency in the pair for getting exchange rate
    - curr2 (string) : Second currency in the pair for getting exchange rate

    Return:
    - float : Current Exchange rate
    '''
    c = CurrencyRates()
    exchange_rate = c.get_rate(curr1, curr2) 
    return exchange_rate

def convert_currencies(from_curr, to_curr, amount):
    '''
    This function converts a given amount from one currency to another

    Parameters:
    - from_curr (string) : First currency in the pair for conversion
    - to_curr (string) : Second currency in the pair for conversion
    - amount: Amount / value of currency to be converted

    Return:
    - float : Converted Value
    '''
    c = CurrencyRates()
    exchange_rate = get_live_exchange_rate(from_curr, to_curr)
    converted_value = exchange_rate * float(amount)
    return converted_value