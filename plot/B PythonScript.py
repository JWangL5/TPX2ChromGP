import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

plt.rcParams['svg.fonttype'] = 'none'
sns.set_style("ticks")
#colormap = LinearSegmentedColormap.from_list("", ["#B83945", "#FBDFE2"])
# colormap = LinearSegmentedColormap.from_list("", ["#0A4990", "#6DADD3", "#F18742", "#D0151E"])
# colormap = LinearSegmentedColormap.from_list("", ["#FAB051", "#D0151E"])
colormap = LinearSegmentedColormap.from_list("", ["#FFEBEE", "#F44336", "#B71C1C"])



def div(x):
    a,b = x['GeneRatio'].split('/')
    c,d = x['BgRatio'].split('/')
    return int(a)/int(c)


# down = pd.read_csv('../../RNA/240405 RNA结果表格 DOWN.xGO.csv')
# down = down.dropna().sort_values('Topic')
# down['Ratio'] = down.apply(div, axis=1)
# down = down.sort_values(['Topic', 'Ratio'])
#
# fig, ax = plt.subplots(1,1,figsize=(15, 6))
# sc = plt.scatter(down['ID'], down['Ratio'], s=down['Count']*10, c=down['qvalue'], cmap=colormap)
# ax.set_ylim([0,0.07])
# ax.set_xticklabels(down['ID'], rotation=45, ha='right', fontsize=12)
# # ax.set_xlabel("GO Term", fontsize=12)
# ax.set_ylabel("Gene Ratio", fontsize=12)
#
# plt.colorbar()
# handles, labels = sc.legend_elements(prop="sizes", alpha=0.6, num=3)
# labels = [int(int(i.split('{')[-1][:-2])/10) for i in labels]
# legend = plt.legend(handles, labels, loc="upper right", title="Counts", handleheight=4)
# # plt.legend(*sc.legend_elements("sizes", num=3), handleheight=3)
# ax.set_title("GO Enrichment for RNA-seq Down-regulated Genes")
#
# lines = [
#     plt.Line2D([-0.05, 0.085], [-0.22, -0.22], transform=ax.transAxes, color='darkslategrey'),
#     plt.Line2D([0.095, 0.25], [-0.22, -0.22], transform=ax.transAxes, color='darkslategrey'),
#     plt.Line2D([0.26, 0.485], [-0.22, -0.22], transform=ax.transAxes, color='darkslategrey'),
#     plt.Line2D([0.495, 0.69], [-0.22, -0.22], transform=ax.transAxes, color='darkslategrey'),
#     plt.Line2D([0.70, 0.89], [-0.22, -0.22], transform=ax.transAxes, color='darkslategrey'),
# ]
#
# ax.text(0.01, -0.26, "Cell Cycle", ha='center', transform=ax.transAxes, fontsize=12)
# ax.text(0.17, -0.26, "Microtubule", ha='center', transform=ax.transAxes, fontsize=12)
# ax.text(0.39, -0.26, "Mitosis", ha='center', transform=ax.transAxes, fontsize=12)
# ax.text(0.60, -0.26, "RNA splicing", ha='center', transform=ax.transAxes, fontsize=12)
# ax.text(0.80, -0.26, "Chromatin organization", ha='center', transform=ax.transAxes, fontsize=12)
#
# for line in lines:
#     line.set_clip_on(False)
#     ax.add_line(line)
#
# fig.savefig('B 240510 RNA DOWN GO 气泡图.pdf', bbox_inches='tight', facecolor='white')


# -------------------------------------------------------------------

# up = pd.read_csv('../../RNA/240405 RNA结果表格 UP.xGO.csv')
# up = up.dropna().sort_values('Topic')
#
# up['Ratio'] = up.apply(div, axis=1)
# up = up.sort_values(['Topic', 'Ratio'])
#
# fig, ax = plt.subplots(1,1,figsize=(15,6))
# sc = plt.scatter(up['ID'], up['Ratio'], s=up['Count']*10, c=up['qvalue'], cmap=colormap)
# # ax.set_ylim([0,5])
# ax.set_xticklabels(up['ID'], rotation=45, fontsize=12, ha='right')
# ax.set_ylabel("Gene Ratio", fontsize=12)
# plt.colorbar()
# handles, labels = sc.legend_elements(prop="sizes", alpha=0.6, num=2)
# labels = [int(int(i.split('{')[-1][:-2])/10) for i in labels]
# # handles = [item for index, item in enumerate(lst) if index % 2 != 0]
# # [item for index, item in enumerate(lst) if index % 2 != 0]
# legend = plt.legend(handles, labels, loc="upper right", title="Counts", handleheight=4)
# # plt.legend(*sc.legend_elements("sizes", num=3), handleheight=3)
# ax.set_title("GO Enrichment for RNA-seq Up-regulated Genes")
#
# lines = [
#     plt.Line2D([-0.05, 0.08], [-0.22, -0.22], transform=ax.transAxes, color='darkslategrey'),
#     plt.Line2D([0.09, 0.285], [-0.22, -0.22], transform=ax.transAxes, color='darkslategrey'),
#     plt.Line2D([0.295, 0.55], [-0.22, -0.22], transform=ax.transAxes, color='darkslategrey'),
#     plt.Line2D([0.56, 0.725], [-0.22, -0.22], transform=ax.transAxes, color='darkslategrey'),
#     plt.Line2D([0.735, 0.89], [-0.22, -0.22], transform=ax.transAxes, color='darkslategrey'),
# ]
#
# ax.text(0.015, -0.26, "Cell cycle", ha='center', transform=ax.transAxes, fontsize=12)
# ax.text(0.19, -0.26, "Chromatin", ha='center', transform=ax.transAxes, fontsize=12)
# ax.text(0.42, -0.26, "Cytoskeleton", ha='center', transform=ax.transAxes, fontsize=12)
# ax.text(0.64, -0.26, "G1/S transition", ha='center', transform=ax.transAxes, fontsize=12)
# ax.text(0.81, -0.26, "Spindle", ha='center', transform=ax.transAxes, fontsize=12)
#
# for line in lines:
#     line.set_clip_on(False)
#     ax.add_line(line)
#
# fig.savefig('B 240510 RNA UP GO 气泡图.pdf', bbox_inches='tight', facecolor='white')

# -------------------------------------------------------------------

sig = pd.read_csv('../../RNA/240405 RNA结果表格 Sig.xGO.csv')
sig = sig.dropna().sort_values('Topic')

sig['Ratio'] = sig.apply(div, axis=1)
sig = sig.sort_values(['Topic', 'Ratio'])

fig, ax = plt.subplots(1,1,figsize=(17,6))
sc = plt.scatter(sig['ID'], sig['Ratio'], s=sig['Count']*10, c=-np.log10(sig['qvalue']), cmap=colormap)
# ax.set_ylim([0,0.045])
ax.set_xticklabels(sig['ID'], rotation=45, fontsize=12, ha='right')
ax.set_ylabel("Gene Ratio", fontsize=12)
plt.colorbar()
handles, labels = sc.legend_elements(prop="sizes", alpha=0.6, num=2)
labels = [int(int(i.split('{')[-1][:-2])/10) for i in labels]
# handles = [item for index, item in enumerate(lst) if index % 2 != 0]
# [item for index, item in enumerate(lst) if index % 2 != 0]
legend = plt.legend(handles, labels, loc="upper left", title="Counts", handleheight=4)
# plt.legend(*sc.legend_elements("sizes", num=3), handleheight=3)
ax.set_title("GO Enrichment for Differential Expressed Genes in RNA-seq")

lines = [
    plt.Line2D([-0.05, 0.215], [-0.22, -0.22], transform=ax.transAxes, color='darkslategrey'),
    plt.Line2D([0.225, 0.42], [-0.22, -0.22], transform=ax.transAxes, color='darkslategrey'),
    plt.Line2D([0.43, 0.625], [-0.22, -0.22], transform=ax.transAxes, color='darkslategrey'),
    plt.Line2D([0.635, 0.89], [-0.22, -0.22], transform=ax.transAxes, color='darkslategrey'),
]

ax.text(0.08, -0.26, "Cell cycle", ha='center', transform=ax.transAxes, fontsize=12)
ax.text(0.32, -0.26, "Chromatin", ha='center', transform=ax.transAxes, fontsize=12)
ax.text(0.53, -0.26, "G1/S transition", ha='center', transform=ax.transAxes, fontsize=12)
ax.text(0.76, -0.26, "Microtubule", ha='center', transform=ax.transAxes, fontsize=12)

for line in lines:
    line.set_clip_on(False)
    ax.add_line(line)

fig.savefig('B 240419-1 RNA Sig GO 气泡图.pdf', bbox_inches='tight', facecolor='white')
# print(sig['ID'])