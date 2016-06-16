# max.R
require(stats)
path = paste(getwd(), "/apps/freeling_app/helpers/lematizador.r", sep="")
source(path)
# Fetch command line arguments
myArgs <- commandArgs(trailingOnly = TRUE)

# Convert to numerics
usq<-0
for(i in 1:length(myArgs))
{
	  usq[i]<-lematizador(myArgs[i])
}

# cat will write the result to the stdout stream
cat(toString(usq))
