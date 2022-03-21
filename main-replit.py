from pytube import YouTube
from os import system
from time import sleep



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
    print(header_final)
    print("[?] Youtube video link URL ↓")
    link = input("")
    yt = YouTube(link)
    sleep(1)

    #Showing details
    if link.startswith("https://youtu.be/"):
        try:
            print(header_final)
            print("[!] Title : " + yt.title)
            print("[!] Number of views : " + str(yt.views))
            print("[!] Length of video : " + str(yt.length))
            print("[!] Rating of video : " + str(yt.rating))
            sleep(1)
            #Getting the highest resolution possible
            ys = yt.streams.get_highest_resolution()            

            print("[?] Do you want to download the video ? y for yes ; n for no")
            answer = input()

            if answer == ("y"):
                #Starting download
                print("[!] Starting download...")
                ys.download()
                print("[!] Download complete, 3 seconds before script restarting")
                sleep(3)

            elif answer == ("n"):
                print("[!] No download, 3 seconds before script restarting")
                sleep(3)
            
            else:
                print("[!] Answer is not y or no, restarting the script in 3 seconds")
                sleep(3)

        except: 
            system('cls')
            print("[!] Error !")
            sleep(2)


    else:
        system('cls')
        print("[!] Invalid link !")
        sleep(2)
