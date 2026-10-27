from cliente import Cliente
from conta_corrente import ContaCorrente
from conta_poupanca import ContaPoupanca
from banco import Banco


def demonstrar_sistema():
    banco = Banco("Banco Sprint 6")

    # Cinco clientes e cinco contas: 10 instâncias, sem contar o banco.
    clientes = [
        Cliente("Ana Lima", "ana@example.com"),
        Cliente("Bruno Souza", "bruno@example.com"),
        Cliente("Carla Mendes", "carla@example.com"),
        Cliente("Diego Alves", "diego@example.com"),
        Cliente("Eva Santos", "eva@example.com"),
    ]

    contas = [
        ContaCorrente(101, clientes[0], 800, 10),
        ContaPoupanca(102, clientes[1], 1200, 0.6),
        ContaCorrente(103, clientes[2], 450, 12),
        ContaPoupanca(104, clientes[3], 2000, 0.7),
        ContaCorrente(105, clientes[4], 150, 8),
    ]

    for cliente in clientes:
        banco.adicionar_cliente(cliente)
    for conta in contas:
        banco.adicionar_conta(conta)

    print("=== SISTEMA BANCÁRIO ===")
    print(banco)
    print("\n=== CONTAS CADASTRADAS ===")
    for conta in banco.contas:
        print(conta)

    print("\n=== DEMONSTRAÇÃO DE POLIMORFISMO ===")
    # A mesma chamada produz resultados diferentes conforme a classe concreta.
    for conta in banco.contas:
        rendimento = conta.calcular_rendimento()
        print(f"Conta {conta.numero} ({type(conta).__name__}): rendimento = R$ {rendimento:.2f}")

    print("\n=== OPERAÇÕES ===")
    contas[0].depositar(100)
    contas[0].sacar(50)
    contas[1].aplicar_rendimento()
    print(contas[0])
    print(contas[1])

    print("\n=== ORDENAÇÃO POR SALDO ===")
    for conta in sorted(banco.contas):
        print(f"Conta {conta.numero}: R$ {conta.saldo:.2f}")

    print("\n=== TRATAMENTO DE EXCEÇÕES ===")
    try:
        clientes[0].email = "email-invalido"
    except ValueError as erro:
        print(f"E-mail inválido tratado: {erro}")

    try:
        contas[0].sacar(999999)
    except ValueError as erro:
        print(f"Saque inválido tratado: {erro}")

    try:
        contas[0].saldo = -10
    except ValueError as erro:
        print(f"Saldo inválido tratado: {erro}")

    try:
        banco.adicionar_conta(ContaCorrente(101, clientes[0], 50))
    except ValueError as erro:
        print(f"Conta duplicada tratada: {erro}")


if __name__ == "__main__":
    demonstrar_sistema()
