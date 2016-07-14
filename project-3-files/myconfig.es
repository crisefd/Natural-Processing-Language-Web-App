##
#### default configuration file for Spanish analyzer
##

#### General options 
Lang=es
Locale=es_ES.utf8

### Tagset description file, used by different modules
TagsetFile=$FREELINGSHARE/es/tagset.dat

## Traces (deactivated)
TraceLevel=0
TraceModule=0x0000

## Options to control the applied modules. The input may be partially
## processed, or not a full analysis may me wanted. The specific 
## formats are a choice of the main program using the library, as well
## as the responsability of calling only the required modules.
InputLevel=text
OutputLevel=morfo

# Do not consider each newline as a sentence end
AlwaysFlush=no

#### Tokenizer options
TokenizerFile=$FREELINGSHARE/es/tokenizer.dat

#### Splitter options
SplitterFile=$FREELINGSHARE/es/splitter.dat

#### Morfo options
AffixAnalysis=yes
CompoundAnalysis=yes
MultiwordsDetection=yes
NumbersDetection=yes
PunctuationDetection=yes
DatesDetection=yes
QuantitiesDetection=yes
DictionarySearch=yes
ProbabilityAssignment=yes
DecimalPoint=,
  ThousandPoint=.
  LocutionsFile=$FREELINGSHARE/es/locucions.dat 
  QuantitiesFile=$FREELINGSHARE/es/quantities.dat
  AffixFile=$FREELINGSHARE/es/afixos.dat
  CompoundFile=$FREELINGSHARE/es/compounds.dat
  ProbabilityFile=$FREELINGSHARE/es/probabilitats.dat
  DictionaryFile=$FREELINGSHARE/es/dicc.src
  PunctuationFile=$FREELINGSHARE/common/punct.dat
  ProbabilityThreshold=0.001

# NER options 
  NERecognition=yes
  NPDataFile=$FREELINGSHARE/es/np.dat
## comment line above and uncomment one of those below, if you want 
## a better NE recognizer (higer accuracy, lower speed)
#NPDataFile=$FREELINGSHARE/es/nerc/ner/ner-ab-poor1.dat
#NPDataFile=$FREELINGSHARE/es/nerc/ner/ner-ab-rich.dat
# "rich" model is trained with rich gazetteer. Offers higher accuracy but 
# requires adapting gazetteer files to have high coverage on target corpus.
# "poor1" model is trained with poor gazetteer. Accuracy is splightly lower
# but suffers small accuracy loss the gazetteer has low coverage in target corpus.
# If in doubt, use "poor1" model.

## Phonetic encoding of words.
  Phonetics=no
  PhoneticsFile=$FREELINGSHARE/es/phonetics.dat

## NEC options. See README in common/nec
  NEClassification=no
  NECFile=$FREELINGSHARE/es/nerc/nec/nec-ab-poor1.dat
#NECFile=$FREELINGSHARE/es/nerc/nec/nec-ab-rich.dat

## Sense annotation options (none,all,mfs,ukb)
  SenseAnnotation=none
  SenseConfigFile=$FREELINGSHARE/es/senses.dat
  UKBConfigFile=$FREELINGSHARE/es/ukb.dat

#### Tagger options
  Tagger=hmm
  TaggerHMMFile=$FREELINGSHARE/es/tagger.dat
  TaggerRelaxFile=$FREELINGSHARE/es/constr_gram-B.dat
  TaggerRelaxMaxIter=500
  TaggerRelaxScaleFactor=670.0
  TaggerRelaxEpsilon=0.001
  TaggerRetokenize=yes
  TaggerForceSelect=tagger

#### Parser options
  GrammarFile=$FREELINGSHARE/es/chunker/grammar-chunk.dat

#### Dependence Parser options
  DependencyParser=txala
  DepTxalaFile=$FREELINGSHARE/es/dep_txala/dependences.dat
  DepTreelerFile=$FREELINGSHARE/es/dep_treeler/dependences.dat

#### Coreference Solver options
  CorefFile=$FREELINGSHARE/es/coref/relaxcor/relaxcor.dat
  SemGraphExtractorFile=$FREELINGSHARE/es/semgraph/semgraph-SRL.dat
