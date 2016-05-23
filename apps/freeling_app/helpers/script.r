# max.R
require(stats)
source("/srv/npl_project/apps/freeling_app/helpers/lematizador.r")
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
