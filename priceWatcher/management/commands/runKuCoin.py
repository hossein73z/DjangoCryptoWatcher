import asyncio

from django.core.management import BaseCommand

from CryptoWatcher.functions.Coloring import red
from priceWatcher.exchanges.KuCoin import KuCoin


class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            kucoin = KuCoin('wss://ws.postman-echo.com/raw')
            asyncio.run(kucoin.start_listening())
        except Exception as e:
            print(red(str(e)))
            self.handle()
