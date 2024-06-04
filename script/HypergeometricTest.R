library(getopt)
spec <- matrix(c(
  'statfile', 'f', 1, 'character', '输入需要csv表格',
  'help', 'h', 0, 'logical', '帮助'
), byrow = T, ncol = 5)

args = getopt(spec)
if(!is.null(args$help) || is.null(args$bedfilePath)){
  cat("\n脚本可以对输入的bed文件区域上下游1kb做基因组注释，输出对应的csv结果表格\n\n")
  cat(paste(getopt(spec, usage = T), "\n"))
  q()
}
