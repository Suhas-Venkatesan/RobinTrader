import robin_stocks as r
import pyotp
import pandas as pd
import numpy as np
from Misc import *
from Config import *

# Logging into your Robinhood account
login = r.login(rh_username, rh_password)
# Two Factor Authentication Code:
totp = pyotp.TOTP("").now()
print("Current OTP:", totp)

"""
Algorithmic trading will only work with more than $25,000 of total assets in the Robinhood account due
to restrictions on day trading. 
"""

# Returning the tickers of all the watch list stocks as a list

def watch_list_tickers():
    watchlists = r.get_all_watchlists





# Returning the tickers of all the portfolio stocks as a list

watch_list_tickers()