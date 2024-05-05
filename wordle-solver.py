import random

def get_length_of_word_choice():
    while True:
        word_length_choice = input("Hi, what length of word would you like to play with:\n")
        if int(word_length_choice) > 0:
            return int(word_length_choice)
        print("Not a valid choice for word length")

def get_word_list(length_of_word):
    word_list = []
    with open("words.txt", "r") as words:
        for word in words:
            word = word.strip()
            if len(word) == length_of_word and word.islower():
                word_list.append(word.strip())
    return word_list

def pick_word(list_of_words):
    return list_of_words[random.randint(0, len(list_of_words))]

def count_frequency_letters(word):
    counter = {}
    for x in word:
        counter[x] = counter.get(x, 0) + 1
    return counter

def get_user_guess(list_of_valid_words, valid_letters):
    while True:
        user_input = input("Please type your guess \n")
        if user_input in list_of_valid_words:
            user_letters = set(user_input)
            check = all(letter in valid_letters for letter in user_letters)
            if check: 
                break
            
            print("Your guess has letters that cannot be used")
        
        print("Not a valid guess")
    return user_input

def check_user_guess(user_guess, answer):
    positions = [0] * len(answer)
    answer_letters = set(answer)
    for index in range(len(answer)):
        if user_guess[index] == answer[index]:
            positions[index] = 2
        elif user_guess[index] in answer_letters:
            positions[index] = 1
    return positions

def remove_grey_letters(letters, user_guess, user_guess_positions):
    for index in range(len(user_guess_positions)):
        if user_guess_positions[index] == 0:
            letters.remove(user_guess[index])

def get_correct_positions(user_guess_positions, answer):
    correct_positions = []
    for index in range(len(answer)):
        if user_guess_positions[index] == 2:
            correct_positions.append(answer[index])
        else:
            correct_positions.append(user_guess_positions[index])

    return correct_positions

def game_loop():
    chances = 6
    length_of_word_choice = get_length_of_word_choice()
    words = get_word_list(length_of_word_choice)
    answer = pick_word(words)
    valid_letters = list(map(chr, range(ord('a'), ord('z')+1)))
    while chances > 0:
        print("Valid letters remaining:\n", valid_letters)
        guess = get_user_guess(words, valid_letters)
        if guess == answer:
            break
        positions = check_user_guess(guess, answer)
        correct_positions = get_correct_positions(positions, answer)
        print(correct_positions)
        remove_grey_letters(valid_letters, guess, positions)
    
    if chances == 0:
        print("Sorry you failed to guess the word")
    else:
        print("You guessed the word!")

def main():
    game_loop()
    while True:
        replay = input("Would you like to play again? Y/N \n")
        if replay.capitalize() == 'N':
            print("Thanks for playing!")
            break
        elif replay.capitalize() == 'Y': 
            game_loop()
        else:
            print("Your choice was not valid")
    

if __name__ == '__main__':
    main()