import random
print("---- HANGMAN GAME ----")
name = input("Enter Your Name : ").capitalize()
print(name ,", Welcome to our hangman game")

word_lst = ["computer", "mouse","dog","unbelievable","python","social","distance","fundamental","task"]
word = random.choice(word_lst)

hiding_word = list("_" * len(word))

guessed_word =[]
tries = 6
print(hiding_word)
while tries > 0:
    guess = input("enter a letter : ")
    if guess in guessed_word:
        print(f"{guess} already entered.")
        continue

    elif len(guess) > 1:
        print("You can enter only one letter")

    elif guess not in word:
        tries -= 1
        print(f"Absolutely wrong! You can try more {tries} times!")

    else:
        for i in range(len(word)):
            if guess == word[i]:
                print("That's right !")
                hiding_word[i] = guess
                guessed_word.append(guess)
        print(hiding_word , end='\n')

    print("Yes or No")
    answer = input("Will you guess the word ?").capitalize()

    if answer == "Yes":
        word_guess = input("What is your guess ? : ")
        if word_guess == word:
            print(" That's right ! YOU WON.")
            break
        else:
            tries -= 1
            print(f"That's wrong... You can try {tries} times more.")
        
    if tries == 0:
        print(f" You cannot try anymore... YOU LOSE!")
        break