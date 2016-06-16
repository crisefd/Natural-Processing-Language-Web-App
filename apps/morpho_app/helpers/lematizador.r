
##f <- url("http://uce.uniovi.es/mundor/lematizador.rda")
##f <- file(paste(getwd(), "/apps/freeling_app/helpers/lematizador.rda", sep=""))
f <- paste(getwd(), "/apps/freeling_app/helpers/lematizador.rda", sep="")
load(f)  # spdictionary, spcommonwords, spmorphemes
# close(f)

require(fastmatch)
require(XML) # to use Grampal # install.packages("XML") # sudo apt-get install libxml2-dev

lematizador <- function(word, all.words = FALSE, commonwords =  spcommonwords, dictionary = spdictionary, morphemes = spmorphemes, ...) {

  word <- tolower(as.character(word))
  getcanonicalword <- function(words, database, all.words = FALSE ) {
	pos <- fmatch(words, database$word )
        pos <- pos[!is.na(pos)]
        if( all.words ) database$canonical[pos]
          else database$canonical[ pos[1] ]
	}

    ## Is it a spanish common word?
    canonical <-  getcanonicalword(word, commonwords, all.words)
    if( any(!is.na(canonical)) ) return(canonical)

      ## Is this word in the dictionary?
      canonical <-  getcanonicalword(word, dictionary, all.words)
      if( any(!is.na(canonical)) ) return(canonical)

        ## No. So we have to find out 'similar' words from the dictionary
        ## We split the word in root + desinence.
        ## And we paste root with other possibles desinences.

        ## Divide the word into root+desinence
        nch <- nchar(word)
        listroots <- lapply(1:(nch-1), function(i, word, nch) {
			root <- substring(word,1,i)
		        desinence <- substring(word,i+1,nch)
		        c(root, desinence)
		}, word,nch)
	  listroots <- as.data.frame(do.call(rbind, listroots))
	  names(listroots) <- c("root","desinence")

       getderivational <- function(x, mylist) {
	 pos <- fmatch(x, names(mylist))
	 tmp <- mylist[[pos]]
	          if(is.null(tmp) ) {NA}
	          else {tmp}
         }

	   ## Get the derivational morphemes that correspond to each desinence
	   derivational <- lapply(as.character(listroots$desinence), getderivational , spmorphemes)
	      names(derivational) <- listroots$root

	      ## Build the possible words: root + derivational morphemes
	      possiblewords <-  (unlist(lapply(names(derivational), function(x) paste(x, derivational[[x]], sep=""))))
	        possiblewords <- possiblewords[ !duplicated(possiblewords)]

	        ## Get the canonical words!
	        canonical <- getcanonicalword(possiblewords, dictionary, all.words )
		  if( any(!is.na(canonical)) ) return(canonical[!is.na(canonical)])

		  ## No words until here.
		  return(NA)

}


lematizadorGRAMPAL <- function(word) {
	cambiaracentos <- function(jj){ ## FALTA Ü
	jj <- gsub("Ã\\u0081","Á", jj, fixed=TRUE)
        jj <- gsub("Ã\\u0089","É", jj, fixed=TRUE)
        jj <- gsub("Ã\\u008d","Í", jj, fixed=TRUE)
        jj <- gsub("Ã\\u0093","Ó", jj, fixed=TRUE)
	jj <- gsub("Ã\\u009a","Ú", jj, fixed=TRUE)
	jj <- gsub("Ã\\u0091","Ñ", jj, fixed=TRUE)
	jj
}

    lematiza <- function( frase ){
	      ## Borrowed from
	      ## http://www.datanalytics.com/blog/2011/12/13/un-lematizador-para-el-espanol-con-r-¿cutre-¿mejorable/
	      palabra <- gsub( " ", "+", frase )
              base.url <- paste(
			        "http://cartago.lllf.uam.es/grampal/grampal.cgi?m=etiqueta&e=",
			        palabra, sep = "" )
              tmp <- readLines( base.url, encoding = 'utf8' )
              tmp <- iconv( tmp, "utf-8" )
	      tmp <- gsub( "&nbsp;", " ", tmp )
	      tmp <- readHTMLTable( tmp )
	      tmp <- as.character( tmp[[1]]$V3 )
	      tmp <- do.call( rbind, strsplit( tmp, " " ) )[,4]
		      tmp
    }

    canonical <- lematiza(word)
    canonical <- tolower(cambiaracentos(canonical))
      if( canonical == tolower("UNKN")) canonical <- NA
      canonical
}
