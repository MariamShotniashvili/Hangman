from random import randint # Do not delete this line

def displayIntro():
    print(
        """"_______________________________________________
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
_______________________________________________
_____________________Rules_____________________
Try to guess the hidden word one letter at a   
time. The number of dashes are equivalent to   
the number of letters in the word. If a player 
suggests a letter that occurs in the word,     
blank places containing this character will be 
filled with that letter. If the word does not  
contain the suggested letter, one new element  
of a hangman’s gallow is painted. As the game  
progresses, a segment of a victim is added for 
every suggested letter not in the word. Goal is
to guess the word before the man hangs!        
_______________________________________________"""
    )

def displayEnd(result):
    if result == True:
        print("""________________________________________________________________________
          _                                  _                          
         (_)                                (_)                         
__      ___ _ __  _ __   ___ _ __  __      ___ _ __  _ __   ___ _ __    
\ \ /\ / / | '_ \| '_ \ / _ \ '__| \ \ /\ / / | '_ \| '_ \ / _ \ '__|   
 \ V  V /| | | | | | | |  __/ |     \ V  V /| | | | | | | |  __/ |      
  \_/\_/ |_|_| |_|_| |_|\___|_|      \_/\_/ |_|_| |_|_| |_|\___|_|      
           | |   (_)    | |                  | (_)                      
        ___| |__  _  ___| | _____ _ __     __| |_ _ __  _ __   ___ _ __ 
       / __| '_ \| |/ __| |/ / _ \ '_ \   / _` | | '_ \| '_ \ / _ \ '__|
      | (__| | | | | (__|   <  __/ | | | | (_| | | | | | | | |  __/ |   
       \___|_| |_|_|\___|_|\_\___|_| |_|  \__,_|_|_| |_|_| |_|\___|_|   
________________________________________________________________________""")

    else:
        print(""" __     __           _           _   _                                    
 \ \   / /          | |         | | | |                                   
  \ \_/ /__  _   _  | | ___  ___| |_| |                                   
   \   / _ \| | | | | |/ _ \/ __| __| |                                   
    | | (_) | |_| | | | (_) \__ \ |_|_|                                   
    |_|\___/ \__,_| |_|\___/|___/\__(_)                                   
        _______ _                                        _ _          _ _ 
       |__   __| |                                      | (_)        | | |
          | |  | |__   ___   _ __ ___   __ _ _ __     __| |_  ___  __| | |
          | |  | '_ \ / _ \ | '_ ` _ \ / _` | '_ \   / _` | |/ _ \/ _` | |
          | |  | | | |  __/ | | | | | | (_| | | | | | (_| | |  __/ (_| |_|
          |_|  |_| |_|\___| |_| |_| |_|\__,_|_| |_|  \__,_|_|\___|\__,_(_)
__________________________________________________________________________""")
            
def displayHangman(state):
    if state == 5:
        print("""     ._______.   
     |/          
     |           
     |           
     |           
     |           
     |           
 ____|___  """)

    elif state == 4:
        print("""     ._______.   
     |/      |   
     |           
     |           
     |           
     |           
     |           
 ____|___ """)

    elif state == 3:
        print("""     ._______.   
     |/      |   
     |      (_)  
     |           
     |           
     |           
     |           
 ____|___        """)

    elif state == 2:
        print("""     ._______.   
     |/      |   
     |      (_)  
     |       |   
     |       |   
     |           
     |           
 ____|___        """)

    elif state == 1:
        print("""     ._______.   
     |/      |   
     |      (_)  
     |      \|/  
     |       |   
     |           
     |           
 ____|___        """)

    elif state == 0:
        print("""     ._______.   
     |/      |   
     |      (_)  
     |      \|/  
     |       |   
     |      / \  
     |           
 ____|___        """)


def getWord():
    listOfWords = []
    file = open("hangman-words.txt", "r")
    for i in file.readlines():
        listOfWords.append(i)
    file.close()
    chosenWord = listOfWords[randint(0, len(listOfWords))]
    return chosenWord

def valid(c):
    if c.islower() and len(c) == 1:
        return True
    else:
        return False


def play():
    word = getWord()
    hiddenWord = '_' * (len(word) - 1)
    lives = 5
    while True:
        displayHangman(lives)
        print("Guess the word: " + hiddenWord)
        while True:
            inputLetter = input("Enter the letter: ")
            if valid(inputLetter) == False:
                print("Invalid Input. Please enter single lowercase letter")
            else:
                break
        if word.find(inputLetter) != -1:
            for i in range(0, len(word)):
                if word[i] == inputLetter:
                    hiddenWord = hiddenWord[:i] + inputLetter + hiddenWord[i+1:]
        else:
            lives = lives -1

        if lives == 0:
            displayHangman(lives)
            print("Hidden word was: " + word)
            break

        if hiddenWord == word[:len(word) - 1]:
            print("Hidden word was: " + word)
            return True

def hangman():
    while True:
        displayIntro()
        result = play()
        displayEnd(result)
        askPlayer = input("Do you want to play again? (yes/no)")
        if askPlayer == "no":
            break

if __name__ == "__main__":
    hangman()


