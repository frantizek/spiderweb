import sys
import argparse
from numero_letras import numero_a_letras


parser = argparse.ArgumentParser(description="Ennumera la cantidad de animales que se "
                                             "columpiaban sobre la tela de una araña.")
parser.add_argument('-a', '--animal', type=str,
                    required=False, default="elefante",
                    help="El animal que queremos que se columpie.")
parser.add_argument('-c', '--cantidad', type=int,
                    required=False, default=19,
                    help="El numero de animales que queremos que se columpien.")
args = parser.parse_args()


def plural(animal_singular):
    return animal_singular+"s"


def main(iteraciones, animal):
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
    sys.exit(main(args.cantidad, args.animal))
