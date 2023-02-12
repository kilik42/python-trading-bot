# CCXT Tutorial: how to get crypto order book


import ccxt
import dontshare_config as config

symbol = 'BTC/USDT'

phemex = ccxt.phemex({
    'enableRateLimit': True,
    'apiKey': config.api_key, #.xP_KEY you might have to use this instead of 'apiKey': config.api_key
    'secret': config.secret, #.xP_SECRET
})

#how to create an order book
def ob(symbol):
    orderbook = phemex.fetch_order_book(symbol)
    print(orderbook)
    bid = orderbook['bids'][0][0] if len(orderbook['bids']) > 0 else None
    ask = orderbook['asks'][0][0] if len(orderbook['asks']) > 0 else None
    print(f'the bid is {bid} and the ask is {ask}')
    spread = (ask - bid) if (bid and ask) else None
    return bid, ask, spread

print(ob())
#how to create a limit order



