import random


NUM_DIGITS = 5
MAX_GUESSES = 20


def main():
    print(f'''
    Я загадал {NUM_DIGITS}-значное число без повторяющихся цифр.
    Попробуй отгадать что это за число. У тебя будет {MAX_GUESSES} попыток.
    Вот некоторые подсказки, которые помогут тебе:
    Когда я говорю:              Это означает что:
    Почти                        Одна цифра правильная, но в неправильном месте
    Точно                        Одна цифра правильная и в правильном месте
    Увы                          Ни одной правильной цифры

    Например, если загаданное число было 43218, а ты назвал 44581, то подсказка будет: Точно Почти Почти''')

    while True:
        secret_num = get_secret_num()

        print("Я загадал число!")
        print(f"У тебя есть {MAX_GUESSES} попыток чтобы его отгадать")

        num_of_guesses = 1

        while num_of_guesses <= MAX_GUESSES:
            guess = ''
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f"Попытка №{num_of_guesses}")
                guess = input('> ')

            clue = get_clue(guess, secret_num)
            print(clue)
            num_of_guesses += 1

            if guess == secret_num:
                break
            if num_of_guesses > MAX_GUESSES:
                print("Все попытки закончились")
                print(f"Ответ был: {secret_num}")

        # Asking if player wants to play one more time with
        print("Хотели бы сыграть еще? (Да/Нет)")
        if not input('> ').lower().startswith("д"):
            break
        print("Спасибо за игру!")


def get_secret_num():
    """ Return the secret number made of 10 unique random digits"""
    numbers = [x for x in range(10)] # Make a list of 10 digits
    random.shuffle(numbers)  # shuffle gigits

    secret_num = ''
    for i in range(NUM_DIGITS):
        secret_num += str(numbers[i])
    return secret_num


def get_clue(guess, secret_num):
    """ Return a clue out of guess provided """
    if guess == secret_num:
        return "У тебя получилось!"

    clues = []

    for i in range(len(secret_num)):
        if guess[i] == secret_num[i]: # correct digit at the correct place
            clues.append("Точно")
        elif guess[i] in secret_num: # correct digit in the wrong place
            clues.append("Почти")
    if len(clues) == 0: # No correct digits
        return 'Увы'

    else:
        clues.sort() # sort so that original order doesn't give information
        return ' '.join(clues)


if __name__ == '__main__':
    main()
