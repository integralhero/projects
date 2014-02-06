#Little web crawler. Doesn't have looping protection
import re
import urllib2
import urllib
 
target = 'https://www.kamcord.com/developers/' 
visited = []

def spider(curURL):
    curURL = urllib.quote(curURL, safe="/:=&?#+!$,;'@()*[]")
    #print "Looking at  " + curURL
    if not(curURL in visited):
        visited.append(curURL)
    
    site=""
    try:
        site = urllib2.urlopen(curURL)
    except urllib2.HTTPError, e:
        return

    page = site.read()
    
    links = re.findall('<[aA][^>]*>([^<]+)</[aA]>', page)
    for link in links:
        fullURL =  curURL.partition('?')[0].rpartition('/')[0]+"/"+ str(link)
        spider(fullURL) #recursive call
    return
 
spider(target)
print visited
print "We found " + str(len(visited)) + " pages!"
