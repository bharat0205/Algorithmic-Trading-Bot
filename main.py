# documentation: https://www.mql5.com/en/docs/integration/python_metatrader5

import MetaTrader5 as mt  # pip install MetaTrader5
import pandas as pd  # pip install pandas
import plotly.express as px  # pip install plotly
from datetime import datetime

# start the platform with initialize()
mt.initialize()

# login to Trade Account with login()
# make sure that trade server is enabled in MT5 client terminal

login = 89805403
password = 'L_4dLbLe'
server = 'MetaQuotes-Demo'

mt.login(login, password, server)

# get account info
account_info = mt.account_info()
print(account_info)

# getting specific account data
login_number = account_info.login
balance = account_info.balance
equity = account_info.equity

print()
print('login: ', login_number)
print('balance: ', balance)
print('equity: ', equity)

# get number of symbols with symbols_total()
num_symbols = mt.symbols_total()

print(num_symbols)

# get all symbols and their specifications
symbols = mt.symbols_get()
print(symbols)

# get symbol specifications
symbol_info = mt.symbol_info("EURUSD")._asdict()
print(symbol_info)
# ohlc_data
ohlc_data = pd.DataFrame(mt.copy_rates_range("EURUSD", 
                                             mt.TIMEFRAME_H4, 
                                             datetime(2024, 1, 1), 
                                             datetime.now()))

fig = px.line(ohlc_data, x=ohlc_data['time'], y=ohlc_data['close'])
fig.show()

print(ohlc_data)

