from matplotlib import pyplot as plt
import pandas as pd
c = ["#6DADD3", "#fab051", "#ec684f", "#0A4990", "#D0151E", "#c9daf5"]
plt.rcParams['svg.fonttype'] = 'none'


def clean_anno(x:str):
    if x.startswith("Intron"):
        return "Intron"
    if x.startswith("Exon"):
        return "Exon"
    if x.startswith("Distal"):
        return "Intergenic"
    if x.startswith("Down"):
        return "Downstream"
    if x.startswith("Promoter"):
        return "Promoter"
    if x.endswith("UTR"):
        return "UTR"
    else:
        return x


diff = pd.read_csv("../04 ATAC peaks注释/ATAC Degron DEseq2 peakAnno.csv")
diff['A'] = diff['annotation'].apply(clean_anno)
# fig, axes = plt.subplots(1, 2, figsize=(5, 3))
# p = axes[0].pie(diff['A'].value_counts(), autopct='%1.1f%%', colors=c)
# # axes[0].set_title("CTRL")
#
# axes[1].axis("off")
# axes[1].legend(p[0], diff['A'].value_counts().index, loc="center", fontsize=10)
# fig.tight_layout()

plt.pie(diff['A'].value_counts(), labels=diff['A'].value_counts().index,autopct='%1.1f%%', colors=c, pctdistance=1.2, labeldistance=1.3)
plt.savefig("D 240510-3 ATAC diff deseq2 peaksAnno 饼图 (ChIPseeker).pdf", bbox_inches='tight', facecolor='white')
