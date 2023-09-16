import os
import random


def logo_hangman():
    print('''
    ╔═══════════════════════════════════════════════════════════╗
    ║                                                           ║
    ║   █   █   █████   █   █   █████   █   █   █████   █   █   ║
    ║   █   █   █   █   ██  █   █       ██ ██   █   █   ██  █   ║
    ║   █████   █████   █ █ █   █████   █ █ █   █████   █ █ █   ║
    ║   █   █   █   █   █  ██   █   █   █   █   █   █   █  ██   ║
    ║   █   █   █   █   █   █   █████   █   █   █   █   █   █   ║
    ║                                                           ║
    ╚═══════════════════════════════════════════════════════════╝
''')


def image_hangman():
    die0 = '''













'''
    die1 = '''







        _____________
      /             /|
     /____________ / |
    |             | /
    |_____________|/

'''
    die2 = '''
          ╔
          ║
          ║
          ║
          ║
          ║
          ║
        __║__________
      /   ║         /|
     /____________ / |
    |             | /
    |_____________|/

'''
    die3 = '''
          ╔═════╦  
          ║
          ║
          ║
          ║
          ║
          ║
        __║__________
      /   ║         /|
     /____________ / |
    |             | /
    |_____________|/

'''
    die4 = '''
          ╔═════╦  
          ║
          ║
          ║
          ║
          ║
          ║   d   b
        __║__________
      /   ║         /|
     /____________ / |
    |             | /
    |_____________|/

'''
    die5 = '''
          ╔═════╦  
          ║
          ║
          ║
          ║
          ║    / ''' + chr(92) + '''
          ║   d   b
        __║__________
      /   ║         /|
     /____________ / |
    |             | /
    |_____________|/

'''
    die6 = '''
          ╔═════╦  
          ║
          ║
          ║
          ║     │
          ║    / ''' + chr(92) + '''
          ║   d   b
        __║__________
      /   ║         /|
     /____________ / |
    |             | /
    |_____________|/

'''
    die7 = '''
          ╔═════╦  
          ║
          ║
          ║    ─┼─
          ║     │
          ║    / ''' + chr(92) + '''
          ║   d   b
        __║__________
      /   ║         /|
     /____________ / |
    |             | /
    |_____________|/

'''
    die8 = '''
          ╔═════╦  
          ║
          ║
          ║   ┌─┼─┐
          ║     │
          ║    / ''' + chr(92) + '''
          ║   d   b
        __║__________
      /   ║         /|
     /____________ / |
    |             | /
    |_____________|/

'''
    die9 = '''
          ╔═════╦  
          ║
          ║     @
          ║   ┌─┼─┐
          ║     │
          ║    / ''' + chr(92) + '''
          ║   d   b
        __║__________
      /   ║         /|
     /____________ / |
    |             | /
    |_____________|/

'''
    die10 = '''
          ╔═════╦  
          ║     │
          ║     @       ¡AHORCADO!
          ║   ┌─┼─┐
          ║     │
          ║    / ''' + chr(92) + '''
          ║   d   b
        __║__________
      /   ║         /|
     /____________ / |
    |             | /
    |_____________|/

'''
    die11 = '''
          ╔═════╦  
          ║
          ║     
          ║
          ║              ¡GANASTE!
          ║
          ║                  
        __║__________        @
      /   ║         /|     └─┼─┘  
     /____________ / |       │
    |             | /       / ''' + chr(92) + '''
    |_____________|/       d   b

'''
    deaths = {0: die0, 1: die1, 2: die2, 3: die3, 4: die4, 5: die5, 6: die6, 7: die7, 8: die8, 9: die9, 10: die10,
              11: die11}
    return deaths


def read_word(level):
    word_li = []
    with open('./archivos/data.txt', 'r', encoding='utf-8') as data_words:
        words = [word.strip().upper() for word in data_words]

    if level == 'facil':
        words = [word for word in words if len(word) <= 5]
    elif level == 'medio':
        words = [word for word in words if 5 < len(word) <= 8]
    elif level == 'dificil':
        words = [word for word in words if len(word) > 8]

    word = random.choice(words)

    for letter in word:
        if letter in 'ÁÉÍÓÚ':
            letter = letter.replace('Á', 'A').replace('É', 'E').replace('Í', 'I').replace('Ó', 'O').replace('Ú', 'U')
        word_li.append(letter)
    return ''.join(word_li)


def new_word(level):
    word = read_word(level)
    dict_word = {i[0]: i[1] for i in enumerate(word)}
    discovered = ['- ' for i in range(len(dict_word))]
    deaths = 0
    letters = [chr(65 + i) for i in range(26)]
    return word, dict_word, discovered, deaths, letters


def compare_letter(letter, dict_word, discovered, fail):
    for l, char in dict_word.items():
        if char == letter:
            discovered[l] = letter + ' '
            fail = False
    return discovered, fail


def calculate_score(word_length, deaths):
    return (word_length * 10) - (deaths * 2)


def refresh(hangman_deaths, deaths, letters, score):
    os.system('clear')
    logo_hangman()
    print('Letras disponibles: ' + "  ".join(letters))
    print(hangman_deaths.get(deaths))
    print(f"Puntuación actual: {score}")


def run_game():
    hangman_deaths = image_hangman()
    score = 0

    while True:
        os.system('clear')
        logo_hangman()
        level = input("Selecciona un nivel (facil, medio o dificil): ").lower()

        while level not in ['facil', 'medio', 'dificil']:
            level = input("Nivel no válido. Selecciona un nivel (facil, medio o dificil): ").lower()

        word = ''
        dict_word = {}
        discovered = []
        deaths = 0
        letters = []
        non_letter = 0
        word, dict_word, discovered, deaths, letters = new_word(level)
        word_length = len(word)

        while True:
            refresh(hangman_deaths, deaths, letters, score)

            if non_letter == 1:
                print('Debes ingresar una de las letras disponibles')
                non_letter = 0

            try:
                letter = input(f'''¡Adivina la palabra!     {''.join(discovered)}
Ingresa una letra: ''').upper()

                if letter not in letters:
                    raise ValueError

                letters.remove(letter)

            except ValueError:
                non_letter = 1

            fail = True
            discovered, fail = compare_letter(letter, dict_word, discovered, fail)

            if fail == True:
                deaths += 1
                if deaths == 10:
                    refresh(hangman_deaths, deaths, letters, score)
                    print('¡Perdiste! La palabra era ' + word)
                    print(f"Tu puntuación final es: {score}")
                    again = input('¿Quieres jugar otra vez? (1-Si 0-No):  ')
                    if again == '1':
                        reset_score = input('¿Quieres reiniciar tu puntaje? (1-Si 0-No): ')
                        if reset_score == '1':
                            score = 0
                        break
                    else:
                        print('Gracias por jugar :)')
                        return

            if ''.join(discovered).replace(' ', '') == word:
                score += calculate_score(word_length, deaths)
                refresh(hangman_deaths, 11, letters, score)
                print(f'¡Ganaste! La palabra era {word}')
                print(f"Tu puntuación final es: {score}")
                again = input('¿Quieres jugar otra vez? (1-Si 0-No):  ')
                if again == '1':
                    reset_score = input('¿Quieres reiniciar tu puntaje? (1-Si 0-No): ')
                    if reset_score == '1':
                        score = 0
                    break
                else:
                    print('Gracias por jugar :)')
                    return


if __name__ == '__main__':
    run_game()
