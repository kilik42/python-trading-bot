#top 3 things to know about ccxt
import ccxt
import dontshare_config as config

phemex = ccxt.phemex({
             'embaleRateLimit': True,
            #  'apiKey': "your_api_key",
              'apiKey': config.api_key, #or .xP_KEY
             'secret': "your_secret",
            })

print(phemex.fetch_balance())


def get_bid_ask(symbol):
    orderbook = phemex.fetch_order_book(symbol)
    print(orderbook)
    bid = orderbook['bids'][0][0] if len(orderbook['bids']) > 0 else None
    ask = orderbook['asks'][0][0] if len(orderbook['asks']) > 0 else None
    print(f'the bid is {bid} and the ask is {ask}')
    spread = (ask - bid) if (bid and ask) else None
    return bid, ask, spread

symbol = 'BTC/USDT'
pos_Size = 0.001
bid = get_bid_ask(symbol)[0]
ask = get_bid_ask(symbol)[1]
params = {'timeInForce': 'PostOnly', 'reduceOnly': True, 'triggerPrice': 10000, 'triggerBy': 'MarkPrice'}

phemex.create_limit_buy_order(symbol,pos_Size, bid, params)


get_bid_ask('BTC/USDT')
get_bid_ask('ETH/USDT')
get_bid_ask('XRP/USDT')
get_bid_ask('LTC/USDT')





