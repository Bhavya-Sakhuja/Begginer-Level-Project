import random as rd 

easy_words = ['apple','train','tiger','money','india']
medium_words = ['python','bottle','monkey','planet','laptop']
hard_words = ['elephant','diomand','unbrella','computer','mountain']

print("Welcome to the password guessing game")
print("Choose Difficulty: easy,medium or hard")

level = input("Enter diffulity level do you want: ").lower()

if level == 'easy':
    word = rd.choice(easy_words)
elif level == 'medium':
    word = rd.choice(medium_words)
elif level == 'hard':
    word = rd.choice(hard_words)
else:
    print("Invalid Difficulty Level. By default we go with easy level")
    word = rd.choice(easy_words)

attempt = 0
print('\nGuess the secret Password')

while(True):
    guess = input("Enter your guess: ")
    attempt += 1

    if guess == word:
        print(f'Congratulations! you guessed the right word in {attempt} attempts.')
        break

    hint = ""

    for i in range(len(word)):
        if i < len(guess) and guess[i] == word[i]:
            hint += guess[i]
        else:
            hint += '_'

    print('Hint: ',hint)

print("Game Over!")