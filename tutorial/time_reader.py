import pytesseract
from discord_webhook import DiscordEmbed, DiscordWebhook
import cv2
import time

iterazione = 0


def check_time(time):
    pass


if iterazione % 2000:  # ogni 2k iteazioni esegue
    temp = pytesseract.image_to_string('time.png')
    while (check_time(time)):
        time.sleep(1)
        temp = pytesseract.image_to_string('time.png')
        if temp == False:
            pass  # errore
