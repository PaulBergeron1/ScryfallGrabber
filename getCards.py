import json, requests, os, pyautogui, time
from PIL import Image

#access scryfall card database
def getallcardsdata():
                      
    request_url = requests.get('https://api.scryfall.com/bulk-data')
    request_data = requests.get(request_url.json()['data'][3]['download_uri'])
    return request_data.json()
c = 0
pyautogui.FAILSAFE = False

#creates art directory
os.makedirs("art", exist_ok=True)

#defines txt file name
filename = "cards.txt"
print("While program is running, pc sleep will be prevented")
#opens file
with open(filename, "r") as file:
    for line in file:
        card_name = line.strip()
        for card in getallcardsdata():
            #makes cards
            if card['lang'] == 'en' and card['name'] == card_name and card['border_color']!='gold' and card['image_status']=='highres_scan' and card['highres_image']==True and card['image_status']!='placeholder':
                r = requests.get(card['image_uris']['png'])
                card_name=card['name'] + '.jpg'
                result_card = os.path.join("art", card_name)
                open(result_card, 'wb').write(r.content)
                c+=1
                 
                #combines files
                base_path = os.path.dirname(os.path.abspath(__file__))
                image_path1 = os.path.join(base_path, 'blank.jpg')
                image_path2 = os.path.join(base_path, 'art', card['name'] + '.jpg')

                image1 = Image.open(image_path1).convert('RGBA')
                image2 = Image.open(image_path2).convert('RGBA')

                x_offset = (image1.width - image2.width) // 2
                y_offset = (image1.height - image2.height) // 2

                combined_image = Image.new('RGBA', image1.size)
                combined_image.paste(image1, (0, 0))
                combined_image.paste(image2, (x_offset, y_offset), mask=image2)

                output_folder = os.path.join(base_path, 'MPC Ready')
                os.makedirs(output_folder, exist_ok=True)

                output_path = os.path.join(output_folder, card['name']+'.png')
                combined_image.save(output_path)
                #prevents shutdown
                print("card number", c, ", card name, ", card['name'])
                for i in range(2):
                    pyautogui.press('shift')
