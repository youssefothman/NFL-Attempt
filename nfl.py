def main():

    import http.client

    conn = http.client.HTTPSConnection("v1.american-football.api-sports.io")

    headers = {
        'x-rapidapi-host': "v1.american-football.api-sports.io",
        'x-rapidapi-key': "2f16913deceba91e002f073433d34748"
    }

    conn.request("GET", "/players/statistics?team=1&season=2018", headers=headers)

    res = conn.getresponse()
    data = res.read()
    read(data)

def read(data):
    import json
    js = json.loads(data)

    for thing in js:
        print(thing)
    print(js['response'])



main()

#2f16913deceba91e002f073433d34748
