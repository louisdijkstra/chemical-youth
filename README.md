Chemical Youth Data Sprint
==========================

This repository contains some of the code/scripts and data written and generated during the Chemical Youth Data Sprint. 

## Getting started

The code/scripts in this project are written in Python. We require __Python 3__ to be installed. First, install `virtualenv` (if you haven't already): 

    $ pip install virtualenv 

Create a virtual environment called `chemicalyouth` by typing in the main directory: 

    $ virtualenv -p python3 chemicalyouth
    $ source chemicalyouth/bin/activate

You can now easily install all requirements by typing

    $ pip install -r requirements.txt

Make sure that whenever you start working with the scripts in this repository to source the environment: 

    $ source chemicalyouth/bin/activate

## Directory structure 

The repository consists of the following directories/files: 

* `bin/` - contains the various Python scripts.

* `data/` - contains the raw data files. See the `README.md` for a more elaborate description of each file. 

* `python/` - contains some functions used by several scripts in `bin/`.

* `R/` - some R-scripts. 

* `Snakefile` - the data processing pipeline (contains some of the more frequently used commands)

## Contact

Louis Dijkstra

__E-mail__: louisdijkstra (at) gmail.com

