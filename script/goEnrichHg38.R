library(getopt)
spec <- matrix(c(
  'csvfilePath', 'f', 1, 'character', 'peak注释后输出的csv格式文件',
  'help', 'h', 0, 'logical', '帮助'
), byrow = T, ncol = 5)

args = getopt(spec)
if(!is.null(args$help) || is.null(args$csvfilePath)){
  cat("\n脚本可以对输入的peak注释文件做GO富集分析，并输出对应的csv结果表格到原路径\n\n")
  cat(paste(getopt(spec, usage = T), "\n"))
  q()
}

suppressPackageStartupMessages(
  library(clusterProfiler, quietly = T, include.only=c("enrichGO"))
)
suppressPackageStartupMessages(
  library(org.Hs.eg.db, quietly = T)
)


id <- read.csv(args$csvfilePath, header = T)

# library(xlsx)
# args$csvfilePath <- 'G:\\Bioseq\\Output\\01 RNA火山图或热图\\240405 RNA结果表格 Sig.xlsx'
# id <- read.xlsx(args$csvfilePath, sheetIndex=1, header = T)
# print(id$ENSEMBL, id$ens_gene)
go <- enrichGO(gene=id$ENSEMBL, "org.Hs.eg.db", ont="ALL", keyType="ENSEMBL",
               pAdjustMethod="BH", pvalueCutoff=0.5, qvalueCutoff=0.05,
               readable=TRUE)
go.res <- data.frame(go)
outputPath <- paste(substring(args$csvfilePath, 1, nchar(args$csvfilePath)-3),"GO.csv", sep='')
write.csv(go.res, outputPath)
