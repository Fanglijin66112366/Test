import pygame
import tkinter 

scores = 0

print("北方")
print("1.ทิศเหนือ")
print("2.หนังสือ")
print("3.การบ้าน")
print("4.กระดาษ")
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
print("着急")
print("1.ดูทีวี")
print("2.กังวล")
print("3.ดูหนัง")
print("4.อารมดี")
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
print("游戏")
print("1.เกม")
print("2.หมอน")
print("3.ครู")
print("4.ทีวี")
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
print("作业")
print("1.ทำงานบ้าน")
print("2.ทำงาน")
print("3.อาหาร")
print("4.การบ้าน")
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
print("楼")
print("1.บรรได")
print("2.ตัด")
print("3.อาคาร")
print("4.ช้าง")
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
print("办公室")
print("1.วัด")
print("2.ออฟฟิต")
print("3.โรงอาหาร")
print("4.โรงแรม")
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
print("裤子")
print("1.กางเกง")
print("2.ถุงเท้า")
print("3.ลองเท้า")
print("4.กระโปรง")
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
print("比赛")
print("1.แข่งขัน")
print("2.ทำงาน")
print("3.ดูหนัง")
print("4.ฟังเพลง")
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

root=tkinter.Tk
label=tkinter.Label(root,open)
root.mainloop() 

pygame.display.update()       
pygame.quit()
quit()
