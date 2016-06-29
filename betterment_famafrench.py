import pandas as pd
import statsmodels.api as sm
from statsmodels.iolib.summary2 import summary_col

data = pd.read_csv('betterment_data.csv')

ports = ['bmt0', 'bmt10', 'bmt20', 'bmt30', 'bmt40', 'bmt50', 'bmt60', 'bmt70', 'bmt80', 'bmt90', 'bmt100']

output = pd.DataFrame(columns=['Bond Percentage', 'Alpha', 'P < 0.05', 'Mu', 'Sigma', 'Sharpe'])
regresults = []

for p in ports:
	temp = data[data.portfolio==p]
	mu = temp['monthRetPct'].mean()
	sigma = temp['monthRetPct'].std()
	X = temp[['Mkt-RF', 'SMB', 'HML']]
	X = sm.add_constant(X)
	res = sm.OLS(temp['monthRetPct'], X).fit()
	output.loc[len(output)] = [100 - int(p.split('bmt')[-1]), res.params[0], res.pvalues[0] < 0.05, mu, sigma, mu/sigma]
	regresults.append(res)


output.to_csv('famafrench_output.csv')
reg_summary = summary_col(regresults, stars=True)