import requests

def f1():
    r = requests.get('https://ramadan.oybekdev.uz/api/ramadan/')
    response = r.json()
    l_sahar, l_iftor, data = [], [], []
    for i in range(30):
        a = response["dates"][i]["sehar"]
        b = response["dates"][i]["iftar"]
        c = response["dates"][i]["melod_date"]
        l_sahar.append(a)
        l_iftor.append(b)
        data.append(c)
    time_sahar = dict(zip(data, l_sahar))
    time_iftor = dict(zip(data, l_iftor))
    return time_sahar, time_iftor
if __name__ == '__main__':
    print(f1()[0])

