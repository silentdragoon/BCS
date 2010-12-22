import urllib, json


def retrievestats():
    
    players = "VelocityGirl,Irnn"
    fields = "weapons"
    
    params = "players=" + players + "&fields=" + fields
    f = urllib.urlopen("http://api.bfbcs.com/api/pc?", params)
    
    stats = json.load(f)
    print stats
    f.close()
    
    return stats

def printbasics(stats):
    print "You're returning data for these players:"
    for player in stats[u'players']:
        print u"%(name)s, rank %(rank)d." % player
    return
    

if __name__ == '__main__':
    stats = retrievestats()
    printbasics(stats)
    
    pass