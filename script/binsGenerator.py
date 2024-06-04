import requests
import argparse

parser = argparse.ArgumentParser(description='Generate a bed file, dividing human chromosomes (hg38) into uniform blocks')
parser.add_argument('-binSize', '-b', type=int, required=False, default=10000, help='bin size, the default is 10000')
args = parser.parse_args()

hg38 = requests.get('https://hgdownload.soe.ucsc.edu/goldenPath/hg38/bigZips/hg38.chrom.sizes').text
chromSizes = {i.split('\t')[0]: int(i.split('\t')[1]) for i in hg38.split('\n')[:-1]}

with open(f'bin{args.binSize}.bed', 'w') as f:
    for k, v in chromSizes.items():
        for j in range(0, v, args.binSize):
            f.writelines(f"{k}\t{j}\t{j+args.binSize}\n")
print(f'bin{args.binSize}.bed has been generated!')
