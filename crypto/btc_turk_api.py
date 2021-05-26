import requests
from .utils import normalize_prices, get_headers


class Client(object):
    def __init__(self):
        super(Client, self).__init__()
        self.api_url = 'https://api.btcturk.com'

    def get_all_prices(self, currency='USDT', pair=False):
        url = self.api_url + f'/api/v2/ticker/currency?symbol={currency}'
        data = requests.get(url).json()['data']
        result = normalize_prices(data)
        if pair:
            return result[pair]
        return result


if __name__ == '__main__':
    client = Client()
    prices = client.get_all_prices()
