help(){
	echo "usage: bed2bin.sh -b bin.bed -p bedfilePath -o overlap"
	echo ""
	echo "Transform all bedpath in specific path into bin bedfile"
	echo ""
	echo "options:"
	echo "-b, a bed file with all bins"
	echo "-p, the path of bedfiles exist"
	echo "-o, overlap to define the bin"
	exit -1
}

while getopts 'h:b:p:o:' OPT; do
	case $OPT in
		b)binfile="$OPTARG";;
		p)bedpath="$OPTARG";;
		o)overlap="$OPTARG";;
		h)help;;
		?)help;;
	esac
done

suffix=$(basename ${binfile} ".bed")
for bedfile in $bedpath/*.bed; do
	# echo "${overlap} ${binfile} ${bedfile}"
	prefix=$(basename ${bedfile} ".bed")
	output="./${prefix}_${suffix}o${overlap}.bed"
	bedops -e ${overlap} ${binfile} ${bedfile} > ${output}
	echo "${output} has been saved!"
done

