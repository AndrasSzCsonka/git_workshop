from word import word_list
import random


lives = 7
solution = []
def get_word():
    solution = random.choice(word_list)
    word_lenght = "_" * len(solution)
    print("Your word is: "+word_lenght)
    
def play():
    i="a"
    for i in solution:
        print(i)


get_word()
play()