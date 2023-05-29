import json, requests, os
    
def getallcardsdata(): #downloads the current all-cards.json file from scryfall. Just reads to memory, doesn't save it to a file.
                      
    request_url = requests.get('https://api.scryfall.com/bulk-data')
    request_data = requests.get(request_url.json()['data'][3]['download_uri'])
    return request_data.json()
c = 0
os.makedirs("art", exist_ok=True)
filename = "cards.txt"
with open(filename, "r") as file:
    for line in file:
        card_name = line.strip()
        for card in getallcardsdata():
            if card['lang'] == 'en' and card['name'] == card_name:
                r = requests.get(card['image_uris']['png'])
                card_name=card['name'] + '.jpg'
                result_card = os.path.join("art", card_name)
                open(result_card, 'wb').write(r.content)
                c+=1
                print("card number", c, ", card name, ", card['name'])
