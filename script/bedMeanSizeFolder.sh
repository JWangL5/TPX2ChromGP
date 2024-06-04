help(){
	echo "usage: bedMeanSize.sh -p bedfilePath"
	echo ""
	echo "Transform all bedpath in specific path into bin bedfile"
	echo ""
	echo "options:"
	echo "-p, the path of bedfiles exist"
	exit -1
}

while getopts 'h:p:' OPT; do
	case $OPT in
		p)bedpath="$OPTARG";;
		h)help;;
		?)help;;
	esac
done

for bedfile in $bedpath/*.bed; do
	 awk -F '\t' '{SUM+=$3-$2} END {print SUM, SUM/NR}' $bedfile
done
