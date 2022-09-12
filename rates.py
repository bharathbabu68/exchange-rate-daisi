from forex_python.converter import CurrencyRates
from datetime import datetime
import streamlit as st


def get_live_exchange_rate(curr1, curr2, date=datetime.now()):
    '''
    This function returns the live exchange rate between a pair of currencies

    Parameters:
    - curr1 (string) : First currency in the pair for getting exchange rate
    - curr2 (string) : Second currency in the pair for getting exchange rate

    Return:
    - float : Current Exchange rate
    '''
    c = CurrencyRates()
    exchange_rate = c.get_rate(curr1, curr2, date) 
    return exchange_rate

def convert_currencies(from_curr, to_curr, amount, date=datetime.now()):
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
    exchange_rate = get_live_exchange_rate(from_curr, to_curr, date)
    converted_value = exchange_rate * float(amount)
    return converted_value

def _currency_codes():
    '''
    This function just returns a list of available currency rates supported by the forex-python package

    Return:
    - array : An array of supported currency codes
    '''
    codes = ["USD"]
    c = CurrencyRates()
    rates = c.get_rates('USD')
    for code in rates:
        codes.append(code)
    return codes

def st_ui():
    '''
    This function creates a Streamlit UI and enables users to choose from a dropdown about the currencies they wish to get the exchange rate on.
    '''
    codes = _currency_codes()
    st.title("Forex App")
    tab1, tab2, tab3 = st.tabs(["Live Exchange Rate", "Convert Live", "Historic Rates"])
    with tab1:
        st.subheader("Live Exchange Rates")
        curr1 = st.selectbox(
        'Select currency 1',
        codes, index=0, key="1")
        curr2 = st.selectbox(
        'Select currency 2',
        codes, index=22, key="2")
        if curr1 == curr2:
            st.text("")
            st.warning('Both currency 1 and currency 2 are same, please change your option', icon="⚠️")
        else:
            b1 = st.button('Get Exchange Rate', key="button1")
            if b1:
                with st.spinner('Loading the exchange rate !'):
                    res = get_live_exchange_rate(curr1, curr2)
                st.text("")
                st.text("Exchange rate between " + curr1 + " and " + curr2 + " is " + str(res))
    with tab2:
        st.subheader("Convert Currencies")
        curr1 = st.selectbox(
        'Select currency 1',
        codes, index=0, key="3")
        curr2 = st.selectbox(
        'Select currency 2',
        codes, index=22, key="4")
        amount = st.number_input("Enter amount to convert", min_value=1, key="7")
        if curr1 == curr2:
            st.text("")
            st.warning('Both currency 1 and currency 2 are same, please change your option', icon="⚠️")
        else:
            b1 = st.button('Convert', key="button2")
            if b1:
                with st.spinner('Converting...'):
                    res = convert_currencies(curr1, curr2, amount)
                st.text("")
                st.text(str(amount) + " " + curr1 + " is equal to " + str(res) + " " + curr2)
    with tab3:
        st.subheader("Get Historic Rates")
        curr1 = st.selectbox(
        'Select currency 1',
        codes, index=0, key="5")
        curr2 = st.selectbox(
        'Select currency 2',
        codes, index=22, key="6")
        amount = st.number_input("Enter amount to convert", min_value=1, key="8")
        dateval = st.date_input("Enter date", value=None, min_value=None, max_value=datetime.now(), key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False)
        if curr1 == curr2:
            st.text("")
            st.warning('Both currency 1 and currency 2 are same, please change your option', icon="⚠️")
        else:
            b1 = st.button('Convert', key="button3")
            if b1:
                with st.spinner('Converting...'):
                    res = convert_currencies(curr1, curr2, amount, dateval)
                st.text("")
                st.text(str(amount) + " " + curr1 + " is equal to " + str(res) + " " + curr2)


if __name__ == '__main__':
    st_ui()
