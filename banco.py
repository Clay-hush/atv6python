from conta import Conta


class Banco:
    """Gerencia clientes e contas. Usa composição: o banco contém listas de objetos."""

    def __init__(self, nome):
        self.nome = nome
        self.clientes = []
        self.contas = []

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("O nome do banco não pode ficar vazio.")
        self._nome = valor.strip()

    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)

    def adicionar_conta(self, conta):
        if not isinstance(conta, Conta):
            raise TypeError("Só é possível cadastrar objetos do tipo Conta.")
        if any(c.numero == conta.numero for c in self.contas):
            raise ValueError("Já existe uma conta com esse número.")
        self.contas.append(conta)

    def buscar_conta(self, numero):
        for conta in self.contas:
            if conta.numero == numero:
                return conta
        raise LookupError(f"Conta {numero} não encontrada.")

    def __str__(self):
        return f"Banco {self.nome} | Clientes: {len(self.clientes)} | Contas: {len(self.contas)}"

    def __repr__(self):
        return f"Banco(nome={self.nome!r})"
