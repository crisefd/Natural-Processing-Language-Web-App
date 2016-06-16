import sys, re, os, shlex, getopt
from per1 import partition, textToTree, clean, getSegments, evaluate, printList, printDisagreements
#from  NLPlib import *
#nlp = NLPlib()
import per1
#from subprocess import Popen, PIPE
#import subprocess

def parseval(files1, files2, argv):
            ########## Execution starts here ##########

            startTag = '('
            endTag = ')'

            doCleanup = False
            showTrees = False
            showSegments = False
            showIndividualEval = False
            showDisagreements = False
            fileNames = []
            data = [] # A List for holdin trees and segments
	    # Check command line arguments
            #print argv
            print argv
            for o in argv[0:]:
                  print o
                  if o == '-c':
                     doCleanup = True
                  elif o == '-s':
                     showSegments = True
                  elif o == '-t':
                     showTrees = True
                  elif o == '-i':
                     showIndividualEval = True
                  elif o == '-d':
                     showDisagreements = True
                  else:
                     fileNames.append(o)


	    # Check if there were enough arguments
            if len(files1) < 1 and len(files2) < 1:
               # Print out some information
               print 'usage: parseval [file 1] [file 2] [options]'
               print 'example: parseval parse.txt gold.txt -c'
               print 'Precision, recall and cross-bracketing are given in tuples (prescision, recall, cross bracketing).'
               print '-c    remove unidentified words and additional labels eg. NP-SBJ --> NP'
               print '-s    display tags and their span'
               print '-t    display trees'
               print '-i    show evaluation results for every single tree'
               print '-d    show errors, prints "?" where constituent spans do not match'
               sys.exit()

            #print 'entro aqui', files1,len(files1)
            # Process the first file

	    try:
                file1 = open(files1, 'r')
                text1 = file1.read()
                file1.close()
            except:
                   print 'Invalid file.'
                   sys.exit()

            trees1 = []
            segments1 = []
            parts1 = partition(text1, startTag, endTag)
            for part in parts1:
                tree = textToTree(part, startTag, endTag)
                if doCleanup:
                   tree = clean(tree)
                trees1.append(tree)
                segments1.append(getSegments(tree, 1))

               # Process the second file
            try:
                file2 = open(files2, 'r')
                text2 = file2.read()
                file2.close()
            except:
                   print 'Invalid file.'
                   sys.exit()

            trees2 = []
            segments2 = []
            parts2 = partition(text2, startTag, endTag)
            for part in parts2:
                tree = textToTree(part, startTag, endTag)
                if doCleanup:
                   tree = clean(tree)
                trees2.append(tree)
                segments2.append(getSegments(tree, 1))
               # print parts1

               # Evaluate and print the output
            print ''
            precision = recall = crossing = 0
            for i in range(len(parts1)):
                if showTrees or showSegments or showIndividualEval or showDisagreements:
                   print '########## ' + str(i) + ' ##########'
                   print ''
                if showTrees:
                   print parts1[i]
                   print ''
                   print parts2[i]
                   print ''
                if showSegments:
                   printList(segments1[i])
                   print ''
                   printList(segments2[i])
                   print ''
                eval = evaluate(segments1[i], segments2[i])
                if showIndividualEval:
                   print eval[:3]
                   print ''
                if showDisagreements:
                   printDisagreements(eval[3])
                   print ''
               # print 'ESTA EL ERROR'
                precision = precision + eval[0]
                recall = recall + eval[1]
                crossing = crossing + eval[2]
#LP es la precision que es el numero de constituyentes correctos in el analizador
#propuesto sobre el numero de constituyentes en el analizador propuesto
#LR es el recall que es el numero correcto de constituyentes en el analizador
#propuesto sobre el numero de constituyentes en el treebank parse
            #print parts1
            precision = precision/len(parts1)
            recall = recall/len(parts2)
            crossing = crossing/len(parts1)
            pre1=precision*100
            re1=recall*100
            fscore=(2*pre1*re1)/(pre1+re1)
            #fscore es la media armonica entre LP y LR

            print '########## TOTAL ##########'
            print ''
            print 'Average precision, recall,  cross brackets and F-score:'
            print (pre1, re1, crossing,fscore)
            return { 'precision': pre1, 'recall': re1, 'cross-brackets': crossing, 'f-score': fscore }

#text2='wsj_0003.mrg'
#text1= 'siembra.txt.parsed'
#l=[]
#sparseval(text1,text2,l)
