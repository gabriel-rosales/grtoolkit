import seaborn as sns, pandas as pd, os
import matplotlib.pyplot as plt

def plot(*data):
    plt.plot(data)
    # pyplot.savefig(<filename>)
    plt.show()


def heatMap(*data):
    """SAMPLE DATA (Pandas dataframe):
    index,year,month,passengers
    0,1949,January,112
    1,1949,February,118
    2,1949,March,132
    3,1949,April,129
    4,1949,May,121
    5,1949,June,135
    6,1949,July,148"""

    sns_plot = sns.heatmap(data, annot=True, fmt="d", linewidths=.5)
    #sns_plot.figure.savefig(cwd + r"\heatmap_annotation.png")
    plt.yticks(rotation=0)
    plt.show()