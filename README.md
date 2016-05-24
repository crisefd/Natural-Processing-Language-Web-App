# Natural Processing Language Web App

- Django 1.9 (Python 2.7)
- Freeling 4.0
- Stemmer-es
- Lematizador-es in R

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

### Install the required front-end libraries

`$ bower install`

## Running the App in localhost

`$ python manage.py runserver`
