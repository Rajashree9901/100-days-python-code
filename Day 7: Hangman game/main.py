import random
import hangman_words
from hangman_art import logo, stages

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(logo)

display = []
for _ in range(word_length):
    display += "_"

print("You have to guess")
print(f"{' '.join(display)}")
print("\n")

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    print("\n")
    if guess in display:
      print(f"you have already guessed the letter {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"{guess} is not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("\nYou lose.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("\nYou win.")
    print(stages[lives])
