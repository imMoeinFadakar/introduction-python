import random



# wordBank = ["tree","book","table","desk","train","fish",
#             "women","life","freedom","sky","life","python" ]

word_bank = ["book","letter","mango","apple","actor","tiger"]

trueLetters = []
wrongLetters = []

selected_word = random.choice(word_bank)
user_mistake_count = 0

string_to_list = list(selected_word)
delete_same_index = set(string_to_list)
count_of_selected_word_no_repeat = len(delete_same_index)

print(count_of_selected_word_no_repeat)







while user_mistake_count < 6:

    for i in range(len(selected_word)):

        if selected_word[i] in trueLetters:
            print(selected_word[i], end=" ")



        else:
            print("_" , end="")

    user_character = input("   please write you guess:")
    if len(user_character) == 1:


        if user_character.lower() in selected_word:
            trueLetters.append(user_character)
            count_of_selected_word_no_repeat -= 1

            if count_of_selected_word_no_repeat==0 and user_mistake_count < 6:
                print("you WON!, thanks for saving this man")
                break
            else:
                print("Right !")

        else:
            wrongLetters.append(user_character)
            user_mistake_count += 1
            print("false")
    else:
        print("please enter only one character!")


if user_mistake_count == 6:
    print("game over!  executed ")






lastWord = ", ".join(trueLetters)

print(lastWord)

