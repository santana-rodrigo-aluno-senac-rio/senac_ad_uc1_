from typing import List


def ler_nota(indice: int) -> float:
    """
    Lê uma nota do usuário garantindo que seja um número entre 0 e 10.
    """
    while True:
        try:
            valor = float(input(f"Digite a nota {indice}: "))
            if 0.0 <= valor <= 10.0:
                return valor
            raise ValueError("Nota fora do intervalo permitido.")
        except ValueError:
            print("Entrada inválida. Informe um número entre 0 e 10.")


def calcular_media(notas: List[float]) -> float:
    """
    Calcula a média aritmética de uma lista de notas.
    """
    return sum(notas) / len(notas)


def determinar_status(media: float) -> str:
    """
    Retorna o status do aluno com base na média.
    """
    if media >= 6.0:
        return "Aprovado"
    return "Recuperação"


def main() -> None:
    QUANTIDADE_NOTAS = 3
    notas: List[float] = []

    for i in range(1, QUANTIDADE_NOTAS + 1):
        notas.append(ler_nota(i))

    media = calcular_media(notas)
    status = determinar_status(media)

    print(f"\nMédia final: {media:.2f}")
    print(f"Status: {status}")


if __name__ == "__main__":
    main()