from bs4 import BeautifulSoup
import urllib2
import json

def writeAsJSON(content_infos_to_fetch, outputfile):
    try:
        with open(outputfile, 'wb') as outfile:
            json.dump(content_infos_to_fetch, outfile, indent=2)
    except Exception, e:
        print 'Failed to output to file %s' % e

spafinder=[['http://blog.spafinder.com/valentines-day-at-the-spa-treatments-couples/'],
['http://blog.spafinder.com/asian-beauty-10-big-brands/'],
['http://blog.spafinder.com/'],
['http://blog.spafinder.com/nude-resorts-spas-time-naked/'],
['http://blog.spafinder.com/category/beauty-2/'],
['http://blog.spafinder.com/spa-savant-valentines-day-deals-stressfree-february/'],
['http://blog.spafinder.com/secret-ingredient-zeaxanthin/'],
['http://blog.spafinder.com/what-is-a-couples-massage/'],
['http://blog.spafinder.com/category/healthy-eating-2/'],
['http://blog.spafinder.com/category/healthy-eating-2/'],
['http://blog.spafinder.com/new-year-new-you-your-2015-horoscope/?utm_source=SFNewsletter012715&utm_medium=email&utm_campaign=23859'],
['http://blog.spafinder.com/category/mindset/']]

kcet=[
['http://www.kcet.org/news/'],['http://www.kcet.org/socal/'],['http://www.kcet.org/living/'],['http://www.kcet.org/arts/'],['http://www.kcet.org/news/agenda/laws/california-department-of-water-resources.html'],['http://www.kcet.org/socal/la-food/top-ten-weird-la-food-spots.html'],['http://www.kcet.org/socal/summer/top-10-must-hike-trails.html'],['http://www.kcet.org/news/agenda/laws/new-california-laws-of-note-that-take-effect-in-2015.html'],['http://www.kcet.org/news/agenda/diversity/indian-teaching-credential.html'],['http://www.kcet.org/news/agenda/'],['http://www.kcet.org/news/agenda/parking/whats-the-story-behind-las-preferential-parking-districts.html']]



def getjsonfromurl(input,output):
    blah=[]
    for u in input[1:]:
        soup = BeautifulSoup(urllib2.urlopen(u[0]))
        title = soup.title.string
        title = title.encode('ascii', 'ignore')
        fb_meta = soup.find('meta', attrs={'property': 'og:description', 'content': True})
        if fb_meta:
            description = fb_meta['content']
            description = description.encode('ascii', 'ignore')
        else:
            description = ''
        temp = {}
        temp['url'] = u[0]
        temp['title'] = title
        temp['description'] = description
        temp['domain'] = 'blog.spafinder.com'
        blah.append(temp)
        writeAsJSON(blah, output)

getjsonfromurl(spafinder,'spafindertest.json')
getjsonfromurl(kcet,'kcettest.json')


 
 

