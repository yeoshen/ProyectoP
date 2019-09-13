import sys
import csv
import os
import random


EXAMEN = 'examen2.csv'
EXAM_SCHEMA = ['numero', 'pregunta', 'respuesta']
preguntas = []

# Abrir archivo como diccionario de datos en modo lectura


def _initialize_exam_from_storage():
    with open(EXAMEN, mode='r') as f:
        reader = csv.DictReader(f, fieldnames=EXAM_SCHEMA, delimiter=';')
        for row in reader:
            preguntas.append(row)


def _buscar_pregunta(pos):
    p = preguntas[pos-1]
    return p


def _buscar_respuestas_aleatorias(num_rep):
    r = 1
    ans = []
    while (r <= num_rep):
        ans.append(str(_buscar_pregunta_aleatoria()['respuesta']).capitalize())
        r += 1
    return ans


def _buscar_pregunta_aleatoria():
    return preguntas[random.randrange(1, 340, 1)]


def _print_welcome():
    print('EXAMEN DE NATURALIZACION EN MEXICO DE 340 PREGUNTAS')
    print('*' * 50)


def list_preguntas():
    print('numero |  pregunta  | respuesta ')
    print('*' * 150)

    for idx, pregunta in enumerate(preguntas):
        print('{uid} | {pregunta}'.format(
            uid=idx+1,
            pregunta=pregunta['pregunta']))


def _examen(num_preguntas):
    i = 1
    porcent = 0
    while i <= num_preguntas:
        os.system("clear")
        _print_welcome()
        pregunta = _buscar_pregunta_aleatoria()
        p = str(pregunta['pregunta']).capitalize()
        r = str(pregunta['respuesta']).capitalize()
        print("Pregunta No." + str(i) + ": " +
              p + "?" + "(" + pregunta['numero'] + ")")
        l1 = _buscar_respuestas_aleatorias(3)
        l1.append(r)
        random.shuffle(l1)
        print('a.- {r1}\nb.- {r2}\nc.- {r3}\nd.- {r4}'.format(
            r1=l1[0],
            r2=l1[1],
            r3=l1[2],
            r4=l1[3]))

        np = input('Respuesta: ')

        if np == 'a':
            np = l1[0]
        elif np == 'b':
            np = l1[1]
        elif np == 'c':
            np = l1[2]
        elif np == 'd':
            np = l1[3]

        if np == r:
            porcent += 1

        # input()

        i += 1

    pc = (porcent/num_preguntas)*100
    print('*' * 50)
    print('Obtuvo una calificación del {} %'.format(pc))
    if pc >= 70:
        print('Ha aprobado el examen. Felicitaciones!!!')
    else:
        print('Ha reprobado el examen lo sentimos, vuelva a intentarlo!!!')
    print('*' * 50)


if __name__ == '__main__':
    os.system("clear")
    _initialize_exam_from_storage()
    _print_welcome()
    # list_preguntas()
    #print('Cuantas preguntas quiere responder ?')
    num_preguntas = int(input('Cuantas preguntas quiere responder ? '))
    _examen(num_preguntas)
