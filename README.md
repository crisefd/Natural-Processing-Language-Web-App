# Natural Language Processing Web App

- Django 1.9 (Python 2.7)
- Freeling 4.0
- Stemmer-es
- Lematizador-es in R
- Stanford Parser
- Stanford Postagger
- Dan Bikel's Parser

## Installing the required libraries

### To install Freeling with Python, please refer [here ](https://medium.com/@cristhian.fuertes/installation-of-freeling-with-python-7407797f5afd#.4y07ar3q9)

### Installation of PHP for the [Stemmer-es](http://stemmer-es.sourceforge.net/)
- We recommend to install aptitude

`$ sudo apt-get install -y aptitude`

- Install PHP5 and Python RPY2

`$ sudo aptitude install -y php5-cli python-rpy2`

- Update the repositories

`$ sudo aptitude update`

### Installation of R for the [Lematizador-es](http://uce.uniovi.es/mundor/indexse2.html)

- Install R and dependencies with:

`$ sudo aptitude install -y r-base r-base-dev r-recommended libxml2-dev r-cran-xml`

- Install fastmatch package in R

`$ R`

`install.packages("fastmatch",,"http://rforge.net/",type="source")`

`$ q()`

### Installation of NPM and Bower package managers

- Install the NodeJS framework

`$ curl -sL https://deb.nodesource.com/setup_4.x | sudo -E bash -`

`$ sudo aptitude install -y nodejs`

- Install bower

`$ npm install -g bower`

### Installation of Django and Virtualenv

`$ pip install virtualenv`

`$ virtualenv env`

`$ source env/bin/activate`

`$ pip install -r npl_project/requirements.txt`
### Installation of the required front-end libraries

`$ bower install`

### Installation of NLTK

`$ sudo pip install -U nltk`

`$ python -c "import nltk; nltk.download('all')"`

### Installation of Java 8

`$ sudo add-apt-repository ppa:webupd8team/java`

`$ sudo aptitude update`

`$ sudo aptitude install -y oracle-java8-installer`

### Installation of Stanford and Dan Bikel libraries

Create the directories `static/stanford-parser`, `static/stanford-postagger` and `static/dbparser`

And place the contents of the libraries in the corresponding directories

Download from:
- [Dan Bikel's Parser Engine](http://www.bibsonomy.org/url/9fdf389e4993e908ea01dca8996cc65e)
- [Stanford Parser](http://nlp.stanford.edu/software/lex-parser.shtml)
- [Stanford Postagger](http://nlp.stanford.edu/software/tagger.shtml)

## Running the App in localhost

`$ python manage.py runserver`

## For morphological analysis in spanish
Go to URL `/morpho_app/`

## For syntactic analysis in english
Go to URL `/syntactic_app/`
