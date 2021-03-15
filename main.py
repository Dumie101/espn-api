from math import sqrt
from espn_api.basketball import League
from termcolor import colored

#vars#
playersDic = {}
statsDic = {}
minsList = []
xAxis = [1, 2, 3]
slope = 0
count = 0


# Intializing myLeague : your league_id: int, your year: int, your espn_s2=None, your swid=None #
mainLeague = League('league_id', 'year',
                    'espn_s2',
                    'swid')

listOfTeamsPlaying = mainLeague.standings()
agents = mainLeague.free_agents(size=200)


# Function for Fantasy Points (Last 15 Days) #
def myPoints(player):
    points = 0
    points += player.__getattribute__('stats')['032021']['avg']['FGM'] * 2
    points -= player.__getattribute__('stats')['032021']['avg']['FGM'] - \
              player.__getattribute__('stats')['032021']['avg']['FGA']
    points += player.__getattribute__('stats')['032021']['avg']['FTM']
    points -= player.__getattribute__('stats')['032021']['avg']['FTA'] - \
              player.__getattribute__('stats')['032021']['avg']['FTM']
    points += player.__getattribute__('stats')['032021']['avg']['3PTM']
    points += player.__getattribute__('stats')['032021']['avg']['OREB'] + \
              player.__getattribute__('stats')['032021']['avg']['DREB']
    points += player.__getattribute__('stats')['032021']['avg']['AST'] * 2
    points += player.__getattribute__('stats')['032021']['avg']['STL'] * 4
    points -= player.__getattribute__('stats')['032021']['avg']['TO'] * 2
    points += player.__getattribute__('stats')['032021']['avg']['PTS']
    return points

# Main Code to Create Dictionary { PlayerName : Ranking Metric  } #
for players in agents:
    if (players.__getattribute__('injuryStatus') == 'ACTIVE') and (
            '012021' in players.__getattribute__('stats').keys()) and (
            '022021' in players.__getattribute__('stats').keys()) and (
            players.__getattribute__('stats')['032021']['avg']['MIN'] >= 20):

        # vars #
        pointsPerMin = myPoints(players) / players.__getattribute__('stats')['022021']['avg']['MIN']

        lastSevenDayAverageMin = players.__getattribute__('stats')['012021']['avg']['MIN']
        lastFifteenDayAverageMin = players.__getattribute__('stats')['022021']['avg']['MIN']
        lastThirdlyDayAverageMin = players.__getattribute__('stats')['032021']['avg']['MIN']

        minsList.append(lastThirdlyDayAverageMin)
        minsList.append(lastFifteenDayAverageMin)
        minsList.append(lastSevenDayAverageMin)

        # Slope Calculation: See Equations.txt #
        for num in range(0, 3):
            xSum = 6
            ySum = + minsList[num]
            xySum = + minsList[num] * xAxis[num]
            delta = 6
            slope = 3 * xySum - (xSum * ySum) / 6

        # Distance Formula: See Equations.txt #
        xValue = slope ** 2
        yValue = pointsPerMin ** 2
        ranking = sqrt((0.7 * xValue) + (0.3 * yValue))

        playersDic[players] = ranking

        minsList.clear()


#Method for getting key value#
def get_key(val):
    for key, value in playersDic.items():
        if val == value:
            return key
    return "key doesn't exist"

#Printing#
for i in sorted(playersDic.values(), reverse=True):
    count += 1
    print(str(count) + '.', colored(get_key(i).__getattribute__('name'), 'red'))
