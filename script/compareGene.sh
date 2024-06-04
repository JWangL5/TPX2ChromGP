help(){
	echo "Usage:"
	echo "compare.sh -f fpath -e extends"
	echo ""
	echo "Transform specific bed file into bin bed, and compare with HeLa ChIP target genes."
	echo "Output is a csv file with statistics data"
	echo ""
	echo "Description:"
	echo "-f, the path of bed file"
	exit -1
}

while getopts 'f:h' OPT; do
	case $OPT in
		f)fpath="$OPTARG";;
		h)help;;
		?)help;;
	esac
done

filename=$(basename ${fpath} ".bed")
# echo ${filename}.anno.csv
# exit -1

# sample_size
if [[ ! -e ${filename}.anno.csv ]]; then
	Rscript /mnt/h/Bioseq/bash-script/peakAnnoFromHg38.R -f ${fpath}
fi
ss=$(python3 /mnt/h/Bioseq/bash-script/cutColUniq.py -f "${filename}.anno.csv" -c ENSEMBL | wc -l)

# population_size
ps=22803

output="./${filename}_genes_intersect_with_HeLa_ChIP.txt"
echo "#The file list the intersection with HeLa ChIP" >> $output

echo "ChIPTarget,success_sample,success_population,sample_size,population_size" > $output
for filepath in /mnt/h/Bioseq/Genome/HeLa/bed/*.bed; do
	# ChIPTarget
	chipfile=$(basename ${filepath} '.bed')
	echo -n "${chipfile}," >> $output

	# success_sample
	intersection="./${filename}_intersect_${chipfile}"
	if [[ ! -e ${intersection}.bed ]]; then
		cat $fpath | tr -d '\r' | sort-bed - | bedops --element-of 1 - $filepath > "${intersection}.bed"
	fi
	if [[ ! -e ${intersection}.anno.csv ]]; then
		Rscript /mnt/h/Bioseq/bash-script/peakAnnoFromHg38.R -f "${intersection}.bed"
	fi
	ssam=$(python3 /mnt/h/Bioseq/bash-script/cutColUniq.py -f ${intersection}.anno.csv -c ENSEMBL | wc -l)
	echo -n "${ssam}," >> $output

	# success_population
	if [[ ! -e /mnt/h/Bioseq/Genome/HeLa/bed/${chipfile}.anno.csv ]]; then
		Rscript /mnt/h/Bioseq/bash-script/peakAnnoFromHg38.R -f ${filepath}
	fi
	sp=$(python3 /mnt/h/Bioseq/bash-script/cutColUniq.py -f /mnt/h/Bioseq/Genome/HeLa/bed/${chipfile}.anno.csv -c ENSEMBL | wc -l)
	echo -n "${sp}," >> $output
	
	# sample_size
	echo -n "${ss}," >> $output

	# population_size
	echo "${ps}" >> $output
	
	echo "${filepath} successd!"
	echo "--------------------------------------------"

done
