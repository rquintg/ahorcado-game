## Table of Contents
1. [General Info](#general-info)
2. [Technologies](#technologies)
3. [Installation](#installation)
4. [changes and improvements](#changes-and-improvements)
### General Info
***
The Data of the game are located in: archivos/data

This project is for educational purposes only 
### Screenshot
![Peaku](https://www.uniandinos.org.co/wp-content/uploads/2023/02/Logo-PeakU.png)
## Technologies
***
A list of technologies used within the project:
* [Python](https://www.python.org/): Version 3.11.3

## Installation
***

```
$ git clone [https://github.com/rquintg/ahorcado_game]
$ run main.py
```

## changes and improvements
***

## Nivel de dificultad

Se implementa un nivel de dificultad en el cual se puede elegir entre 3 niveles (facil, medio, dificil)


### Puntaje

Se agrega un puntaje que se va acumulando a medida que se aciertan las palabras, y se va restando a medida que se fallan las palabras

La puntuación se establece en word_length * 10, donde word_length es la longitud de la palabra que el jugador debe adivinar. Es decir que el jugador puede ganar ganar un máximo de 10 puntos por cada letra en la palabra.

Por cada error que selecciona una letra que no está en la palabra, se restan 2 puntos.

### Reestablecer puntaje
Al final de cada juego tiene la opcion de reestablecer el puntaje a 0

### Cambios

La funcion read_word se simplifica el codigo para reemplazar las palabras con tilde

```
for letter in word:
        if letter in 'ÁÉÍÓÚ':
            letter = letter.replace('Á', 'A').replace('É', 'E').replace('Í', 'I').replace('Ó', 'O').replace('Ú', 'U')
        word_li.append(letter)
    return ''.join(word_li)
```
La funcion new_word se optimiza
```
letters = [chr(65 + i) for i in range(26)]
```
contiene todas las letras del alfabeto en mayúsculas ('A' a 'Z'). Se utiliza para llevar un registro de las letras disponibles que el jugador puede adivinar.



