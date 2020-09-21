coin = ('Bitcoin', 'Ether', 'Ripple', 'Litecoin')
code = ('BTC', 'ETH', 'XRP', 'LTC')
# coin_code = coin + code
coin_code = {key: value for key, value in zip(coin, code)}
print(coin_code)
