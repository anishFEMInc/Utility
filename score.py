import requests
import json
import itertools
import os.path


from contextlib import contextmanager
import os

@contextmanager
def cd(newdir):
    prevdir = os.getcwd()
    os.chdir(newdir)
    try:
        yield
    finally:
        os.chdir(prevdir)


def score(old,new,num):
    data=json.load(open(old))
    print "The Score is:"
    data2=json.load(open(new))
    score=0
    j=0
    for i in range(0,num-1):
        if (data['results'][i]['videoid']==data2['results'][i]['videoid']):
            score=score+2
        else:
            for j in range(0,num-1):
                if (data['results'][i]['videoid']==data2['results'][j]['videoid']):
                    score=score+1
    print score
    return score

#Score=[]

for i in range(0,10):
    old=str(i)+'.json'
    new=str(i)+'new'+'.json'
    with cd('/Users/anishacharya/Desktop/new'):
        Score=score(old,new,10)
    print Score
