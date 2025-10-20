import websockets
import json
from decimal import Decimal

async def get_coins_data(coins_list):
    # Costruisci URL con multipli streams
    streams = [f"{symbol.lower()}@ticker" for symbol in coins_list]
    url = f"wss://stream.binance.com:9443/stream?streams={'/'.join(streams)}"
    
    async with websockets.connect(url) as binance_ws:
        async for message in binance_ws:
            data = json.loads(message)
            coin_data = process_data(data['data'])
            yield coin_data

def process_data(raw_data):
    # Estrazone dati e conversione in Decimal
    ticker = raw_data['s']
    price = Decimal(str(raw_data['c']))
    volume_24h = Decimal(str(raw_data['v']))
    change_24h = Decimal(str(raw_data['P']))

    # Format data
    volume_24h = volume_24h.quantize(Decimal("0.01"))
    change_24h = change_24h.quantize(Decimal("0.1"))
    min_notional = get_min_notional(price)
    step_size = get_step_size(price, min_notional)
    price = format_price(price)
    
    return {
        "type": "coin_data",
        "payload": {
            ticker: {
                "price": str(price),
                "change_24h": str(change_24h),
                "volume_24h": str(volume_24h),
                "min_notional": min_notional,
                "min_size": str(step_size)
            }
        }
    }


def get_min_notional(price):

    if price < 0.00001:
        return 1
    elif price < 0.001 and price > 0.000009:
        return 2
    elif price < 1 and price > 0.0009:
        return 3
    elif price > 0.9 and price < 99.9:
        return 4
    elif price > 99.9:
        return 5
    else:
        return 5

def get_step_size(price, min_notional):

    step_size = min_notional / price

    if step_size % 1 != 0:
        decimals = str(step_size).split(".")[1]

        if len(decimals) > 6:
            return round(step_size, 6)
    
    return step_size

def format_price(price):

    if price >= 1:
        return price.quantize(Decimal("0.01"))
    
    elif price < 1:
        ignore, decimals = str(price).split(".")
        decimals_array = [int(n) for n in decimals]
        count = 0
        decimals_to_show = 4

        for decimal in decimals_array:
            if decimal == 0:
                count += 1
            else:
                decimals_to_show += count
                break
        
        if decimals_to_show < 8:
            quantize_decimals_to_show = "0." + "0" * (decimals_to_show -1) + "1"
            return price.quantize(Decimal(quantize_decimals_to_show))
        
    return price