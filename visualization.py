import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from random import seed
from random import randint

dataset = pd.read_csv('selecteditemset.csv')

selecetedItemSet = dataset.iloc[:,0].values
selecetedItemSetSupport = dataset.iloc[:,1].values
selecetedItemSetConfidence = dataset.iloc[:,2].values

# #Visualization
# _, ax = plt.subplots()
# ax.bar(selecetedItemSet, selecetedItemSetSupport, color = '#539caf', align = 'center')
# ax.set_ylabel("Support")
# ax.set_xlabel("Selected Itemset")
# ax.set_title("Selected Itemset in dataset with respect to Support ")

#Visualization-2
_, ax = plt.subplots()
ax.bar(selecetedItemSet, selecetedItemSetConfidence, color = '#539caf', align = 'center')
ax.set_ylabel("Confidence")
ax.set_xlabel("Selected Itemset")
ax.set_title("Selected Itemset in dataset with respect to Confidence ")

#output result
plt.show()