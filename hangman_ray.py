import random


data=["peach","orange","history","math","United","Dubai","Science",'SST',"CHemistRY",
                                                                         "physics",
      'result','texas','nevada','cali','LA','boston','newyork','lasvegas','berlin',
      'tokyo','kyoto','osaka','sapporo','bein','furrano','asakusa','otaru','seoul'
      ,'busan','gangnam','london','france','switzerland','italy','vatican city',
      'georgia','austria','hungary','denmark','sweden','thailand','malaysia','singapore'
                                                                             ,'australia',
      'melbourne','brisbane','gold coast','sydney']





lives=6
word=[]
choice=''


print("WELCOME TO HANGMAN BY RAY!!!")
def letter(alpha):
    global letters
    global choice
    global word
    choice = random.choice(alpha).lower()

    word = ["_" for var in choice if var != ""]
    with open("words.txt", "w") as file:
        file.write(f"{''.join(word)}")


def play_is_onn():
    global lives
    global choice
    
    global data
    with open("words.txt") as file:
        word=list(file.read())

    


    if word == list(choice):

        print(f"{''.join(word).upper()} WAS THE WORD \nTHANK YOU PLAYING,TO PLAY ENTER THE CODE\n\n\n")
        exit()

    elif word != list(choice):

        print(f"\n\n****************************{lives}/6 LIVES LEFT****************************")
        inp = input(f"PLS GUESS A LETTER:\n"
                    f"YOUR WORD IS {word} ").lower()


        if inp.lower() in list(choice):
            for itr in range(len(list(choice))):
                if inp== list(choice)[itr]:
                    word.pop(itr)
                    word.insert(itr, inp)
                else:
                    pass

            with open("words.txt","w") as file:
                file.write(f"{''.join(word)}")

        elif inp.lower() not in list(choice):
                        lives -= 1

        else:
                        print("TRY TO GUESS AN ALPHABET PLEASE!!!!")
    else:
        pass

letter(alpha=data)
while lives>0:
    play_is_onn()
else:
    print(f"\n\n\nOH NO YOU LOST!!!\n"
          f"YOUR WORD WAS {choice}\n"
          "PLS RUN THE CODE AGAIN TO PLAY.")
    exit()