access_token="eyJ0eXAiOiJKV1QiLCJrZXlfaWQiOiJza192MS4wIiwiYWxnIjoiSFMyNTYifQ.eyJzdWIiOiIzVkNEQkYiLCJqdGkiOiI2ODQ3YzBjYjg1YTA2MzRhMWU4YTI5N2EiLCJpc011bHRpQ2xpZW50IjpmYWxzZSwiaXNQbHVzUGxhbiI6dHJ1ZSwiaWF0IjoxNzQ5NTMyODc1LCJpc3MiOiJ1ZGFwaS1nYXRld2F5LXNlcnZpY2UiLCJleHAiOjE3NDk1OTI4MDB9.VOixYrJn7vRl8BRYGrYJfwawFuRxVuztLt6Ngv9vh3M"


a=["NSE_FO|57912"]

import upstox_client

def on_message(message):
    print('inside message')
    print(message)

def on_error(error):
    print("Error:", error)

def on_close():
    print("WebSocket closed")

def main():
    # Use your existing access_token
    configuration = upstox_client.Configuration()
    configuration.access_token = access_token

    # Replace with your desired instrument key and mode
    instrument_key = a
    mode = 'full_d30'  # full_d30, ltpc, full, etc.

    streamer = upstox_client.MarketDataStreamerV3(
        upstox_client.ApiClient(configuration),
        instrument_key,
        mode=mode
    )

    streamer.on("message", on_message)
    streamer.on("error", on_error)
    streamer.on("close", on_close)

    print("Connecting to Upstox Market Data Stream...")
    streamer.connect()


if __name__ == "__main__":
    main()
