# Hangman Game

#Imports
import random

#Greating user
print('Hello in Hangman game')
print('You have to guess a word, which has same count letter as you see blanks')

#generate random word
word_list = ['kredka', 'drabina', 'kluczyk', 'migawka', 'kubek']
word = random.choice(word_list) #string - kubek
print(word)
# print(type(word))

#Create list from word
game_word = list(word) #lista ['k', 'u', 'b', 'e', 'k']
print(type(game_word))
print(game_word)

#Generate blanks for each letter in word
blank = []
for l in range(0, len(game_word)):
    blank.append('_')

print(f'Your word has these count of letters')
print(blank)


#While loop
life = 10

while life > 0:
    if game_word == blank:
        print('You guess the game word. You won!')
        life = 0
    else:
        user_answer = input('Guess a letter in word or print "exit" to leave: ')
        if user_answer == 'exit':
            print('you quit game')
            life = 0
        else:

                if user_answer in game_word:
                    print('Your letter is correct')

                    letter_count = game_word.count(user_answer)
                    print(f'In game word were: {letter_count} {user_answer}')

                    first_letter_index = word.find(f'{user_answer}')
                    blank.insert(first_letter_index, user_answer)
                    blank.pop(first_letter_index+1)

                    if letter_count > 1:
                        next_letter_index = word.find(f'{user_answer}', first_letter_index+1)
                        blank.insert(next_letter_index, user_answer)
                        blank.pop()
                        # for n in (0,letter_count-2):
                        #     blank.pop()
                    print(blank)

                else:
                    life -= 1
                    print(f'Not found this letter in game word. You loose 1 life. You have {life} lives')
                    if life == 0:
                        print(f'You lost')





#Ask user for letter

# Check letter
# while '_' in blank:
# for n in range(0,len(game_word)):
#     print('hello')