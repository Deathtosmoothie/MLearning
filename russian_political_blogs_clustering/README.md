# Russian political blogs clustering
The goal of this project is to make clusterisation of top Russian political blogs on livejournal.com.
The data for clusterisation process is the number of occurrences of certain words in each entry in the blog.
All code was written on Python3 with libraries for parsing and working with images (installation described below).
### Getting started
First, we need to install required libraries.

*Beautiful Soup*
```
$ apt-get install python3-bs4
```
*PIL*

```
$ pip install Pillow
```
*Transliterate*

```
$ pip install transliterate
```
### Clusterisation
Launch Python console
```
$ python
```
Run the script which parses words from RSS of blogs and counts them. List of blogs nested in fl_supertrain.txt file.

```
>>> import feedvector_train
>>> feedvector_train.mainfun()
```
