from utils import *
from candidate import Candidate
import seaborn as sns
import matplotlib.pyplot as plt

endorsements = loadAndCleanData("endorsements-2020.csv")
#print(endorsements)

# create a set of candidates from the endorsements dataset
candidates = {}

for endorsee in endorsements["endorsee"].unique():
	if type(endorsee) == str:
		candidates[endorsee] = Candidate(endorsee,endorsements)

#print(candidates)

for endorsee in candidates:
	if candidates[endorsee].countEndorsements() > 10:
		print(endorsee,"has",candidates[endorsee].countEndorsements(),"endorsements.")
	
#	print(endorsee,"has",candidates[endorsee].data["points"].mean(),"+/-",computeConfidenceInterval(candidates[endorsee].data["points"]))

ax = sns.violinplot(x="endorsee",y="points",data=endorsements)
plt.show()

biden = candidates["Joe Biden"].getScore()
sanders = candidates["Bernie Sanders"].getScore()
klobuchar = candidates["Amy Klobuchar"].getScore()

# print("Effect size between Biden and Sanders is",getEffectSize(biden,sanders))
# print("Effect size between Biden and Klobuchar is",getEffectSize(biden,klobuchar))

# print("T-Test between Biden and Sanders is",runTTest(biden,sanders))
# print("T-Test between Biden and Klobuchar is",runTTest(biden,klobuchar))

print(runANOVA(endorsements, "points ~ endorsee + state"))