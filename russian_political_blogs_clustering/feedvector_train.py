import bs4 as bs
import urllib.request 
import re


def mainfun():
    apcount={}
    wordcounts={}
    for url in open('fl_supertrain.txt'):
        blog_title, wc = getwordcounts(url)
        print(url)
        if blog_title == None and wc == None: continue    
        wordcounts[blog_title]=wc
        for word,count in wc.items( ):
            apcount.setdefault(word,0)
            if count>1:
                apcount[word]+=1

    wordlist = []
    for w,bc in apcount.items():
        wordlist.append(w)

    out = open('blogdata_train.txt', 'w')
    out.write('Blog')
    for word in wordlist:
        out.write('\t%s' % word)
    out.write('\n')
    for (blog, wc) in wordcounts.items():
        print (blog)
        out.write(blog)
        for word in wordlist:
            if word in wc:
                out.write('\t%d' % wc[word])
            else:
                out.write('\t0')
        out.write('\n')


def getwordcounts(url):
    try:
        sauce = urllib.request.urlopen(url).read()
        soup = bs.BeautifulSoup(sauce, 'lxml')

        wc = {}
        blog_title = soup.title.text
        items_pull = soup.find_all('item', limit=3)

        for item in items_pull:
            title = item.title.text
            words = title.split()
            garbage = ['-', '_', 'об', 'во', 'а', 'и', 'для', 'о', 'как', 'на', 'по', 'от', 'в', 'к', 'the', 'to',
                       'for', 'about', 'с']
            for word in words:
                word = word.strip('»"«_;:?*()!,.')
                word = word.lower()

                if word not in garbage:
                    wc.setdefault(word, 0)
                    wc[word] += 1
    except:
        print('HTTP error occured, damn it!')
        blog_title = None
        wc = None
    print(blog_title, wc)
    return blog_title, wc

