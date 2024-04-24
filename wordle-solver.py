import random

def get_word_list():
    word_list = []
    with open("words.txt", "r") as words:
        for word in words:
            word_list.append(word.strip())
    return word_list

def pick_word(list_of_words):
    random_index = random.randint(0, len(list_of_words))
    return list_of_words[random_index]

def count_frequency_letters(word):
    counter = {}
    for x in word:
        counter[x] = counter.get(x, 0) + 1
    return counter

def get_user_guess(list_of_valid_words):
    while True:
        user_input = input("Please type your guess \n")
        if user_input in list_of_valid_words:
            break
        
        print("Not a valid guess")
    return user_input

def get_letters_in_word(word):
    result = set()
    for x in word:
        result.add(x)
    return result

def check_user_guess(user_guess, answer):
    positions = [0] * len(answer)
    answer_letters = get_letters_in_word(answer)
    for index in range(len(answer)):
        if user_guess[index] == answer[index]:
            positions[index] = 2
        elif user_guess[index] in answer_letters:
            positions[index] = 1
    return positions

def main():
    words = get_word_list()
    answer = pick_word(words)
    guess = get_user_guess(words)
    positions = check_user_guess(guess, answer)

if __name__ == '__main__':
    main()