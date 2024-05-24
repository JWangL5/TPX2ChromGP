import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
from matplotlib.colors import LinearSegmentedColormap
plt.rcParams['svg.fonttype'] = 'none'
sns.set_style("ticks")


exp = pd.read_excel('../08 热图/240426 Gene超几何分布检验.xlsx', sheet_name='Sheet1')
ctrl = pd.read_excel('../08 热图/240426 Gene超几何分布检验.xlsx', sheet_name='Sheet2')

exp.index = exp['ChIPTarget'].apply(lambda x: x.split('_')[1])
ctrl.index = ctrl['ChIPTarget'].apply(lambda x: x.split('_')[1])

res = pd.merge(exp, ctrl, left_index=True, right_index=True)

hmap = res[['pval_x', 'pval_y']]
hmap.columns = ['ADRD', 'Random']
hmap = hmap.iloc[:36,:]
hmap = hmap[hmap.index != 'POLR2AphosphoS2']
# print(hmap)

fig, ax = plt.subplots(1, 1, figsize=(18, 2))
ax.xaxis.tick_top()
colormap = LinearSegmentedColormap.from_list("", ["#0A4990", "white", "#D0151E"])
sns.heatmap(-np.log10(hmap).T, cmap=colormap, ax=ax)

ax.set_xticklabels(hmap.index.tolist(), rotation=60, ha='left')

fig.savefig('./E 240520-1 Heatmap.pdf',  bbox_inches='tight')