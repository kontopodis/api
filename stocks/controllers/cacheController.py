from datetime import datetime
from stocks.controllers.tickerController import TickerController
from stocks.models import Stock
import pandas as pd
class CacheController:
    def __init__(self):
        self.controller = []
        self.last_update = datetime.today()
    def add_equity(self,equity):
        self.controller.append(equity)

    def clear_all(self):
        self.controller.clear()

    def check_last_update(self):

        if self.last_update.date() == datetime.today().date():

            print("Cache didn't update")
        else:

            self.update()
            print("Cache updated")

    def update(self):
        ## I have to put here the updates
        equities = Stock.objects.all()
        for e in equities:

            ticker = TickerController(e.ticker)
            tick = pd.DataFrame(ticker.get_5year_data())
            self.add_equity({
                "id":e.id,
                "data":tick.to_json(),
                "name":e.name,
                "ticker":e.ticker,

            })


