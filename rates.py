from forex_python.converter import CurrencyRates, CurrencyCodes
import streamlit as st


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

def currency_codes():
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
    codes = currency_codes()
    st.title("Forex App")
    tab1, tab2 = st.tabs(["Live Exchange Rate", "Convert"])
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
            b1 = st.button('Get Exchange Rate')
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
        amount = st.number_input("Enter amount to convert", min_value=1)
        if curr1 == curr2:
            st.text("")
            st.warning('Both currency 1 and currency 2 are same, please change your option', icon="⚠️")
        else:
            b1 = st.button('Convert')
            if b1:
                with st.spinner('Converting...'):
                    res = convert_currencies(curr1, curr2, amount)
                st.text("")
                st.text(str(amount) + " " + curr1 + " is equal to " + str(res) + " " + curr2)


if __name__ == '__main__':
    st_ui()
