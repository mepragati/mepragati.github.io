import os
import random
import hangman_art
import hangman_words

print(hangman_art.logo)
end_of_game = False
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.
lives=6

#Testing code
print(f"The Chosen Word is: {chosen_word}.")

#TODO-2: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
display=[]
for i in range(len(chosen_word)):
  display+="_"
print(display)

#TODO-3: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

#TODO-4: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    os.system("cls")
    print(hangman_art.logo)
    #TODO-5: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"You've already guessed '{guess}'.")
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess :
          display[position] = letter

    #TODO-6: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."
    if guess not in chosen_word:
      #TODO-7: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
      print(f"You guessed '{guess}', that's not in the word. You lose a life.")
          
      lives-=1
      if lives == 0:
        print(hangman_art.lose)
        end_of_game=True
        break
    #Join all the elements in the list and turn it into a String.
    print(f"Your guessing so far is: {' '.join(display)}")

    #Check if user has got all letters.
    #TODO-8: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
    if "_" not in display:
        print(hangman_art.win)
        end_of_game = True
        break

    #TODO-9: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print("\nYour Hangman's Condition so far: ")
    print(hangman_art.stages[lives])



