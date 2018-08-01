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
Import python scripts.


```
>>> import feedvector_train
>>> import cluster_train
```
The first script parses words from RSS of blogs and counts them. List of blogs nested in fl_supertrain.txt file.
The matrix of counted words will nested in blogdata_train.txt file, which will be created in the same folder.

```
>>> feedvector_train.mainfun()
```

The second script launches clusterisation of the data from the blogs

```
>>> blognames,words,data=cluster_train.readfile('blogdata_train.txt')
>>> clust=cluster_train.hcluster(data)
```

And after that it draws dendrogram by creating a jpg file in the same folder.

```
>>> cluster_train.drawdendrogram(clust,blognames,jpeg='dendrogram.jpg')
```

If we'll open dendrogram.jpg file, we'll see all top russian political blogs divided into clusters.

