import sys
if sys.version_info[0]!=3:
    sys.exit("BCS needs Python 3.0")

import urllib.request
import json

# TODO: Check for Platinum Stars that have already been awarded
# Progress: It seems to work, although type errors result

# TODO: Distinguish between pistols, as these have half kills
# Progress: Done, needs testing

# TODO: Add some error handling for incorrectly-typed usernames
# Progress: Spell your name right, newb.

# TODO: Add in some memory between program runs
# Progress: To be added when adapted for web / exe

def retrievestats():

    print("Welcome to BCS.")
    platform = input("What platform? PC|360|PS3. Default is PC. ")
    players = input("What players? Separate with commas. Default is devs. ")

    # defaults...
    if platform == "": platform = "PC"
    if players == "": players = "VelocityGirl,Irnn"
    fields = "weapons"
    URL = "http://api.bfbcs.com/api/" + platform + "?players=" + players + "&fields=" + fields
    
    f = urllib.request.urlopen(URL).read()
    stats = json.loads(f.decode("utf-8"))
    # f.close()
    
    return stats

def printbasics(stats):
    print("You're returning data for these players:")
    
    
    for player in stats['players']:
        comingup = []
        print("%(name)s, rank %(rank)d." % player)
        for weapon in player['weapons']:
            
            if weapon in {"mp443","m9","m1911","mp412","m93r","tt33"}:
                # print("Pistol Detected!" + weapon)
                ispistol = 1
            else:
                ispistol = 0
                
            kills = player['weapons'][weapon]['kills']
            try:
                if player['weapons'][weapon]['stars']['plat'] == 1:
                    pass
                    # print("PLATTED ALREADY: " + weapon + " with " + str(kills) + " kills")
                else:
                    needxmore = nextstar(kills,ispistol)
                    comingup.append((needxmore,kills,str(weapon)))
            except TypeError:
                # TODO: Fix this TypeError :)
                # Some kind of type error here, after it works for the first few 31 or 34 weapons for some reason
                # print("OH SHIT TYPE ERROR")
                pass
        comingup.sort()
        prettify(logic(comingup))
    return

def prettify(final):
    print("Next 5 Stars")
    for index, item in enumerate(final):
        if index > 4: break
        value = item[0]
        kills = item[1]
        name = item[2]
        print(str(index+1) + ". " + name + " - " + str(kills) + " more kills, overall value is " + str(value))


    return

def nextstar(kills,ispistol):
    
    if ispistol == 0:
        
        if kills < 25:          return 25 - kills  #bronze
        if 25 <= kills < 50:    return 50 - kills  #silver
        if 50 <= kills < 100:   return 100 - kills #gold
        if 100 <= kills < 200:  return 200 - kills
        if 200 <= kills < 300:  return 300 - kills
        if 300 <= kills < 400:  return 400 - kills
        if 400 <= kills < 500:  return 500 - kills
        if 500 <= kills < 600:  return 600 - kills
        if 600 <= kills < 700:  return 700 - kills
        if 700 <= kills < 800:  return 800 - kills
        if 800 <= kills < 900:  return 900 - kills
        if 900 <= kills < 1000: return 1000 - kills #platinum
        if kills >= 1000: return 1000

    if ispistol == 1:
        
        if kills < 10:          return 10 - kills  #bronze
        if 10 <= kills < 25:    return 25 - kills  #silver
        if 25 <= kills < 50:    return 50 - kills #gold
        if 50 <= kills < 100:   return 100 - kills
        if 100 <= kills < 150:  return 150 - kills
        if 150 <= kills < 200:  return 200 - kills
        if 200 <= kills < 250:  return 250 - kills
        if 250 <= kills < 300:  return 300 - kills
        if 300 <= kills < 350:  return 350 - kills
        if 350 <= kills < 400:  return 400 - kills
        if 400 <= kills < 450:  return 450 - kills
        if 450 <= kills < 500: return 500 - kills #platinum
        if kills >= 500: return 1000


def logic(nsr):

    final = []

    for index, item in enumerate(nsr):
        xmore = item[0]
        kills = item[1]
        weapon = item[2]
        
        if kills < 25: value = 500 / xmore
        if 25 <= kills < 50: value = 1000 / xmore
        if 50 <= kills < 900: value = 5000 / xmore
        if 900 <= kills < 1000: value = 10000 / xmore
        
        final.append((value, xmore, weapon,))
       
    final.sort(reverse=True)
    return final

if __name__ == '__main__':
    stats = retrievestats()
    printbasics(stats)

