import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go

py.sign_in('bickez', 'lfzacdduka')
data = pd.read_csv('betterment_data.csv')

piv_data = data.pivot(index='Unnamed: 0', columns='portfolio', values='monthRetPct')
ports = ['bmt0', 'bmt10', 'bmt20', 'bmt30', 'bmt40', 'bmt50', 'bmt60', 'bmt70', 'bmt80', 'bmt90', 'bmt100']
data = []
for p in ports:
	data.append(go.Scatter(x=piv_data.index, y=piv_data[p], name=str(100-int(p.split('bmt')[-1])) + '% Bonds'))

linelayout = go.Layout(
		title='Betterment Portfolio Returns',
		yaxis=dict(
			title='Monthly Percent Return'
			)
	)

fig = go.Figure(data=data, layout=linelayout)
py.plot(fig, filename='betterment-returns')
