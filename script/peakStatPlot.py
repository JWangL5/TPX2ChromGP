from matplotlib import pyplot as plt
plt.subplots_adjust(top=1,bottom=0,left=0,right=1,hspace=0,wspace=0)
import pandas as pd
import argparse

parser = argparse.ArgumentParser(description='peak anno output file')
parser.add_argument('-file', '-f', type=str, required=True, help="file path to extract")
parser.add_argument('-name', '-n', type=str, required=False, help="title of the plot")
args = parser.parse_args()


def clean_anno(x: str):
    if x.startswith("Intron"):
        return "Intron"
    if x.startswith("Exon"):
        return "Exon"
    if x.startswith("Distal"):
        return "Intergenic"
    if x.startswith("Down"):
        return "Downstream"
    else:
        return x


data = pd.read_csv(args.file)
data['A'] = data['annotation'].apply(clean_anno)

fig, ax = plt.subplots(2, 1, figsize=(3, 5), dpi=120)
p = ax[0].pie(data['A'].value_counts(), autopct='%1.1f%%')
ax[0].set_title(args.name)
ax[1].axis("off")
ax[1].legend(p[0], data['A'].value_counts().index, loc="center", fontsize=10)
fig.savefig(f'{args.file[:-4]}.png', bbox_inches='tight')
