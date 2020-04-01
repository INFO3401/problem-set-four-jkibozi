import matplotlib.pyplot as plt

# Problem Set 4: Problem 5
def normalizeData(dataset):
	newcolumn = []
	for i, row in dataset.iterrows():
		row.drop(labels=['Poll','Date','Sample','Spread'],inplace=True)
		value = 100 - row.sum()
		newcolumn.append(value)
	dataset['Undecided'] = newcolumn

# Problem Set 4: Problem 7
def plotCandidate(candidate,dataset):
	plt.scatter(dataset["Poll"],dataset[candidate])
	plt.title(candidate)
	plt.show()

# Problem Set 4: Problem 8
def statsPerCandidate(candidate,dataset):
	return dataset[candidate].mean()

# Problem Set 5: Problem 10
def cleanSample(dataset):
	sampleType = []
	sampleSize = []
	for i, row in dataset.iterrows():
		if 'RV' in row["Sample"]:
			sampleType.append('RV')
			sampleSize.append(row["Sample"].replace(' RV',''))
		elif 'LV' in row["Sample"]:
			sampleType.append('LV')
			sampleSize.append(row["Sample"].replace(' LV',''))
	for size in range(len(sampleSize)):
		if 'RV' not in sampleSize[size] and 'LV' not in sampleSize[size]:
			sampleSize[size] = int(sampleSize[size])
		else:
			sampleSize[size] = 0
	dataset["Sample Type"] = sampleType
	dataset["Sample Size"] = sampleSize

# Problem Set 5: Problem 12.1
def computePollWeight(dataset,poll):
	return sum(dataset[dataset['Poll'] == poll]["Sample Size"]) / sum(dataset["Sample Size"])

# Problem Set 4: Problem 13
def weightedStatsPerCandidate(candidate,dataset):
	weightedAverages = []
	for poll in dataset["Poll"].unique():
		val = sum(dataset[dataset["Poll"] == poll][candidate]) * computePollWeight(dataset,poll)
		weightedAverages.append(val)
	return sum(weightedAverages) / len(weightedAverages)

# Problem Set 4: Problem 15
def computeCorrelation(candidate1,candidate2,dataset):
	return dataset[candidate1].corr(dataset[candidate2])

# Problem Set 4: Problem 17
def superTuesday(dataset,candidates):
	BidenST = []
	SandersST = []
	
	for i, row in dataset.iterrows():
		BidenCount = row["Biden"]
		SandersCount = row["Sanders"]
		
		for candidate in candidates: 
			if candidate != "Biden" and candidate != "Sanders":
				BidenCorr = computeCorrelation("Biden",candidate,dataset)
				SandersCorr = computeCorrelation("Sanders",candidate,dataset)
				
				if abs(BidenCorr) > abs(SandersCorr):
					BidenCount += row[candidate]
				else:
					SandersCount += row[candidate]
		
		BidenST.append(BidenCount)
		SandersST.append(SandersCount)
	
	dataset["BidenST"] = BidenST
	dataset["SandersST"] = SandersST