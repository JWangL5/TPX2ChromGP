help(){
	echo "Usage: compare.sh -f bedpath [-b binfile]"
	echo ""
	echo "Transform specific bed file into bin bed, and compare with HeLa ChIP target bins."
	echo "Output is a csv file with statistics data"
	echo ""
	echo "Description:"
	echo "-f, the path of bed file"
	echo "-b, the bin file, optional, default is bin2000"
	exit -1
}

bfile="/mnt/h/Bioseq/bash-script/bin2000.bed"
while getopts 'f:b:h' OPT; do
	case $OPT in
		f)ffile="$OPTARG";;
		b)bfile="$OPTARG";;
		h)help;;
		?)help;;
	esac
done

# bash /mnt/h/Bioseq/bash-script/bed2bin.sh -b $bfile -p $fpath -o 100
prefix=$(basename ${ffile} ".bed")
suffix=$(basename ${bfile} ".bed")
binpath="./${prefix}_${suffix}o100.bed"

if [ ! -e "$binpath" ]; then
    bedops -e 100 $bfile $ffile > ${binpath}
fi

filename=$(basename ${ffile} ".bed")
output="./${filename}_intersect_with_HeLa_ChIP_bin500o100.txt"
# echo "# The file list the intersection with HeLa ChIP" > $output
echo "ChIPTarget,success_sample,success_population,sample_size,population_size" >> $output

ss=$(cat $binpath | wc -l) 
ps=$(cat $bfile | wc -l)

for filepath in /mnt/h/Bioseq/Genome/HeLa/bin500o100/*; do
	echo -n "$(basename ${filepath}), "  >> $output
	echo -n "$(bedops --element-of 1 $binpath $filepath | wc -l), " >> $output
	echo -n "$(cat $filepath| wc -l), " >> $output
	echo -n "${ss}, " >> $output
	echo "${ps}" >> $output
	echo "$(basename ${filepath}) has been output!"
done
