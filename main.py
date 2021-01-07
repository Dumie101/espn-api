from espn_api.basketball import League
from espn_api.basketball import Team
from espn_api.basketball import Player
from espn_api.basketball.constant import STATS_MAP

mainLeague = League(1107053257, 2021,
                    'MY-SWID',
                    'MY-ESPN')
listOfTeamsPlaying = mainLeague.standings()
agents = mainLeague.free_agents()

"""
tester = mainLeague.free_agents()[3]
print(tester.__dict__['injuryStatus'])
print(tester.__dict__['stats']['002020']['avg']['MPG'])  #: Full Season Stats (2021)
print(tester.__dict__['stats']['002021'])  #: Full Season Stats (2020)
print(tester.__dict__['stats']['102021'])  #: Projected Stats for Season
print(tester.__dict__['stats']['012021'])  #: Last 7 Days Stats
print(tester.__dict__['stats']['022021'])  #: Last 15 Days Stats
print(tester.__dict__['stats']['032021'])  #: Last 30 Days Stats

"""

# removes injuryed players and players who have less that 20 min of playing time (last 30 days) #
def removePlayers(freeAgents):
    for player in freeAgents:
        if player.__dict__['injuryStatus'] == 'OUT':
            freeAgents.remove(player)
        try:
            if player.__dict__['stats']['032021']['avg']['MPG'] < 20:
                print(player)
                freeAgents.remove(player)
        except:
            continue

    return freeAgents


print(removePlayers(agents))
