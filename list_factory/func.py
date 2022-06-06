import random


def list_factory(n : int) -> list:
    """
    Retorna uma lista aleatória de tamanho n. 
    Validação para inteiros positivos.
    """
    if not isinstance(n, int):
        raise ValueError
    if n <= 0:
        raise ValueError

    return random.sample(range(1, n + 1), n)