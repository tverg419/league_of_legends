from riotwatcher import LolWatcher, ApiError
import pandas as pd

api_key = 'RGAPI-xxxxx'
watcher = LolWatcher(api_key)
my_region = 'na1'

summoner_name = 'MG Oblivion'
me = watcher.summoner.by_name(my_region, summoner_name)
print(me)

# ranked_stats = watcher.league.by_summoner(my_region, me['id'])
# print(ranked_stats)

my_matches = watcher.match.matchlist_by_account(my_region, me['accountId'])
last_match = my_matches['matches'][0]
match_detail = watcher.match.by_id(my_region, last_match['gameId'])

participants = []
for row in match_detail['participants']:
    participants_row = {}
    participants_row['champion'] = row['championId']
    participants_row['spell1'] = row['spell1Id']
    participants_row['spell2'] = row['spell2Id']
    participants_row['win'] = row['stats']['win']
    participants_row['kills'] = row['stats']['kills']
    participants_row['deaths'] = row['stats']['deaths']
    participants_row['assists'] = row['stats']['assists']
    participants_row['totalDamageDealt'] = row['stats']['totalDamageDealt']
    participants_row['goldEarned'] = row['stats']['goldEarned']
    participants_row['champLevel'] = row['stats']['champLevel']
    participants_row['totalMinionsKilled'] = row['stats']['totalMinionsKilled']
    participants_row['item0'] = row['stats']['item0']
    participants_row['item1'] = row['stats']['item1']
    participants.append(participants_row)
df = pd.DataFrame(participants)
print(df)
