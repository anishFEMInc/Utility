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

#subdirectory=old

def score(old,new,num):
    data=json.load(open(old))
    print "The Score is:"
    data2=json.load(open(new))
    score=0
    j=0
    for i in range(0,num):
        if (data['results'][i]['videoid']==data2['results'][i]['videoid']):
            score=score+2
        else:
            for j in range(0,num):
                if (data['results'][i]['videoid']==data2['results'][j]['videoid']):
                    score=score+1
    print score
    return score




inputfile='data.json'
#outputfile='result.text'
#outputfile2='result.json'
endpoint = "http://localhost:8080/"
list=[]


#file=open(outputfile,'w')
#file2=open(outputfile2,'w')
#data=json.load(open(inputfile))
data = json.load(open(inputfile))
# data holds all the url,domains for all the partners
size=len(data)
olddir='/Users/anishacharya/Desktop/new'



for i in range(0,size-1):
    url=data[i]["url"]
    # url="http://www.hitfix.com/comedy/10-funny-answers-from-keegan-michael-key-and-jordan-peeles-ama"    						#get URL and Domain from JSON
    #domain= "www.hitfix.com"
    domain=data[i]["domain"]
    string = endpoint +'getRelevantVideos?url='+url+'&domain='+domain
    r = requests.get(string)
    #with open(inputfile,'wb')as f
    #file.write(r.text)
    #list.append(r.json())
    #list.append(r.text)
    #print list
    #json.dump(r.json(),file2, indent=2)
    print i
    #filename=str(i)+'.json'
    filename=str(i)+'new'+'.json'
    #print filename
    #fout=open(os.path.join)
    #print os.getcwd()
    with cd(olddir):
        fout=open(filename, 'w')
        json.dump(r.json(),fout, indent=2)
    #file.write(r)
    #file.close()
    #r.text
    #print(r.text)

with cd(olddir):
    score=score('1new.json','0new.json',10)
    print score
#file=open('TEST.json','wb')
#json.dump(list,file,indent=2)
print os.getcwd()
