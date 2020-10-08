from riotwatcher import RiotWatcher, ApiError
from Constants import tokens
from Constants import text_constants
import requests
regionDict = {
    "EUNE": "EUN1",
    "EUW": "EUW1",
    "NA": "NA1",
    "RU": "RU",
    "KR": "KR",
    "BR": "BR1",
    "OC": "OC1",
    "JP": "JP1",
    "TR": "TR1",
    "LA": "LA1"
}

rolesDict = {
    "TOP": "Top",
    "JUNGLE": "Jungle",
    "MID": "Mid",
    "ADC": "Adc",
    "SUPP": "Supp"
}

dotaDic = {
    "CARRY": "Carry",
    "MID": "Mid",
    "OFFLANE": "Offlane",
    "SOFT SUPPORT": "Soft Support",
    "HARD SUPPORT": "Hard Support"
}


def getSummonerRank(summonerName, region):
    server = regionDict[str(region).upper()]
    watcher = RiotWatcher(tokens.lolapikey)
    try:
        summoner = watcher.summoner.by_name(server, summonerName)
    except:
        return text_constants.NOT_FOUND
    my_ranked_stats = watcher.league.by_summoner(server, summoner['id'])
    for rank in my_ranked_stats:
        if rank['queueType'] == "RANKED_SOLO_5x5":
            return rank['tier']


def getValoRank(gameName, tagline):
    url = "https://europe.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{}/{}?api_key={}".format(gameName, tagline,tokens.lolapikey)
    print(url)
    # headers = {
    #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
    #     "Accept-Language": "en-US,en;q=0.9",
    #     "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    #     "Origin": "https://developer.riotgames.com",
    #     "X-Riot-Token": tokens.lolapikey
    # }
    response = requests.request("GET", url, timeout=5)
    print(response)

