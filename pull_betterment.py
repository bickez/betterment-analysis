import re
import urllib2
import json
import pandas as pd
import pandas_datareader.data as web

response = urllib2.urlopen('https://d1svladlv4b69d.cloudfront.net/src/d3/bmt-hist-perf-line-graph/js/hist-perf.js')
text = response.read()

res = re.search('"data":(.+?)"groups": "portfolio"', text, re.DOTALL)
res = res.group().replace('\n', ' ').replace('\r', '').replace(' ', '')
j = json.loads('{'+res+'}')
data = pd.DataFrame({x:j['data'][x] for x in j['data'].keys()})

ports = ['bmt0', 'bmt10', 'bmt20', 'bmt30', 'bmt40', 'bmt50', 'bmt60', 'bmt70', 'bmt80', 'bmt90', 'bmt100']
data = data.set_index(pd.DatetimeIndex(pd.to_datetime(data['date'], format='%Y-%m-%d')))
data = data[data.portfolio.isin(ports)][['monthRetPct', 'portfolio']]

ffdata = web.DataReader('F-F_Research_Data_Factors', 'famafrench', '1927-01-01')[0]
ffdata = ffdata.set_index(pd.DatetimeIndex(ffdata.index.to_datetime()))

df = data.join(ffdata)
df['monthRetPct'] = df['monthRetPct'] * 100
df.to_csv('betterment_data.csv')
