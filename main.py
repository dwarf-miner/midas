# system library
import datetime
import pickle

# project library
from cstock.yahoo_engine import YahooEngine
from cstock.request import Requester
from cstock.model import Stock

if __name__ == '__main__':

  try:
    input = open('002415.pkl', 'rb')
    stocks = pickle.load(input)
    input.close()
  except Exception, e:
    engine = YahooEngine()
    yahoo_requester = Requester(engine)
    stocks = yahoo_requester.request('002415', ('1900-01-01', '2016-03-29'))
    output = open('002415.pkl', 'wb')
    pickle.dump(stocks, output, pickle.HIGHEST_PROTOCOL)
    output.close()

for stock in stocks:
    print stock

    # def test_parse(self):
    #     data = ("Date,Open,High,Low,Close,Volume,Adj Close\n" 
    #             "2014-08-22,34.20,34.22,33.49,33.70,2222200,33.70\n"
    #             "2014-08-21,33.81,34.29,33.15,34.21,3544800,34.21")

    #     stocks = self.engine.parse(data, 'foo_id')
    #     self.assertEqual(len(stocks), 2)
    #     self.assertEqual(
    #         stocks[0].as_dict(),
    #         {'close': '33.70',
    #          'code': 'foo_id',
    #          'date': '2014-08-22',
    #          'high': '34.22',
    #          'low': '33.49',
    #          'name': None,
    #          'open': '34.20',
    #          'price': None,
    #          'time': None,
    #          'turnover': None,
    #          'yesterday_close': None,
    #          'volume': '2222200'}
    #     )

