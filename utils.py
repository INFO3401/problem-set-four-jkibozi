import pandas as pd
import numpy as np
import scipy.stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
import math

# Problem Set 4: Problem 4
def loadAndCleanData(file):
	dataset = pd.read_csv(file,encoding='utf-8')
	dataset.fillna(value=0,inplace=True)
	# this next line was taken from https://stackoverflow.com/questions/22649693/drop-rows-with-all-zeros-in-pandas-data-frame
	dataset = dataset.loc[(dataset!=0).any(axis=1)] # this lets me drop rows where all values are 0
	return dataset

def computeProbability(feature, bin, data):
	count = 0.0
	for i,datapoint in data.iterrows():
		if datapoint[feature] >= bin[0] and datapoint[feature] < bin[1]:
			count += 1
	return count / len(data)

def computeConfidenceInterval(data):
	npArray = 1.0 * np.array(data)
	stdErr = scipy.stats.sem(npArray)
	n = len(data)
	return stdErr * scipy.stats.t.ppf((1+.95)/2.0,n-1)

def getEffectSize(d1,d2):
	m1 = d1.mean()
	m2 = d2.mean()
	s1 = d1.std()
	s2 = d1.std()
	return (m1 - m2) / math.sqrt((math.pow(s1,3) + math.pow(s2, 3)) / 2.0)

# Problem Set 4: Problem 20.1
def runTTest(d1,d2):
	return scipy.stats.ttest_ind(d1,d2)
	
def runANOVA(dataframe,vars):
	model = ols(vars, data=dataframe).fit()
	aov_table = sm.stats.anova_lm(model, typ=2)
	return aov_table

# Problem Set 4: Problem 19.1
def getConfidenceIntervals(datacolumn):
	npArray = 1.0 * np.array(datacolumn)
	stdErr = scipy.stats.sem(npArray)
	n = len(datacolumn)
	return stdErr * scipy.stats.t.ppf((1+.95)/2.0,n-1)