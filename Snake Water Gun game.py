import random

def gameWin(comp,you):
    if comp==you:
        return None

    elif comp=='s':
     if you=='w':
        return False
    elif you=='g':
         return True

    elif comp=='g':
     if you=='s':
         return False
     elif you=='w':
         return True

    elif comp=='w':
     if you=='g':
         return False
     elif you=='s':
        return True                     



print("Comp's Turn: Snake(s) Water(w) or Gun(g)?")
randNO=random.randint(1,3)
print(randNO)

if randNO==1:
   comp='s'
elif randNO==2:
   comp='w'
elif randNO==3:
   comp='g'

you=input("Your Turn: Snake(s) Water(w) or Gun(g)?")

a=gameWin(comp,you)
print(f"Computer chose {comp}")
print(f"You chose {you}")

if a==None:
    print("The game is a tie!")
elif a:
    print("You win")
else:
    print("You Lose")