import random
def choose():
    words=['Rainbow','Mathematics','Danger','Reverse','Water','Important','Board']
    pick=random.choice(words)
    return pick
def jumble(picked_word):
    jumble="".join(random.sample(picked_word,len(picked_word)))
    return jumble
def thank(player1,player2,pp1,pp2):
    print(player1,"Your score: ",pp1)
    print(player2,"Your score: ",pp2)
    if pp1>pp2:
        print(player1,"You won !!!")
    else:
        print(player2,"You Won !!!")
    print("Thanks for playing.Have a nice day")
    

def play():
    player1=input("Player 1,enter your name: " )
    player2=input("Player 2,enter your name: ")
    pp1=0
    pp2=0
    turn=0
    while(1):
        picked_word=choose()               #comuter's task
        qn=jumble(picked_word)             
        print("The Question is:",qn)
        if turn%2==0:
            print(player1," its your turn now")
            ans=input("What's in my mind? ")
            if ans==picked_word:
                pp1=pp1+1
                print("Your score is: ",pp1)
            else:
                print("Oh no! I thought the word is",picked_word)
            c=int(input("Choose 1 to continue or 0 to exit."))
            if c==0:
                thank(player1,player2,pp1,pp2)
                break
            #player2
        else:
            print(player2," its your turn now")
            ans=input("What's in my mind? ")
            if ans==picked_word:
                pp2=pp2+1
                print("Your score is: ",pp2)
            else:
                print("Oh no! I thought the word is",picked_word)
            c=int(input("Choose 1 to continue or 0 to exit."))
            if c==0:
                thank(player1,player2,pp1,pp2)
                break
        turn=turn+1
play()
                
    
        

