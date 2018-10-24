#Homework 6 Strings
#'Wheel of Fortune' the Game
## Admittedly, when you said that I could make the actual game...
## this did not end up being the simple project I had in mind...
## (Actual homework assignment is at the bottom!)
## (This code is kind of a mess but I ran out of steam to clean it up...)
import time
import random
import textwrap

#phrases to be randomly generated
phraseList = ['Wait and See', 'The End Justifies the Means', "The Apple Doesn't Fall Far From the Tree",  \
          'Talk is Cheap', "Rome Wasn't Built in a Day", 'Revenge Is a Dish Best Served Cold', \
          'Pride Goes Before a Fall', 'Only Fools and Horses Work', 'Once Bitten Twice Shy', \
          'No News is Good News', 'No Man is an Island', 'Misery Loves Company', 'Might Is Right', \
          'Less is More', "It's Never Too Late", 'Ignorance is Bliss', 'A Dime A Dozen', \
          'Hunger is the Best Sauce', 'Haste Makes Waste', 'Good Things Come to Those Who Wait', \
          'Good Things Come in Threes', 'Curiosity Killed the Cat', 'Clothes Make the Man', \
          'Blood is Thicker Than Water', 'Better Late Than Never', 'Bad News Travels Fast',  \
          'A Problem Shared is a Problem Halved', 'A Picture is Worth a Thousand Words',  \
          'A Penny Saved Is a Penny Earned', 'A New Broom Sweeps Clean', "It Takes Two to Tango",  \
          'A Friend in Need is a Friend Indeed', 'A Fool and His Money Are Soon Parted',  \
          'A Bird in the Hand is Worth Two in the Bush', 'A Fish Out Of Water']

noneLetters  = [] #list that will hold letters that are guessed but have no occurences

#intro
def intro():
    print('             Welcome to...')
    time.sleep(1)
    print()
    print('                 WHEEL')
    time.sleep(1)
    print('                  OF')
    time.sleep(1)
    print('                FORTUNE')
    time.sleep(2)
    print()

#blank phrase to be filled as players guess letters
def displayPhrase():

    index = random.randrange(0,len(phraseList))
    phrase = phraseList[index]
    phrase = phrase.lower()
    print()
    print("That's the spirit!")
    time.sleep(1)
    print()
    print("Here is your puzzle...")
    time.sleep(2)
    print()
    print()
    print('Guess The Phrase:')
    print()
    guessPhrase = []
    for letter in phrase:
        if(letter == ' '):
            guessPhrase.append(" ")
        elif(letter == "'"):
            guessPhrase.append("'")
        else:
            guessPhrase.append("_")
    guessString = ' '.join(guessPhrase)
    print(textwrap.fill(guessString,65))
    print()
    print()
    return phrase

#copy of blank phrase that can be edited
def unfilledPhrase():
    guessPhrase = []
    for letter in correctPhrase:
        if(letter == ' '):
            guessPhrase.append(" ")
        elif(letter == "'"):
            guessPhrase.append("'")
        else:
            guessPhrase.append("_")
    guessString = ''.join(guessPhrase)
    return guessString

#partially filled phrase as letters are guessed
def filledPhrase(guess):
    for letter in lessGuesses:
        if(letter == guess):
            index = lessGuesses.index(guess)
            lessGuesses[index] = ' '
            guess = guess.strip()
            lessBlanks[index] = guess
            guessPhrase[index] = guess

#function to simulate the money wheel
def spinWheel():
    wheelList = [300, 500, 'bankrupt', 5000, 500, 900, 700, 300, 800, 550, 400, 500, 600, 350, 500, 900, 'bankrupt', \
                 650, 700, 800, 450, 500, 300]
    print('Spinning the wheel...')
    time.sleep(2)
    print('Spinning...')
    time.sleep(2)
    spin = random.randrange(0, len(wheelList))
    try:
        money = int(wheelList[spin])
        print("Your spin landed on: " + '$' + str(wheelList[spin]) + '!')
        print()
        return money
    except:
        money = wheelList[spin]
        print(str(wheelList[spin]) + '!')
        print()
        time.sleep(2)
        bankrupt = -1
        print()
        return bankrupt
    
#function to pass in a consonant and see if it is in the phrase
def guess(consonant):
    count = correctPhrase.count(consonant)
    print()
    if (count == 1):
        print('There is 1 ' + consonant)
        filledPhrase(consonant)
    elif (count > 1):
        print('There are ' + str(count) + ' of the letter ' + consonant)
        filledPhrase(consonant)
    else:
        print('There are no ' + consonant +"'s")
        noneLetters.append(consonant)
    guessString = ' '.join(lessBlanks)
    print()
    print(textwrap.fill(guessString,65))
    print()
    return count

#function to pass in a vowel and see if it is in the phrase
def buyVowel(vowel):
    vCount = correctPhrase.count(vowel)
    if (vCount == 1):
        print('There is 1 ' + vowel)
        purchase = 250
        filledPhrase(vowel)

    elif (vCount > 1):
        print('There are ' + str(vCount) + ' of the vowel ' + vowel)
        purchase = 250
        filledPhrase(vowel)
    else:
        print('There are no ' + vowel +"'s")
        noneLetters.append(vowel)
        purchase = 0
    guessString = ' '.join(lessBlanks)
    print()
    print(textwrap.fill(guessString,65))
    print()
    return purchase

#function to introduce the AI competitor
def nameAI():
    nameList = ['Bobby B. Boy', 'Billy Bluejeans', 'Marsha', 'Ethel', 'Ugly Sal', 'Big Money', \
                'Scary Susan', 'Simple Dan', 'Handsome Harvey', 'Timmy', 'Homeless Harriet']
    tauntList = [', preprare to get got.', " and you're going down!", ' and I will dance on your grave.', \
                 " and if I lose I will manifest myself in the physical world to exact my revenge.", \
                 ' and it is so lovely to be here.', ', you killed my father, prepare to... lose.', \
                  ', good luck and have fun!', ' and I will resort to violence if necessary.', ", let's do this!", \
                 ', I like big bucks and I can not lie!', ', how much code do I need before my AI resembles consciousness?']
    rName = random.randrange(0, len(nameList))
    rTaunt = random.randrange(0,len(tauntList))
    name = nameList[rName]
    taunt = tauntList[rTaunt]

    print("Let's meet your AI competitor!")
    time.sleep(2)
    print()
    lineAI = 'AI: Hello my name is ' + name + taunt
    print(textwrap.fill(lineAI, 65))
    time.sleep(4)
    return name

#function for beginning of AI turn
def turnAI():
    tauntList = ['OK my turn now.', "Let's see if I can do better", 'Hmmm interesting...', 'Aha! I know what to do', \
                 'Oof..', 'Hmph...', 'Yikes...', 'Heh, nice one.', "I'm secretly cheating you know"]
    rTaunt = random.randrange(0,len(tauntList))
    taunt = tauntList[rTaunt]
    time.sleep(2)
    print('AI: ' + taunt)
    print()
    time.sleep(2)

#function for AI to choose whether to guess letters, vowels, or solve the puzzle
def chooseAI(wheelAI):
    consonants = 'bcdfghjklmnpqrstvwxyz'
    cPriority = 'trnslh' 
    cNext = 'gdmfbywc'
    cLast ='vjkzptrnslh'    
    vowels = 'aeiou'
    pPriority = cPriority + vowels
    pNext = cNext + vowels
    bCount = lessBlanks.count('_')
    lengthCheck = len(correctPhrase) - bCount
    percentageCheck = (lengthCheck/(len(correctPhrase))) * 100
    percentageCheck = int(percentageCheck)
    guessAI = 0
    
   #take out guessed letters from the pool           
    for letter in guessedLetters:
        if letter in consonants:
            consonants = consonants.replace(letter, '')
            consonants = consonants.strip()
        if letter in cPriority:
            cPriority = cPriority.replace(letter, '')
            cPriority = cPriority.strip()
        if letter in cNext:
            cNext = cNext.replace(letter,'')
            cNext = cNext.strip()
        if letter in cLast:
            cLast = cLast.replace(letter,'')
            cLast = cLast.strip()                      
        if letter in vowels:
            vowels = vowels.replace(letter, '')
            vowels = vowels.strip()
            
    if(wheelAI >= 0): #if not bankrupt from wheel spin
        if(percentageCheck > 70): #solve if 70% complete
           guessAI = solveAI()

        elif(percentageCheck <= 40): #if less than 40% is solved, guess more letters
            try:
                if(len(cPriority) > 0 ):
                    guessC = random.randrange(0, len(cPriority))
                    guessAI = cPriority[guessC]
                    guessedLetters.append(guessAI)
                    if(guessAI == 'n' or guessAI == 's' or guessAI == 'l' or guessAI == 'h' or guessAI == 'x' \
                    or guessAI == 'f' or guessAI == 'm' or guessAI == 'r'):
                        print('AI: Is there an...')
                    else:
                        print('AI: Is there a...')
                    time.sleep(1)
                    print(guessAI + '?')
                    time.sleep(2)
            except:
                if(totalAI > 250):
                    vowels = vowels.strip()
                    guessV = random.randrange(0, len(vowels))
                    guessAI = vowels[guessV]
                    guessedLetters.append(guessAI)
                    print("AI: I'd like to buy a vowel...")
                    time.sleep(2)
                    if(guessAI == 'u'):
                        print('AI: Is there a...')
                    else:
                        print('AI: Is there an...')
                    time.sleep(1)
                    print(guessAI + '?')
                    time.sleep(2)        
                else:
                    guessAI = solveAI()

        elif(percentageCheck <= 60): #if less than 60%, randomly guess next priority letters
            randomN = random.randrange(0, 101) #generates random element
            if(randomN > 0 and randomN < 40):
                guessC = random.randrange(0, len(cNext))
                guessAI = cNext[guessC]
                if(guessAI == 'n' or guessAI == 's' or guessAI == 'l' or guessAI == 'h' or guessAI == 'x' \
                    or guessAI == 'f' or guessAI == 'm' or guessAI == 'r'):
                    print('AI: Is there an...')
                else:
                    print('AI: Is there a...')                
            elif(randomN > 40 and randomN < 70  and totalAI > 250):
                vowels = vowels.strip()
                guessV = random.randrange(0, len(vowels))
                guessAI = vowels[guessV]
                guessedLetters.append(guessAI)
                print("AI: I'd like to buy a vowel...")
                time.sleep(2)
                if(guessAI == 'u'):
                    print('AI: Is there a...')
                else:
                    print('AI: Is there an...')
                time.sleep(1)
                print(guessAI + '?')
                time.sleep(2)

            elif(randomN > 70 and randomN < 85 or totalAI < 250):
                guessC = random.randrange(0, len(cLast))
                guessAI = cLast[guessC]
                guessedLetters.append(guessAI)
                if(guessAI == 'n' or guessAI == 's' or guessAI == 'l' or guessAI == 'h' or guessAI == 'x' \
                   or guessAI == 'f' or guessAI == 'm' or guessAI == 'r'):
                    print('AI: Is there an...')
                else:
                    print('AI: Is there a...')
                time.sleep(1)
                print(guessAI + '?')
                time.sleep(2)
            else:
                guessAI = solveAI()
        else:
                guessAI = solveAI()
        
        return guessAI

        
    
    else: #bankrupt
        print("AI: Noooo!")
        print()
        guessAI = -1
        return guessAI

#function for AI to solve the puzzle by comparing it to a database of given words
def solveAI():
    time.sleep(2)
    print("AI: I'd like to solve the puzzle...")
    time.sleep(2)    
    extraList = ['prude', 'crude', 'bride', 'grade', 'toes','ties','lies','fees','bees','dyes','doll','fill','tall','mall','mill' \
                 , 'moons', 'tray','tools','food','rat','fat','fork','dare','lives','last','lost','best','mist',\
                 'dust','fate','past','sad','dad','bed','fed','lad','mad','pens','fans','cats','dogs','hens', \
                 'pans','rats', 'band','sand','word','head','hood','bead','seed','boat','button','soot','hand', \
                 'class', 'grass','chess','glass',]

    for word in extraList:
        phraseList.append(word)
    random.shuffle(phraseList)

    randomizePhrase = guessPhrase
    letterPool = 'abcdefghijklmnopqrstuvwxyz'
    guessPool = []
    wordPool = []
    temp = wordPool
    flag = 0
    guessAI = 0

    for letter in letterPool:
        if letter in guessedLetters:
            letterPool = letterPool.replace(letter, '')
            letterPool = letterPool.strip()

    #break phrase list into array of words
    for phrase in phraseList:
        w = phrase.split()
        for word in w:
            word = word.lower()
            wordPool.append(word)

    #break guess into array of words
    w =''.join(randomizePhrase)
    w = w.split()
    for word in w:
        guessPool.append(word)

    for guessWord in guessPool: #for each guess word
        random.shuffle(temp)
        for actualWord in temp: #compare to words in wordPool
            flag = 0
            index = 0
            if((len(guessWord)) == (len(actualWord))): #if same length
                for letter in guessWord: #compare each character in guess word to actual word
                    if (guessWord[index] == '_'): #skip blank characters
                        index = index + 1
                        continue
                    elif (guessWord[index] == actualWord[index]): #skip characters that have same position
                        index = index + 1
                        continue
                    else:
                        flag = flag+1 #flag if characters don't have same position
                    index = index + 1
                    for letter in actualWord:
                        if letter in noneLetters: #flag if already guessed characters had no occurences
                            flag = flag + 1
                        

                try:
                    if(flag == 0): #if not flagged, use as guess
                        replaceIndex = guessPool.index(guessWord) #____ indexed here (guessWord)
                        guessPool[replaceIndex] = actualWord #replaced here with actualWord
                        break
            
                except:
                    continue

        temp = wordPool                           
    solvePuzzle = ' '.join(guessPool)                                                            
    print(solvePuzzle + '?')
    time.sleep(1)
    if(solvePuzzle == correctPhrase):
          print()
          print(AI + ' Wins!!!')
          print()
          time.sleep(1)
          print('AI: Victory tastes so sweet.')
          guessAI = 999
          return guessAI
          
    else:
        
        print()
        print('Not quite, try again...')
        wordString =  ''.join(lessBlanks)
        wordList = wordString.split()
        guessPool = []
        w =''.join(randomizePhrase)
        w = w.split()
        for word in w:
            guessPool.append(word)        
        return guessAI
    

def score(multiplier, wheelspin, total, vowel):
    total = total + (multiplier * wheelspin) - vowel
    return total
       

#Main Code
intro()
AI = nameAI()
correctPhrase = displayPhrase()
unfilledPhrase = unfilledPhrase()
lessGuesses =  list(correctPhrase)
lessBlanks =  list(unfilledPhrase)
guessPhrase = list(unfilledPhrase)
totalMoney = 0
totalAI = 0
guessedLetters = []
consonants = 'bcdfghjklmnpqrstvwxyz'
vowels = 'aeiou'
newTurn = True
guessAI = 0

while True:
    print()
    print()
    time.sleep(1)
    
    #AI win condition
    if(guessAI == 999):
        time.sleep(1)
        print()
        print(AI + "'s " + 'winnings are ' + '$' + str(totalMoney))
        print()
        newTurn = False
        break
    
    #Player turn
    if(newTurn == True):
        spin = input('Your turn. Press enter to spin the wheel')
        if(spin == ''):
            turnMoney = spinWheel()
            newTurn = False
        else:
            print("Whoops, you missed the wheel. Try again")
            continue
    else:

        #Player options
        if( turnMoney >= 0):
            print('Solve Puzzle [$]')
            print('Exit [*]')
            print('Current Score: $' + str(totalMoney))
            print('Current Guesses: ' + ' '.join(guessedLetters))            
            userInput = input('Enter a letter: ')
            try:
                userInput = userInput.lower()
            except:
                print("Not a letter, try again.")
                continue                                                  
            if userInput == '' or userInput == ' ' or len(userInput) > 1:
                print("Not a letter, try again.")
                continue

            if userInput in guessedLetters:
                print('That letter was already guessed.')
                continue

            #user guesses  consonant
            if userInput in consonants:               
                guessedLetters.append(userInput)
                userMultiplier = guess(userInput)                
                totalMoney = score(userMultiplier, turnMoney, totalMoney, 0)
                print('Current Score: $' + str(totalMoney))
                print('AI Score: $' + str(totalAI))
                print()
                

            #AI turn
                print()
                print(AI + "'s turn.")                
                turnAI()
                wheelAI = spinWheel()
                guessAI = chooseAI(wheelAI)                
                try:
                    if guessAI in consonants:
                        multiplierAI = guess(guessAI)
                        totalAI = score(multiplierAI, wheelAI, totalAI, 0)
                    else:
                        vowelAI = guess(guessAI)
                        totalAI = score(0, wheelAI, totalAI, 250)
                        
                    print('AI Score: $' + str(totalAI))
                except:
                    totalAI = 0
                newTurn = True

            #user guesses vowel
            elif userInput in vowels:                
                if(totalMoney < 250):
                    print("You can't afford a vowel...")
                    continue
                else:                    
                    guessedLetters.append(userInput)
                    vowelMoney = buyVowel(userInput)
                    totalMoney = score(0, turnMoney, totalMoney, vowelMoney)
                    print('Current Score: $' + str(totalMoney))
                    print('AI Score: $' + str(totalAI))
                    print()
                    
            #AI turn
                print()
                print(AI + "'s turn.")
                turnAI()
                wheelAI = spinWheel()
                guessAI = chooseAI(wheelAI)                
                try:
                    if guessAI in consonants:
                        multiplierAI = guess(guessAI)
                        totalAI = score(multiplierAI, wheelAI, totalAI, 0)
                    else:
                        vowelAI = guess(guessAI)
                        totalAI = score(0, wheelAI, totalAI, 250)
                        
                    print('AI Score: $' + str(totalAI))
                except:
                    totalAI = 0
                newTurn = True
                
            #user guesses phrase      
            elif(userInput == '$'):
                userGuess = input('Guess the phrase: ')
                if(userGuess == correctPhrase):
                    print('Correct! You win!')
                    time.sleep(2)
                    print('AI: Drat, foiled again.')
                    time.sleep(1)
                    print()
                    print('Your winnings are ' + '$' + str(totalMoney))
                    print()
                    print("AI: Too bad the money is just imaginary...")
                    break
                else:
                    print(userGuess)
                    print(correctPhrase)
                    print()
                    print('Not quite, try again...')
                
            #AI turn
                print()
                print()
                print('AI Score: $' + str(totalAI))
                print()    
                print(AI + "'s turn.")                   
                turnAI()
                wheelAI = spinWheel()
                guessAI = chooseAI(wheelAI)                
                try:
                    if guessAI in consonants:
                        multiplierAI = guess(guessAI)
                        totalAI = score(multiplierAI, wheelAI, totalAI, 0)
                    else:
                        vowelAI = guess(guessAI)
                        totalAI = score(0, wheelAI, totalAI, 250)
                        
                    print('AI Score: $' + str(totalAI))
                except:
                    totalAI = 0
                newTurn = True

            elif(int(guessAI) == -1):
                newTurn = True

            #user quits            
            elif(userInput == '*'):
                print()
                print("The phrase was: " + correctPhrase)
                print()
                break

            #user inputs incorrect key
            else:
                print("That's not an option. Try again")
                continue
            newTurn = False

        #bankrupt
        else:
            totalMoney = 0
            print('Current Score: $' + str(totalMoney))
            print('AI Score: $' + str(totalAI))
            print()
            time.sleep(1)

            
            #AI turn
            print()
            print(AI + "'s turn.")
            print('AI Score: $' + str(totalAI))
            turnAI()
            wheelAI = spinWheel()
            guessAI = chooseAI(wheelAI)                
            try:
                if guessAI in consonants:
                    multiplierAI = guess(guessAI)
                    totalAI = score(multiplierAI, wheelAI, totalAI, 0)
                else:
                    vowelAI = guess(guessAI)
                    totalAI = score(0, wheelAI, totalAI, 250)
                    
                print('AI Score: $' + str(totalAI))
            except:
                totalAI = 0
            newTurn = True
            
    
print('Thanks for playing.')




#actual homework 6 code
#userInput = input('Please enter a phrase: ')
#userInput = userInput.lower()
#userInput = userInput.strip()
#alphabet = 'abcdefghijklmnopqrstuvwxyz'

#unusedLetterList = []

#for letter in alphabet:  
#    count = userInput.count(letter)
#    if (count == 1):
#        print('There is only 1 ' + letter)
#        continue
#    elif (count > 1):
#        print('There are ' + str(count) + ' of the letter ' + letter)
#
#    else:
#         unusedLetterList.append(letter)
#unusedString = ', '.join(unusedLetterList)         
#print('There are no occurences of: ' + unusedString)
