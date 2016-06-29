import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go

py.sign_in('bickez', 'lfzacdduka')

data1 = pd.read_csv('betterment_data.csv')
piv_data = data1.pivot(index='Unnamed: 0', columns='portfolio', values='monthRetPct')
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

fig1 = go.Figure(data=data, layout=linelayout)
py.plot(fig1, filename='betterment-returns')

# Build the barchart
data2 = pd.read_csv('famafrench_output.csv')

colorf = 'rgba(17, 33, 25, 0.22)'
colort = 'rgba(63, 191, 127, 0.82)'
cols = [colorf] * len(data2['P < 0.05'])
l = (data2['P < 0.05'] == True).values.tolist()
for i in range(len(l)):
	if l[i]:
		cols[i] = colort

trace0 = go.Bar(
		x=data2['Bond Percentage'],
		y=data2['Alpha'],
		marker=dict(
			color= cols
			)
	)

data = [trace0]
barlayout = go.Layout(
    title='Betterment Alpha',
    yaxis=dict(
    	title='Alpha'
    	),
    xaxis=dict(
    	title='Bond Percentage in Portfolio'
    	)
)

fig2 = go.Figure(data=data, layout=barlayout)
py.plot(fig2, filename='betterment-alpha')
