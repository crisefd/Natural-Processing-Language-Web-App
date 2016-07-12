# max.R
require(stats)
source("/home/fabianact/pln_project/mf_test/lematizador.r")
# Fetch command line arguments
myArgs <- commandArgs(trailingOnly = TRUE)

# Convert to numerics
usq<-0
for(i in 1:length(myArgs))
{
  usq[i]<-lematizador(myArgs[i])
}

# cat will write the result to the stdout stream
cat(usq)
