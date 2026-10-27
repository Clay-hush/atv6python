from conta import Conta


class ContaCorrente(Conta):
    """Conta corrente com tarifa fixa de manutenção."""

    def __init__(self, numero, cliente, saldo_inicial=0.0, tarifa=12.0):
        super().__init__(numero, cliente, saldo_inicial)
        self.tarifa = tarifa

    @property
    def tarifa(self):
        return self._tarifa

    @tarifa.setter
    def tarifa(self, valor):
        if not isinstance(valor, (int, float)) or isinstance(valor, bool) or valor < 0:
            raise ValueError("A tarifa deve ser um número não negativo.")
        self._tarifa = float(valor)

    def calcular_rendimento(self):
        """Conta corrente não oferece rendimento neste exemplo."""
        return 0.0

    def cobrar_tarifa(self):
        if self.saldo < self.tarifa:
            raise ValueError("Saldo insuficiente para cobrar a tarifa.")
        self._saldo -= self.tarifa

    def __str__(self):
        return f"Conta Corrente {self.numero} | Cliente: {self.cliente.nome} | Saldo: R$ {self.saldo:.2f} | Tarifa: R$ {self.tarifa:.2f}"
