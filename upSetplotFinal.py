import upsetplot as usp
import pandas as pd
from matplotlib import pyplot

dfr = pd.read_excel(
    "/Users/srujananeelavar/Documents/Summer2023/Research/Rgg144RiosSHP/ExcelsForUpset/ConsolidateExcelForUpset.xlsx")
df = dfr.astype(bool)

df_by_member = usp.from_indicators(["R1-1",	"R1-10",	"R1-13",	"R1-14",	"R1-21",	"R1-23",	"R1-3",	"R1-5",	"R1-6",	"R1-8",	"R1-9",	"R2-11",	"R2-12",	"R2-16",	"R2-17",	"R2-18",	"R2-19",
                                   "R2-2",	"R2-20",	"R2-22",	"R2-4",	"R2-7",	"R3-15",	"R3-24",	"R4-25",	"S1-1",	"S2-2",	"S1-3",	"S1-4",	"S2-5",	"S2-6",	"S1-7",	"S1-8",	"S1-9",	"S1-10",	"S2-11"], data=df)


upset = usp.UpSet(df_by_member, show_counts=True, sort_by='cardinality')
upset.plot()
pyplot.suptitle(
    "Occurence of Rgg144-SHP144 Alleles in GoldenSet")
pyplot.show()
