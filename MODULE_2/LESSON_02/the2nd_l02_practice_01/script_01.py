import requests
def random_joke():
    BASE_URL = "https://icanhazdadjoke.com"
    r = requests.get(BASE_URL, headers={'Accept':'application/json'})
    data = r.json()
    joke = data['joke']
    print(joke)
    filename = data['id'] + '.txt'
    with open(filename, 'w') as f:
        f.write(joke)
random_joke()
