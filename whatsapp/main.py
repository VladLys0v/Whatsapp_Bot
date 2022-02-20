import pyautogui as pt
from time import sleep
import pyperclip
import random

sleep(2)

smile_emoji_path = "C:/Users/Vlad/Desktop/TESTER/Whatsapp-Bot/whatsapp/smiley_paperclip.png"
green_dott_emoji = "C:/Users/Vlad/Desktop/TESTER/Whatsapp-Bot/whatsapp/green_circle.jpg"

position1 = pt.locateOnScreen(smile_emoji_path, confidence=.6)
x =position1[0]
y =position1[1]


#Gets message
def get_message():
    global x,y

    position = pt.locateOnScreen(smile_emoji_path, confidence=.6)
    x = position[0]
    y = position[1]
    pt.moveTo(x,y, duration=.5)
    pt.moveTo(x + 100, y - 50, duration =.5)
    pt.tripleClick()
    pt.rightClick()
    pt.moveRel(12,15)
    pt.click()
    whatsapp_message = pyperclip.paste()
    pt.click()
    print("Message received" + whatsapp_message)
    return whatsapp_message


#Posts
def post_response(message):
    global x,y

    position = pt.locateOnScreen(smile_emoji_path, confidence=.6)
    x = position[0]
    y = position[1]
    pt.moveTo(x +120, y + 35, duration=.5)
    pt.click()
    pt.typewrite(message, interval = .01)

#this one will make bot send the message

    #pt.typewrite('\n', interval = .01)



#Processes the response

def process_response(message):
    random_no = random.randrange(3)
    if "how" or "what's up" in str(message).lower():
# for now it keeps answering to everyone like this
        return "i am fine, chilling"

    else:
        if random_no == 0:
            return "everything is awesome"
        elif random_no == 1:
            return "cool"
        else:
            return "give me a sec, i'll come back"


#alternative to the previous block, will delete it if it does not work
def process_affection(message):
    random_no = random.randrange(3)
    if "affection" in str(message).lower():
        if random_no == 0:
            return "come on, you know that i love you very much\n" \
                   "you are the most beautiful, carrying, compassionate and kind person\n" \
                   "whatever obstacle you have right now, you will over come it"
        elif random_no == 1:
            return "it will be ok, just take a nice hot relaxing bath, read a book or take a good nap\n" \
                   "p.s. i love you"
        else:
            return 'i am busy at the moment, i will answer in few minutes'


#Check for new messgaes
def check_for_new_messages():
    pt.moveTo(x+40,y-60, duration =.5)

    while True:
        #continuously checks for green dot and new messgaes
        try:
            position = pt.locateOnScreen(green_dott_emoji, confidence=.7)
            if position is not None:
                pt.moveTo(position)
                pt.moveRel(-100,0)
                pt.click()
                sleep(.5)

        except(Exception):
            print("No new users with new messages located")

        if pt.pixelMatchesColor(int(x+40), int(y-60), (255,255,255), tolerance=10):
            print("is white")

            processed_message = process_response(get_message())
#will need to delete it if it does not respond on affection word for now it copies the messagee twice - that is the issue
            processed_affection = process_affection(get_message())

            post_response(processed_message or processed_affection)

        else:
            print('no new messages')
        sleep(5)

check_for_new_messages()

