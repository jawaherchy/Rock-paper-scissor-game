import random
def gamewin(comp,you):
    if comp==you:
        return None
    elif comp=='r':
        if you=='s':
            return False
        elif you=='p':
            return True
    elif comp=='p':
        if you=='r':
            return False
        elif you=='s':
            return True
    elif comp=='s':
        if you=='p':
            return False
        elif you=='r':
            return True

print("computer turn:rock(r),paper(p),scissors(s)")
randno=random.randint(1,3)

if randno==1:
    comp='s'
elif randno==2:
    comp='r'
elif randno==3:
    comp='p'
you=input("your turn:rock(r),paper(p),scissors(s)")

a=gamewin(comp,you)
print(f"you choose {you}")
print(f"comp choose {comp}")
if a==None:
    print("the game is tie!")
elif a:
    print("you win")
else:
    print("you lose!")