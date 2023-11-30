import random
import os, sys
import pygame
import time
from pygame.locals import *
pygame.init()
pygame.display.set_caption('BTC clicker')
img = pygame.image.load('bitcoin.png')
button = pygame.image.load('button.png')
button = pygame.transform.scale(button, (250, 100))
w = 800
h = 600
grey = (112,128,144)
greyer = pygame.image.load('maxresdefault.jpg')
greyer = pygame.transform.scale(greyer, (w, 100))
screen = pygame.display.set_mode((w, h))
print("\n"*50)
print("""
Hello Welcome to Bitcoin Clicker.
You play by clicking the Bitcoin and then betting your BTC on a coinflip by clicking "Play Now".
""")
bank = 0
font = pygame.font.Font(None,50)
while True:
  screen.fill((grey))
  screen.blit(greyer,(0, 220))
  screen.blit(img,(-40,0))
  screen.blit(button,(525,340))
  pygame.display.flip()
  value = "You have:"+str(bank)+"BTC"
  textsurface = font.render(value, True, (255,255,255))
  screen.blit(textsurface,(500,240))
  pygame.display.update() 
  for e in pygame.event.get():
    listm = ("heads", "tails")
    num2 = random.choice(listm)
    if e.type == pygame.MOUSEBUTTONDOWN:
      mx, ms = pygame.mouse.get_pos()
      if ms > 37 and ms < 500 and mx > 13 and mx < 464:
        bank += 1
      if ms > 342 and ms < 430 and mx > 527 and mx < 770:
        ui=int(input("\t How much BTC would you like to Bet?:"))
        inp = input("\t heads or tails?")
        if ui > bank:
          print("you do not have enough BTC!")
        elif ui <= bank:
          if inp == num2:
            bank = bank + ui
            print("You got", num2,"! you earned:", ui, "BTC")
          elif inp != num2:
            bank = bank - ui
            print("You got", num2,"! you lost:", ui, "BTC")
        else:
            print("Invalid transaction.")

