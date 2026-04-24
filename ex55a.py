from typing import Tuple


def calcular_irrf(salario: float) -> Tuple[float, float, float]:
    """
    Calcula o IRRF de acordo com o salário informado.

    Regras:
    - Até 5000.00: isento
    - De 5000.01 até 8000.00: 7.5%
    - Acima de 8000.00: 27%

    :param salario: Salário bruto do funcionário
    :return: (alíquota, valor do irrf, salário líquido)
    """
    if salario <= 5000:
        aliquota = 0.0
    elif salario <= 8000:
        aliquota = 7.5
    else:
        aliquota = 27.0

    irrf = salario * (aliquota / 100)
    salario_liquido = salario - irrf

    return aliquota, irrf, salario_liquido


def ler_salario() -> float:
    """
    Lê e valida a entrada do salário.
    Garante que o valor seja numérico e não negativo.
    """
    while True:
        try:
            salario = float(input("Digite o salário do funcionário (R$): "))
            if salario < 0:
                print("❌ Erro: o salário não pode ser negativo.")
            else:
                return salario
        except ValueError:
            print("❌ Erro: digite um valor numérico válido.")


def processar_funcionarios() -> None:
    """
    Controla o fluxo principal do programa,
    permitindo processar múltiplos funcionários.
    """
    while True:
        try:
            quantidade = int(input("Quantidade de funcionários: "))
            if quantidade <= 0:
                print("❌ Informe um número maior que zero.")
            else:
                break
        except ValueError:
            print("❌ Digite um número inteiro válido.")

    for i in range(1, quantidade + 1):
        print(f"\n=== Funcionário {i} ===")
        salario = ler_salario()

        aliquota, irrf, salario_liquido = calcular_irrf(salario)

        print(f"Salário bruto.....: R$ {salario:,.2f}")
        print(f"Alíquota de IR....: {aliquota}%")
        print(f"Valor do IRRF....: R$ {irrf:,.2f}")
        print(f"Salário líquido..: R$ {salario_liquido:,.2f}")


if __name__ == "__main__":
    processar_funcionarios()


    