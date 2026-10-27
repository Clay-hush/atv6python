class Cliente:
    """Representa uma pessoa cliente do banco."""

    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("O nome não pode ficar vazio.")
        self._nome = valor.strip()

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor):
        if not isinstance(valor, str) or "@" not in valor or "." not in valor.split("@")[-1]:
            raise ValueError("Informe um e-mail válido.")
        self._email = valor.strip().lower()

    def __str__(self):
        return f"Cliente: {self.nome} | E-mail: {self.email}"

    def __repr__(self):
        return f"Cliente(nome={self.nome!r}, email={self.email!r})"
