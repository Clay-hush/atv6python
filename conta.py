from abc import ABC, abstractmethod


class Conta(ABC):
    """Classe abstrata que define o comportamento comum das contas."""

    def __init__(self, numero, cliente, saldo_inicial=0.0):
        if not isinstance(numero, int) or numero <= 0:
            raise ValueError("O número da conta deve ser um inteiro positivo.")
        self.numero = numero
        self.cliente = cliente
        self.saldo = saldo_inicial

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, valor):
        if not isinstance(valor, int) or valor <= 0:
            raise ValueError("O número da conta deve ser um inteiro positivo.")
        self._numero = valor

    @property
    def cliente(self):
        return self._cliente

    @cliente.setter
    def cliente(self, valor):
        if not hasattr(valor, "nome") or not hasattr(valor, "email"):
            raise ValueError("A conta precisa estar associada a um Cliente válido.")
        self._cliente = valor

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if not isinstance(valor, (int, float)) or isinstance(valor, bool):
            raise ValueError("O saldo deve ser numérico.")
        if valor < 0:
            raise ValueError("O saldo não pode ser negativo.")
        self._saldo = float(valor)

    def depositar(self, valor):
        if not isinstance(valor, (int, float)) or isinstance(valor, bool) or valor <= 0:
            raise ValueError("O depósito deve ser um valor positivo.")
        self._saldo += float(valor)

    def sacar(self, valor):
        if not isinstance(valor, (int, float)) or isinstance(valor, bool) or valor <= 0:
            raise ValueError("O saque deve ser um valor positivo.")
        if valor > self._saldo:
            raise ValueError("Saldo insuficiente.")
        self._saldo -= float(valor)

    @abstractmethod
    def calcular_rendimento(self):
        """Calcula o rendimento específico de cada tipo de conta."""
        raise NotImplementedError

    def __str__(self):
        return f"Conta {self.numero} | {self.cliente.nome} | Saldo: R$ {self.saldo:.2f}"

    def __repr__(self):
        return f"{self.__class__.__name__}(numero={self.numero!r}, cliente={self.cliente!r}, saldo_inicial={self.saldo!r})"

    def __eq__(self, outro):
        if not isinstance(outro, Conta):
            return NotImplemented
        return self.numero == outro.numero

    def __lt__(self, outro):
        if not isinstance(outro, Conta):
            return NotImplemented
        return self.saldo < outro.saldo
