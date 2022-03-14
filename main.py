from turtle import title
from pytube import YouTube
from pystyle import Colorate, Colors, Center
from os import system
from time import sleep
import colorsys


boucle1 = True

header_final = """
           .         .
          ,8.       ,8.              ,o888888o.     `8.`8888.      ,8'
         ,888.     ,888.          . 8888     `88.    `8.`8888.    ,8'
        .`8888.   .`8888.        ,8 8888       `8b    `8.`8888.  ,8'
       ,8.`8888. ,8.`8888.       88 8888        `8b    `8.`8888.,8'
      ,8'8.`8888,8^8.`8888.      88 8888         88     `8.`88888'
     ,8' `8.`8888' `8.`8888.     88 8888         88     .88.`8888.
    ,8'   `8.`88'   `8.`8888.    88 8888        ,8P    .8'`8.`8888.
   ,8'     `8.`'     `8.`8888.   `8 8888       ,8P    .8'  `8.`8888.
  ,8'       `8        `8.`8888.   ` 8888     ,88'    .8'    `8.`8888.
 ,8'         `         `8.`8888.     `8888888P'     .8'      `8.`8888.

  V 1.0 - Arthurdufinister#3286 - discord.gg/BtNrFc45B7\n\n\n\n"""


while boucle1: 

    #ask for the link from user
    system('cls')
    print(Colorate.Diagonal(Colors.red_to_purple, Center.XCenter(header_final)))
    print(Colorate.Horizontal(Colors.red_to_purple, "[?] Youtube video link URL ↓"))
    link = input("")
    yt = YouTube(link)
    sleep(1)

    #Showing details
    if link.startswith("https://youtu.be/"):
        try:
            system('cls')
            print(Colorate.Diagonal(Colors.red_to_purple, Center.XCenter(header_final)))
            print(Colorate.Horizontal(Colors.red_to_purple, "[!] Title : " + yt.title))
            print(Colorate.Horizontal(Colors.red_to_purple, "[!] Number of views : " + str(yt.views)))
            print(Colorate.Horizontal(Colors.red_to_purple, "[!] Length of video : " + str(yt.length)))
            print(Colorate.Horizontal(Colors.red_to_purple, "[!] Rating of video : " + str(yt.rating)))
            
            #Getting the highest resolution possible
            ys = yt.streams.get_highest_resolution()
            sleep(2)

            print(Colorate.Horizontal(Colors.red_to_purple, "[?] Do you want to download the video ? y for yes ; n for no"))
            answer = input()

            if answer == ("y"):
                #Starting download
                print(Colorate.Horizontal(Colors.red_to_purple, "[!] Starting download..."))
                ys.download()
                print(Colorate.Horizontal(Colors.red_to_purple, "[!] Download complete, 3 seconds before script restarting"))
                sleep(3)

            elif answer == ("n"):
                print(Colorate.Horizontal(Colors.red_to_purple, "[!] No download, 3 seconds before script restarting"))
                sleep(3)
            
            else:
                print(Colorate.Horizontal(Colors.red_to_purple, "[!] Answer is not y or no, restarting the script in 3 seconds"))
                sleep(3)

        except: 
            system('cls')
            print(Colorate.Horizontal(Colors.red_to_purple, "[!] Error !"))
            sleep(2)


    else:
        system('cls')
        print(Colorate.Horizontal(Colors.red_to_purple, "[!] Invalid link !"))
        sleep(2)
