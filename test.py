import alpaca_trade_api as tradeapi
import pandas as pd
import statistics
import sys
import time

from datetime import datetime, timedelta
from pytz import timezone


API_KEY = "PKI954T1M3OSCYFMXE2H"
API_SECRET = "daERvOjYPAhbkpcewq/a/bSCZYM5VjUZbe3s4yxk"
APCA_API_BASE_URL = "https://paper-api.alpaca.markets"

api = tradeapi.REST(API_KEY, API_SECRET, APCA_API_BASE_URL, 'v2')


days_to_test = 2020
now = datetime.now(timezone('EST'))
beginning = now - timedelta(days=days_to_test)

calendars = api.get_calendar(
    start=beginning.strftime("%Y-%m-%d"),
    end=now.strftime("%Y-%m-%d")
)

print(now)
print(beginning)