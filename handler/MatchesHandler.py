import requests
import json
from domain.PlayerMatch import PlayerMatch
from domain.Hero import Hero

heroes = []


# 99255581
def find_matches(playerId):
    res = requests.get('https://api.opendota.com/api/players/{}/recentMatches'.format(playerId))
    matches = json.loads(res.text)
    fill_hero_list()
    return create_player_matchs(matches)


def create_player_matchs(matches):
    playerMatchs = []

    for match in matches:
        result = verify_match_result(match["player_slot"], match["radiant_win"])
        heroi = next((x for x in heroes if x.id == match["hero_id"]), None)
        playerMatchs.append(PlayerMatch(result, heroi, match["kills"], match["deaths"], match["assists"]))

        if len(playerMatchs) == 10:
            break

    print(playerMatchs)

    return playerMatchs


def verify_match_result(slot, radiant_win):
    time = "Radiant" if slot <= 127 else "Dire"
    radiant = radiant_win
    if radiant and time == "Radiant":
        return "Vitoria"
    elif radiant is False and time == "Dire":
        return "Vitoria"
    else:
        return "Derrota"


def fill_hero_list():
    with open('data/heroes.json', encoding='utf-8') as data_file:
        hero_data = json.loads(data_file.read())
    for hero in hero_data:
        heroes.append(Hero(hero["id"], hero["localized_name"]))
