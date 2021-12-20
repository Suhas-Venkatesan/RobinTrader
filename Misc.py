import robin_stocks as r
# Additional Functions

def get_total_gains_minus_dividends():
    """ Returns the amount of money you've gained/lost through trading since the creation of your account, minus dividends
    """
    profileData = r.load_portfolio_profile()
    print(profileData)
    allTransactions = r.get_bank_transfers()
    deposits = sum(float(x['amount']) for x in allTransactions if (x['direction'] == 'deposit')) # and (x['state'] == 'completed'))
    withdrawals = sum(float(x['amount']) for x in allTransactions if (x['direction'] == 'withdraw') and (x['state'] == 'completed'))
    money_invested = deposits - withdrawals
    print(deposits)
    dividends = r.get_total_dividends()
    percentDividend = dividends/money_invested*100
    totalGainMinusDividends = float(profileData['extended_hours_equity']) - dividends - money_invested
    return totalGainMinusDividends
