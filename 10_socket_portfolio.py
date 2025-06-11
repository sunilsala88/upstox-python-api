access_token="eyJ0eXAiOiJKV1QiLCJrZXlfaWQiOiJza192MS4wIiwiYWxnIjoiSFMyNTYifQ.eyJzdWIiOiIzVkNEQkYiLCJqdGkiOiI2ODQ3YzBjYjg1YTA2MzRhMWU4YTI5N2EiLCJpc011bHRpQ2xpZW50IjpmYWxzZSwiaXNQbHVzUGxhbiI6dHJ1ZSwiaWF0IjoxNzQ5NTMyODc1LCJpc3MiOiJ1ZGFwaS1nYXRld2F5LXNlcnZpY2UiLCJleHAiOjE3NDk1OTI4MDB9.VOixYrJn7vRl8BRYGrYJfwawFuRxVuztLt6Ngv9vh3M"


import upstox_client

def on_message(message):
    print('working')
    print(message)


def on_open():
    print("connection opened")


def main():
    configuration = upstox_client.Configuration()
    configuration.access_token = access_token

    streamer = upstox_client.PortfolioDataStreamer(upstox_client.ApiClient(configuration),
                                                  order_update=True,
                                                  position_update=True,
                                                  holding_update=True,
                                                  gtt_update=True)

    streamer.on("message", on_message)
    streamer.on("open", on_open)
    streamer.connect()


if __name__ == "__main__":
    main()
