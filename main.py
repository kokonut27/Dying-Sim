import time, os, getkey, random
#from replit import db
#import json, pickle


#editting stuff
Red = "\033[0;31m"
Green = "\033[0;32m"
Orange = "\033[0;33m"
Blue = "\033[0;34m"
Purple = "\033[0;35m"
Cyan = "\033[0;36m"
White = "\033[0;37m" 
black = "\033[0;30m"
red = "\033[0;91m"
green = "\033[0;92m"
yellow = "\033[0;93m"
blue = "\033[0;94m"
magenta = "\033[0;95m"
cyan = "\033[0;96m"
cyan_back = "\033[0;46m"
purple_back = "\033[0;45m"
white_back = "\033[0;47m"
blue_back = "\033[0;44m"
orange_back = "\033[0;43m"
green_back = "\033[0;42m"
pink_back = "\033[0;41m"
grey_back = "\033[0;40m"
grey = '\033[38;4;236m'
bold = "\033[1m"
underline = "\033[4m"
italic = "\033[3m"
darken = "\033[2m"
invisible='\033[08m'
reverse='\033[07m'
reset='\033[0m'
grey = "\x1b[90m"


#starting functions
def clear():#very handy function btw
  os.system('clear')

def next():
  print(Orange+'\nPress any <KEY> to continue'+White)
  getkey.getkey()#so it can actually press any key
  clear()

inputsymbol='☠️️️️ >'
title=(Red+'Dying Simulator!'+White)
print(title)
time.sleep(2)
next()

menu1=True
bonus = 0
deaths = 1
chance = 0
thingy = 1
while menu1:
  print(Red+'DIE MENU! v1'+White)
  print('[1] Play\n[2] Help')
  menu1e=input(Red+'☠️ > '+White)
  clear()

  if menu1e == '1':
    playmenu=True
    menu1=False

  elif menu1e == '2':
    print(Red+'DEATH HELP!'+White)
    print('Basically, this is a clicker game, you have to keep dying, get upgrades, and etc. You also start with 1 death. Another note is that you have to reach 777 deaths, 777 rebirths, and 777 bonus!')#add
    next()

  else:
    print(Red+'Invalid DEATH Command!'+White)
    next()

while playmenu:
  if deaths <= 0:
    print(Red+"You lived, so you died. (confusing, right?) Bai Bai.")
    time.sleep(4)
    clear()
    playmenu=False
  elif deaths == 777 and chance == 777 and bonus == 777:
    print(Green+"You won! Hooray! Share this message: 'This Sucks!' in the comments! lol. Bai!"+White)
    time.sleep(4)
    clear()
    playmenu=False
  else:
    print(Red+'DEATH PLAY MENU!'+White)
    print('[1] Try to die\n[2] Try to live\n[3] Click this and become pog\n[4] View ur Stats\n[5] Spin da wheel of deaths')
    a=input(Red+'☠️️️️ > '+White)
    clear()

    if a == '1':
      num = random.randint(1, 2)
      NUM = num + bonus
      print(f"You died {NUM} times! That is WITH the bonus (whether or not you have a bonus lol)")
      deaths += NUM
      next()

    elif a == '2':
      print("You rebirthed.\nStupid idea btw, you have to DIE in this game. +10 lives (lol)\nBut you got +1 chance")#not actually too stupid, but yea
      deaths -= 10
      chance += 1
      next()

    elif a == '3':
      print("Will you use ur chance? y/n")
      yn = input('> ').lower()
      clear()

      if yn == 'y':
        if thingy == 1:
          if chance >= 1:
            print("You used your chance and you get a small bonus of deaths")
            chance -= 1
            bonus += 2
            thingy += 1
          else:
            print(Red+"You don't have enough chance/rebirths!"+White)
        elif thingy == 2:
          if chance >= 2:
            print("You used your chance and you get a small bonus of deaths")
            chance -= 2
            bonus += 2
            thingy += 1
          else:
            print(Red+"You don't have enough chance/rebirths!"+White)
        elif thingy == 3:
          if chance >= 3:
            print("You used your chance and you get a small bonus of deaths")
            chance -= 3
            bonus += 2
            thingy += 1
          else:
            print(Red+"You don't have enough chance/rebirths!"+White)
        elif thingy == 4:
          if chance >= 4:
            print("You used your chance and you get a small bonus of deaths")
            chance -= 4
            bonus += 2
            thingy += 1
          else:
            print(Red+"You don't have enough chance/rebirths!"+White)
        elif thingy == 5:
          if chance >= 5:
            print("You used your chance and you get a small bonus of deaths")
            chance -= 5
            bonus += 2
            thingy += 1
          else:
            print(Red+"You don't have enough chance/rebirths!"+White)
        elif thingy == 6:
          if chance >= 6:
            print("You used your chance and you get a small bonus of deaths")
            chance -= 6
            bonus += 2
            thingy += 1
          else:
            print(Red+"You don't have enough chance/rebirths!"+White)
        elif thingy == 7:
          if chance >= 7:
            print("You used your chance and you get a small bonus of deaths")
            chance -= 7
            bonus += 2
            thingy += 1
          else:
            print(Red+"You don't have enough chance/rebirths!"+White)
        elif chance >= 7:
          print("You used your chance and you get a small bonus of deaths")
          chance -= 7
          bonus += 2
          thingy += 2
        else:
          print(Red+"You don't have enough chance/rebirths!"+White)
        time.sleep(2)
        clear()
      elif yn == 'n':
        print("Ok. Going back to menu...")
        time.sleep(2)
        clear()

    elif a == '4':
      if deaths == 1:
        print(f"Ur stats are:\n- {deaths} Death\n- {chance} Chances/Rebirths\n- {bonus} Bonus")
      else:
        print(f"Ur stats are:\n- {deaths} Deaths\n- {chance} Chances/Rebirths\n- {bonus} Bonus")
      next()
    elif a == '5':
      print(Red+"Da Wheel of Deaths!"+White)
      print("[1] Spin da wheel\n[2] Help\n[3] Back")
      wd = input("☠️️️️ > ")
      clear()

      if wd == '3':
        pass
      elif wd == '2':
        print("Pay 10 deaths, and 1 chance to spin the wheel. You might get a prize or you might flunk. Your choice. lol")
        next()
      elif wd == '1':
        yn = input("Will you pay 10 deaths and 1 chance? y/n\n☠️️️️ > ").lower()
        clear()

        if yn == 'y':
          if deaths >= 10 and chance >= 1:
            deaths-=10
            chance-=1
            wheel_list = [1,2,3,4,5,6,7]
            abc = random.choice(wheel_list)
            print("Spinning...")
            time.sleep(2)
            print()
            if abc == 1:
              print(Green+"You got 20 deaths!"+White)
              deaths+=20
            elif abc == 2:
              print(Green+"You lost 25 deaths!"+White)
              deaths-=25
            elif abc == 3:
              print(Green+"You got 3 chances!"+White)
              chance+=3
            elif abc == 4:
              print(Green+"You lost 4 chances!"+White)
              chance-=4
            elif abc == 5:
              print(Green+"You lost 2 bonus"+White)
              bonus-=2
            elif abc == 6:
              print(Green+"You lost 10 deaths!"+White)
              deaths-=10
            else:
              print(Green+"You got 6 bonus!"+White)
              bonus+=6
          else:
            print(Red+"You don't have enough deaths and chances!"+White)
          next()
    else:
      print(Red+'Invalid DEATH Command!'+White)
      next()

#im already done. literally.