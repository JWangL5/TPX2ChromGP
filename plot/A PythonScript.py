import numpy as np
import pandas as pd
import seaborn as sns
from scipy.stats import zscore
from sklearn.cluster import KMeans
from matplotlib import pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
sns.set_style("ticks")
plt.rcParams.update({'font.size': 16})


def get_diff(x):
    if x['pval'] <= 0.05 and x['log2FoldChange'] < np.log(2/3):
        return "DOWN"
    elif x['pval'] <= 0.05 and x['log2FoldChange'] > np.log(3/2):
        return "UP"
    else:
        return "NoSig"


tpm = pd.read_csv('../../RNA/RNA_tpm.csv', index_col=0)
cdna = pd.read_csv("../../RNA/RNA_diff.csv", index_col=2)

cdna = cdna.join(tpm)
cdna['Con'] = cdna.apply(lambda x:(x['Con1']+x['Con2']+x['Con3'])/3, axis=1)
cdna['IAA'] = cdna.apply(lambda x:(x['IAA1']+x['IAA2']+x['IAA3'])/3, axis=1)
cdna = cdna[(cdna['Con']!=0) | (cdna['IAA']!=0)]
cdna['FoldChange'] = cdna['IAA']/cdna['Con']
cdna['log2FoldChange'] = np.log2(cdna['FoldChange'])
cdna['Max']=cdna[['Con1', 'Con2', 'Con3','IAA1', 'IAA2', 'IAA3']].apply(max, axis=1)
cdna = cdna.groupby('ens_gene').apply(lambda x: x[x['Max'] == x['Max'].max()])
cdna['diff'] = cdna.apply(get_diff, axis=1)

fig = plt.figure(figsize=(8/2.54,8/2.54))
ax = fig.add_subplot(111)
# ax.set_size_inches(7/2.54, 7/2.54)

down = cdna.loc[cdna['diff']=='DOWN']
up = cdna.loc[cdna['diff']=='UP']
nosig = cdna.loc[cdna['diff']=='NoSig']
ax.scatter(x=down['log2FoldChange'], y=down['-log10pval'], s=2, color='#88CEE6')
ax.scatter(x=up['log2FoldChange'], y=up['-log10pval'], s=2, color='#E89DA0')
ax.scatter(x=nosig['log2FoldChange'], y=nosig['-log10pval'], s=2, color='#DDDDDF')
ax.set_xlim([-4, 4])
ax.set_ylim([0, 20])
ax.set_xlabel(r"log2FoldChange")
ax.set_ylabel("-log10p-value")
ax.set_box_aspect(1)
ax.set_title(f"RNA CDS \n {len(down['ens_gene'].unique())} genes down, {len(up['ens_gene'].unique())} genes up")

fig.savefig('240405 RNA火山图(p5 FC15 gene number).eps', bbox_inches='tight', facecolor='white')

tpm = tpm.loc[(tpm != 0).all(axis=1)]
logtpm = tpm.apply(np.log2)
ztpm = logtpm.apply(zscore, axis=1)
ztpm = ztpm.join(cdna['diff'])
ztpm = ztpm[ztpm['diff'] != 'NoSig'].sort_values(['diff'])

from matplotlib import cm
import matplotlib.colors as mcolors

fig, ax = plt.subplots(1,1,figsize=(6,6))
colormap = LinearSegmentedColormap.from_list("", ["#E89DA0", "white", "#88CEE6"])
norm = mcolors.Normalize(vmin=-1, vmax=1)
mapper  = cm.ScalarMappable(mcolors.Normalize(vmin=0, vmax=10), colormap)
sns.heatmap(ztpm[tpm.columns], cmap=colormap, norm=norm, yticklabels="")
plt.savefig('240405 RNA热图(update DEGs).svg', bbox_inches='tight', facecolor='white')
