import random
from Hangman_art import stages, logo
from HANGMAN_WORD import word_list
from replit import clear

word = random.choice(word_list).lower()
blank = []
lives = len(stages)-1
# print(word+"\n")
print(logo)

for i in range(0,len(word)):
  blank.append('_')
print(f"{' '.join(blank)}")

eog = False #end of game
while not eog:
  guess = input("\nGuess a letter:\n").lower()
  clear()

  if guess in blank:
    print(f"you already guessed {guess}")
  
  for i in range(len(word)):
    if guess == word[i]:
      blank[i] = guess
      


  if guess not in word:
    lives -= 1
    print(f"you guessed {guess}, that's not in the word. you lose a life\n")
    if lives == 0:
      eog = True
      print('you lose.')
      print(f"The correct answer is {word}")
    

  if '_' not in blank:
    eog = True
    print("\nyou won")
  print(stages[lives])    
  print(f"{' '.join(blank)}")
