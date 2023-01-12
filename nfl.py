TEAMS = {"Raiders":1, "Jaguars":2, "Patriots":3, "Giants":4, "Ravens":5, "Titans":6, "Lions":7, "Falcons":8, "Browns":9, "Bengals":10,
         "Cardinals":11, "Eagles":12, "Jets":13, "49ers":14, "Packers":15, "Bears":16, "Chiefs":17, "Commanders":18, "Panthers":19,
         "Bills":20, "Colts":21, "Steelers":22, "Seahawks":23, "Buccaneers":24, "Dolphins":25, "Texans":26, "Saints":27, "Broncos":28,
         "Cowboys":29, "Chargers":30, "Rams":31, "Vikings":32}

import http.client
import json

def main():
    print("well well well")
    team = input("Enter the team: eg Eagles of Chiefs ")
    get_data(TEAMS[team])

def get_data(team, player):
    link = "/players/statistics?team="+str(team)+"&season=2022"
    conn = http.client.HTTPSConnection("v1.american-football.api-sports.io")

    headers = {
        'x-rapidapi-host': "v1.american-football.api-sports.io",
        'x-rapidapi-key': "2f16913deceba91e002f073433d34748"
    }

    conn.request("GET", link, headers=headers)

    res = conn.getresponse()
    data = res.read()
    read(data, player)

def read(data, player):
    js = json.loads(data)


    for i in range(len(js['response'])):
        if js['response'][i]['player']['name'] == player:
            id = js['response'][i]['player']['id']
            break
    get_player(id)

def get_player(id):
    string = ""
    link = "/players/statistics?id="+str(id)+"&season=2022"
    conn = http.client.HTTPSConnection("v1.american-football.api-sports.io")

    headers = {
        'x-rapidapi-host': "v1.american-football.api-sports.io",
        'x-rapidapi-key': "2f16913deceba91e002f073433d34748"
    }

    conn.request("GET", link, headers=headers)

    res = conn.getresponse()
    data = res.read()
    js = json.loads(data)
    for key in js['response'][0]['teams'][0]['groups']:
        for stat in key['statistics']:
            if stat['value'] != str(0):
                string += stat['name'], ":", stat['value']
        string += "\n\n\n"

    return string

main()

#2f16913deceba91e002f073433d34748
