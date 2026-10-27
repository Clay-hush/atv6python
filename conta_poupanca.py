from conta import Conta


class ContaPoupanca(Conta):
    """Conta poupança com taxa de rendimento percentual."""

    def __init__(self, numero, cliente, saldo_inicial=0.0, taxa_rendimento=0.5):
        super().__init__(numero, cliente, saldo_inicial)
        self.taxa_rendimento = taxa_rendimento

    @property
    def taxa_rendimento(self):
        return self._taxa_rendimento

    @taxa_rendimento.setter
    def taxa_rendimento(self, valor):
        if not isinstance(valor, (int, float)) or isinstance(valor, bool) or not 0 <= valor <= 100:
            raise ValueError("A taxa de rendimento deve estar entre 0 e 100.")
        self._taxa_rendimento = float(valor)

    def calcular_rendimento(self):
        """Retorna o rendimento estimado para um período."""
        return self.saldo * self.taxa_rendimento / 100

    def aplicar_rendimento(self):
        self._saldo += self.calcular_rendimento()

    def __str__(self):
        return f"Conta Poupança {self.numero} | Cliente: {self.cliente.nome} | Saldo: R$ {self.saldo:.2f} | Taxa: {self.taxa_rendimento:.2f}%"
