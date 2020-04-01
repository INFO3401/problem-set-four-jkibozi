from utils import *
from poll import Poll
from pollingData import *

df = loadAndCleanData("2020_democratic_presidential_nomination-6730.csv")
normalizeData(df)

cleanSample(df)
print(df.head())