from utils import *
from poll import Poll
from pollingData import *

df = loadAndCleanData("2020_democratic_presidential_nomination-6730.csv")

pollNames = pd.unique(df["Poll"])

polls = []
for name in pollNames:
	poll = Poll(name, df)
	polls.append(poll)
	pollCount = poll.countPoll()

	if (pollCount > 1):
		print("Biden:",poll.avgInPoll("Biden"),"+/-",poll.pollConfidence("Biden"))
		print("Sanders:",poll.avgInPoll("Sanders"),"+/-",poll.pollConfidence("Sanders"))


		print("Biden:",poll.avgInPoll("Biden"),"+/-",poll.pollUncertainty("Biden"))
		print("Sanders:",poll.avgInPoll("Sanders"),"+/-",poll.pollUncertainty("Sanders"))
		print("Biden:",poll.avgInPoll("Biden"),"+/-",poll.pollStdDev("Biden"))
		print("Sanders:",poll.avgInPoll("Sanders"),"+/-",poll.pollStdDev("Sanders"))
		print("Biden:",poll.avgInPoll("Biden"),"+/-",poll.pollErrorMargin("Biden"))
		print("Sanders:",poll.avgInPoll("Sanders"),"+/-",poll.pollErrorMargin("Sanders"))


	print(poll.outlet)
	print(poll.getMostRecentPoll())
	print(poll.countPoll)
	print(poll.changeInPoll("Sanders"))
	print(poll.avgInPoll("Sanders"))


# Problem Set 4: Problem 6
normalizeData(df)
print(df)

# Problem Set 4: Problem 7
for candidate in df.columns:
	if candidate not in ['Poll','Date','Sample','Spread','Undecided']:
		plotCandidate(candidate,df)
# Based on raw polling data, I think Sanders will win because his average distribution is closer to the top and his lowest is around 15 whereas most of the other candidates go as low as 8 to 0.

# Problem Set 4: Problem 9
myCans = []

for candidate in df.columns:
	if candidate not in ['Poll','Date','Sample','Spread','Undecided']:
		myCans.append(candidate)
		print(candidate,statsPerCandidate(candidate,df))

# Problem Set 4: Problem 11
cleanSample(df)

# Problem Set 4: Problem 12.2
print("Morning ConsultM. Consult:",computePollWeight(df,"Morning ConsultM. Consult"))
print("CNNCNN:",computePollWeight(df,"CNNCNN"))
print("ABC News/Wash PostABC/WP:",computePollWeight(df,"ABC News/Wash PostABC/WP"))

# Problem Set 4: Problem 14
for candidate in myCans:
	print(candidate,":",weightedStatsPerCandidate(candidate,df))
# It's pretty close between Sanders and Biden, but Biden has the edge so he's probably going to win.

# Problem Set 4: Problem 16
repeatList = []

for candidate1 in myCans:
	for candidate2 in myCans:
		if candidate1 != candidate2:
			if [candidate1,candidate2] not in repeatList and [candidate2,candidate1] not in repeatList:
				print(candidate1,"vs",candidate2,":",computeCorrelation(candidate1,candidate2,df))
				repeatList.append([candidate1,candidate2])

print("Biden and Klobuchar are the most correlated.")
print("Sanders and Steyer are the least correlated.")

# Problem Set 4: Problem 18
superTuesday(df,myCans)

print("Biden Mean:",df["BidenST"].mean())
print("Sanders Mean:",df["SandersST"].mean())

print("Biden Weighted Mean:",weightedStatsPerCandidate("BidenST",df))
print("Sanders Weighted Mean:",weightedStatsPerCandidate("SandersST",df))

# Based on the data, I think Biden will win.

# Problem Set 4: Problem 19.2
print("Biden:",getConfidenceIntervals(df["BidenST"]))
print("Sanders:",getConfidenceIntervals(df["SandersST"]))
print("Difference:",abs(getConfidenceIntervals(df["BidenST"])-getConfidenceIntervals(df["SandersST"])))

# Problem Set 4: Problem 20.2
print("1.",runTTest(df["Biden"],df["Sanders"]))
print("2.",runTTest(df["BidenST"],df["SandersST"]))

# Problem Set 4: Problem 22
print("\n")
print("The means are pretty close, with Biden going from",54.74,"to",51.40,"and Sanders going from",35.68,"to",37.00,".")
print("\n")
print("The weighted means are higher, with Biden going from",15.30,"to",20.99,"and Sanders goinf from",9.91,"to",14.23,".")
print("\n")
print("The confidence intervals are lower, with Biden going from",1.84,"to",1.14,"and Sanders going from",1.65,"to",1.25,"and the difference going from",0.20,"to",0.11,".")
print("\n")
print("The p-value in the ttests changed drastically, with both Biden/Sanders and BidenST/SandersST having",4.207,"initaill, but then going to",0.002,"for Biden/Sanders and",1.114,"for BidenST/SandersST.")
print("\n")
print("This tells me that the correltion theory was 17 was good because the SuperTuesday function ended up being a good predictor of Biden beating Sanders.")