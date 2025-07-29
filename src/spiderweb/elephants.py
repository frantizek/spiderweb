import argparse

from numero_letras import numero_a_letras

parser = argparse.ArgumentParser(
    description="Ennumera la cantidad de animales que se "
    "columpiaban sobre la tela de una araña."
)
parser.add_argument(
    "-a",
    "--animal",
    type=str,
    required=False,
    default="elefante",
    help="El animal que queremos que se columpie.",
)
parser.add_argument(
    "-c",
    "--cantidad",
    type=int,
    required=False,
    default=19,
    help="El numero de animales que queremos que se columpien.",
)
args = parser.parse_args()


def plural(animal_singular: str) -> str:
    if animal_singular.endswith("s"):
        return animal_singular
    elif animal_singular.endswith("z"):
        return animal_singular.replace("z", "ces")
    elif (
        animal_singular.endswith("i")
        or animal_singular.endswith("n")
        or animal_singular.endswith("r")
        or animal_singular.endswith("l")
    ):
        return animal_singular + "es"
    else:
        return animal_singular + "s"


def main(iteraciones: int, animal: str) -> None:
    for i in range(1, int(iteraciones) + 1):
        if i == 1:
            print(
                f"""
{numero_a_letras(i)[:-1].capitalize()} {animal},
se columpiaba sobre la tela de una araña,
como veia que resistia, fue a llamar a otro
{animal}..."""
            )
        else:
            print(
                f"""
{numero_a_letras(i).capitalize()} {plural(animal)},
se columpiaban sobre la tela de una araña,
como veian que resistia, fueron a llamar a otro
{animal}..."""
            )
    print("\n")


if __name__ == "__main__":
    main(args.cantidad, args.animal)
