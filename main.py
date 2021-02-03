from turtle import pd
from espn_api.basketball import League
from espn_api.basketball import Team
from espn_api.basketball import Player
from espn_api.basketball.constant import STATS_MAP
from inflect import val
from termcolor import colored

mainLeague = League(1107053257, 2021,
                    'ESPN S2',
                    'SWID')
listOfTeamsPlaying = mainLeague.standings()
agents = mainLeague.free_agents(size=150)

#tester = mainLeague.free_agents()[3]
#print(tester.__dict__['stats'].keys())
#print(tester)
#print(tester.__dict__['injuryStatus'])
#print(tester.__dict__['stats'])  #: Full Season Stats (2021)
# print(tester.__dict__['stats']['002021'])  #: Full Season Stats (2020)
# print(tester.__dict__['stats']['102021'])  #: Projected Stats for Season
# print(tester.__dict__['stats']['012021'])  #: Last 7 Days Stats
# print(tester.__dict__['stats']['022021'])  #: Last 15 Days Stats
# print(tester.__dict__['stats']['032021'])  #: Last 30 Days Stats


# Field goals made: 2
# Field goals missed: -1
# Free-throws made: 1
# Free throws missed: -1
# Three points: 1
# Rebounds: 1
# Assists: 2
# Steals: 4
# Blocks: 4
# Turnovers: -2
# Points: 1

def myPoints(player):
    points = 0
    points += player.__getattribute__('stats')['022021']['avg']['FGM'] * 2
    points -= player.__getattribute__('stats')['022021']['avg']['FGM'] - player.__getattribute__('stats')['022021']['avg']['FGA']
    points += player.__getattribute__('stats')['022021']['avg']['FTM']
    points -= player.__getattribute__('stats')['022021']['avg']['FTA'] - player.__getattribute__('stats')['022021']['avg']['FTM']
    points += player.__getattribute__('stats')['022021']['avg']['3PTM']
    points += player.__getattribute__('stats')['022021']['avg']['OREB'] + player.__getattribute__('stats')['022021']['avg']['DREB']
    points += player.__getattribute__('stats')['022021']['avg']['AST'] * 2
    points += player.__getattribute__('stats')['022021']['avg']['STL'] * 4
    points -= player.__getattribute__('stats')['022021']['avg']['TO'] * 2
    points += player.__getattribute__('stats')['022021']['avg']['PTS']
    return points

playersDic = {}


for players in agents:
    if players.__getattribute__('injuryStatus') == 'ACTIVE' and '022021' in players.__getattribute__('stats').keys() and players.__getattribute__('stats')['022021']['avg']['MIN'] >= 20:
        playersDic[players] = myPoints(players) / players.__getattribute__('stats')['022021']['avg']['MIN']


def get_key(val):
    for key, value in playersDic.items():
        if val == value:
            return key
    return "key doesn't exist"


count = 0

for i in sorted(playersDic.values(), reverse=True):
count += 1
print(str(count) + '.', colored(get_key(i), 'green'), '||', round(i, 2), colored("(PPM)", 'red'), '||', get_key(i).__getattribute__('stats')['022021']['avg']['MIN'], colored("(Mins)", 'red'))

# 1.Get the minutes from every game each player plays
# 2. Calculate the Percent Change from this season and last season
# 3. Rank based on sqaure root ( x^2 + y^2  ), x = ppm, y = percent change or line of best fit, and get the slope of that
# 4. Create a user interface
