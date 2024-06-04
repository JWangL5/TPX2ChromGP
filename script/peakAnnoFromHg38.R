library(getopt)
spec <- matrix(c(
  'bedfilePath', 'f', 1, 'character', '输入需要注释的bed格式文件',
  'help', 'h', 0, 'logical', '帮助'
), byrow = T, ncol = 5)

args = getopt(spec)
if(!is.null(args$help) || is.null(args$bedfilePath)){
  cat("\n脚本可以对输入的bed文件区域上下游1kb做基因组注释，输出对应的csv结果表格到原路径\n\n")
  cat(paste(getopt(spec, usage = T), "\n"))
  q()
}

suppressPackageStartupMessages(
  library(ChIPseeker, quietly = T, 
          include.only=c("readPeakFile", "annotatePeak")
          )
)
suppressPackageStartupMessages(
  library(TxDb.Hsapiens.UCSC.hg38.knownGene, quietly = T)
)
# library(GenomeInfoDb, quietly = T, include.only = c("seqlevels"))

bedPeaksFile = args$bedfilePath
txdb <- TxDb.Hsapiens.UCSC.hg38.knownGene
peak <- readPeakFile(bedPeaksFile)
keepChr= !grepl('_', seqlevels(peak))
seqlevels(peak, pruning.mode="coarse") <- seqlevels(peak)[keepChr]
peakAnno <- annotatePeak(peak, tssRegion=c(-1000, 1000), TxDb=txdb, annoDb="org.Hs.eg.db")
peakAnno_df <- as.data.frame(peakAnno)

# plotAnnoPie(peakAnno)
# plotAnnoBar(peakAnno)
# vennpie(peakAnno)
# upsetplot(peakAnno)

outputPath <- paste(substring(bedPeaksFile, 1, nchar(bedPeaksFile)-3),"anno.csv", sep='')
write.csv(peakAnno_df, outputPath, row.names = FALSE)
cat(paste(outputPath, "has been saved.\n"))
