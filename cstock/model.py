#    Copyright (c) 2015 Walt Chen
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0


class ParserException(Exception):
    pass


class Stock(object):
    
    # yesterday_close is yesterday close price
    # close is today close price

    # volume: unit of stock transacted
    # turnover: total transaction money

    def __init__(self, code, date, open, high, low, close, volume):
        self.code = code
        self.date = str(date)
        self.open = open
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume

    def __str__(self):
        return "%s\tvol: %s\topen: %s\tHI: %s\t LO: %s\tclose: %s" %\
            (self.date, self.volume, self.open, self.high, self.low, self.close)

__all__ = ['ParserException', 'Stock']
