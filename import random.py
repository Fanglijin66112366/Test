import pygame
import sys

pygame.init()
width, pygame.freetype.height = 800,600
clock = pygame.time.Clock()
wite = (255,255,255)
start_time = pygame.time.get_ticks()

scores = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    elapsed_time = pygame.time.get_ticks() - start_time

print("e_g")
print("1.g")
print("2.c")
print("3.z")
print("4.k")
clock.tick(15)
x = int(input("answer :")) 
clock.tick
if x == 1 :
    scores += 1
    print(scores)
else : 
    scores -= 1
    print(scores) 
    if x > 4 :
        scores-=1
    print(scores)    
print("__________________________________________________________________________")
print("c_y")
print("1.o")
print("2.r")
print("3.z")
print("4.i")
clock.tick(10)
x = int(input("answer :"))
if x == 2 :
    scores += 1
    print(scores)
else : 
    scores -= 1
    print(scores)
    if x > 4 :
        scores-=1
        print(scores)    
print("__________________________________________________________________________")
print("no_e")
print("1.t")
print("2.c")
print("3.j")
print("4.c")
clock.tick(10)
x = int(input("answer :"))
if x == 1 :
    scores += 1
    print(scores)
else : 
    scores -= 1
    print(scores)
    if x > 4 :
        scores-=1    
print("__________________________________________________________________________")
print("bea_")
print("1.g")
print("2.x")
print("3.z")
print("4.n")
clock.tick(10)
x = int(input("answer :"))
if x == 4 :
    scores += 1
    print(scores)
else : 
    scores -= 1
    print(scores)
    if x > 4 :
        scores-=1
        print(scores)    
print("__________________________________________________________________________")
print("be_r")
print("1.d")
print("2.c")
print("3.e")
print("4.b")
clock.tick(10)
x = int(input("answer :"))
if x == 3 :
    scores += 1
    print(scores)
else : 
    scores -= 1
    print(scores)
    if x > 4 :
        scores-=1
        print(scores)    
print("__________________________________________________________________________")
print("att__k")
print("1.io")
print("2.uh")
print("3.ac")
print("4.io")
clock.tick(10)
x = int(input("answer :"))
if x == 3 :
    scores += 1
    print(scores)
else : 
    scores -= 1
    print(scores)
    if x > 4 :
        scores-=1
        print(scores)    
print("__________________________________________________________________________")
print("a_o")
print("1.g")
print("2.c")
print("3.v")
print("4.q")
clock.tick(10)
x = int(input("answer :"))
if x == 1 :
    scores += 1
    print(scores)
else : 
    scores -= 1
    print(scores)
    if x > 4 :
        scores-=1
        print(scores)    
print("__________________________________________________________________________")
print("ba_d")
print("1.n")
print("2.d")
print("3.e")
print("4.p")
clock.tick(10)
x = int(input("answer :"))
if x == 1 :
    scores += 1
    print(scores)
else : 
    scores -= 1
    print(scores)
    if x > 4 :
        scores-=1
        print(scores)    
print("__________________________________________________________________________")
print ("scores",scores)
