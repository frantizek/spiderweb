import sys
from numero_letras import numero_a_letras


def plural(animal_singular):
    return animal_singular+"s"


def main(iteraciones=10, animal="elefante"):
    for i in range(1, int(iteraciones)+1):
        if i == 1:
            print(
                '''
                {} {}, 
                se columpiaba sobre la tela de una araña, 
                como veia que resistia, fue a llamar a otro 
                {}...'''.format(numero_a_letras(i)[:-1].capitalize(), animal, animal))
        else:
            print(
                '''
                {} {}, 
                se columpiaban sobre la tela de una araña, 
                como veian que resistia, fueron a llamar a otro 
                {}...'''.format(
                    numero_a_letras(i).capitalize(), plural(animal), animal))

    
if __name__ == "__main__":
    sys.exit(main())
