#!/usr/bin/env python
#
#  Copyright (c) 2007-2008, Corey Goldberg (<a href="mailto:corey@goldb.org">corey@goldb.org</a>)
#
#  license: GNU LGPL
#
#  This library is free software; you can redistribute it and/or
#  modify it under the terms of the GNU Lesser General Public
#  License as published by the Free Software Foundation; either
#  version 2.1 of the License, or (at your option) any later version.
import urllib
"""
This is the "ystockquote" module.
This module provides a Python API for retrieving stock data from Yahoo Finance.
sample usage:
>>> import ystockquote
>>> print ystockquote.get_price('GOOG')
529.46
"""
def __request(symbol, stat):
    url = 'http://finance.yahoo.com/d/quotes.csv?s=%s&f=%s' % (symbol, stat)
    return urllib.urlopen(url).read().strip().strip('"')
def get_all(symbol):
    """
    Get all available quote data for the given ticker symbol.
    Returns a dictionary.
    """
    values = __request(symbol, 'l1c1va2xj1b4j4dyekjm3m4rr5p5p6s7oahagat1k1').split(',')
    data = {}
    data['price'] = values[0]
    data['change'] = values[1]
    data['volume'] = values[2]
    data['avg_daily_volume'] = values[3]
    data['stock_exchange'] = values[4]
    data['market_cap'] = values[5]
    data['book_value'] = values[6]
    data['ebitda'] = values[7]
    data['dividend_per_share'] = values[8]
    data['dividend_yield'] = values[9]
    data['earnings_per_share'] = values[10]
    data['52_week_high'] = values[11]
    data['52_week_low'] = values[12]
    data['50day_moving_avg'] = values[13]
    data['200day_moving_avg'] = values[14]
    data['price_earnings_ratio'] = values[15]
    data['price_earnings_growth_ratio'] = values[16]
    data['price_sales_ratio'] = values[17]
    data['price_book_ratio'] = values[18]
    data['short_ratio'] = values[19]
    data['open'] = values[20]
    data['days_high'] = values[21]
    data['days_low'] = values[22]
    data['last_trade_time'] = values[23]
    data['last_trade_real_time'] = values[24]
    return data
def get_price(symbol):
    return __request(symbol, 'l1')
def get_change(symbol):
    return __request(symbol, 'c1')
def get_volume(symbol):
    return __request(symbol, 'v')
def get_avg_daily_volume(symbol):
    return __request(symbol, 'a2')
def get_stock_exchange(symbol):
    return __request(symbol, 'x')
def get_market_cap(symbol):
    return __request(symbol, 'j1')
def get_book_value(symbol):
    return __request(symbol, 'b4')
def get_ebitda(symbol):
    return __request(symbol, 'j4')
def get_dividend_per_share(symbol):
    return __request(symbol, 'd')
def get_dividend_yield(symbol):
    return __request(symbol, 'y')
def get_earnings_per_share(symbol):
    return __request(symbol, 'e')
def get_52_week_high(symbol):
    return __request(symbol, 'k')
def get_52_week_low(symbol):
    return __request(symbol, 'j')
def get_50day_moving_avg(symbol):
    return __request(symbol, 'm3')
def get_200day_moving_avg(symbol):
    return __request(symbol, 'm4')
def get_price_earnings_ratio(symbol):
    return __request(symbol, 'r')

def get_historical_prices(ticker1, start, end):
    print 'imagine the code here !'
    return
