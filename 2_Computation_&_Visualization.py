import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""
load processed data
"""
path = "folder path/processed_data.xlsx"
data = pd.read_excel(path)
# print(data.head())

"""
visualize a bar plot of the entire dataset
"""
P = data.seed_number
Q = data.gram_weight
X = [x for x in P]
random.shuffle(X)
# print(len(X))   # 3707
y = [x for x in Q]


def plot_entire_dataset():
    fig, ax = plt.subplots()
    ax.bar(X, y, color='darkblue', align='center')
    ax.set_ylim([0, 6])
    ax.set_title(' ')
    ax.set_xlabel(' ')
    ax.set_ylabel('Weight (g)')
    ax.set_xticks([])
    plt.show()


# plot_entire_dataset()

"""
remove outliers in list y
"""


def remove_outliers(data):
    median = np.median(data)
    sd = np.std(data)
    # Note that 'n' below stands for 'new_values'.
    global n
    n = [x for x in data if (median-1.5*sd < x < median + 1.5*sd)]
    return n


n = remove_outliers(y)
# print(n)
# print(len(n))   # 3382

"""
calculate the mean weight in list n
"""
mean_weight = round(np.mean(n), 4)
# print(mean_weight)  # 2.4862

"""
color bars grey if len > mean_weight,
light blue if len < mean_weight
"""
ex1 = [i for i in range(len(n))]
random.shuffle(ex1)


def mean_based_plot():
    fig, ax = plt.subplots()
    vert_bars = ax.bar(ex1, n,
                       color='gray',
                       align='center')
    # change colors
    for bar, height in zip(vert_bars, n):
        if height < mean_weight:
            bar.set(edgecolor='lightblue',
                    facecolor='red',
                    linewidth=3)

    ax.set_ylim([0, 6])
    ax.set_title(' ')
    ax.set_xlabel(' ')
    ax.set_ylabel('Weight (g)')
    ax.set_xticks([])
    plt.show()


# mean_based_plot()

"""
After seeing the decision plot, 
it is difficult to know to which side
of the mean_weight the majority of 
weights lie.
So we calculate
"""
more = [i for i in n if i > mean_weight]
less = [i for i in n if i < mean_weight]

# print(len(more))    # 1636
# print(len(less))    # 1746

# less wins, so mean_less is the selected
# decision value

mean_less = round(np.mean(less), 2)
print(mean_less)    # 1.67
