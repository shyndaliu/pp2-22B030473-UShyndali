import random

def game():
    x=random.randint(1,20)
    print("helloo! what's yo name?")
    name=str(input())
    cnt=0
    print("Well, {}, i am thinking about some number between 1-20".format(name))
    while True:
        print("Take a guess!")
        y=int(input())
        cnt+=1
        if y==x:
            print("congrats!! you won in {} guesses".format(cnt))
            break
        elif y<x:
            print("too loow")
        else:
            print("too high")
game()