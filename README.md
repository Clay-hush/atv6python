Sistema de Funcionários em Python

Descrição

Este projeto foi desenvolvido como parte do Desafio Sprint 6, com o objetivo de aplicar os principais conceitos de Programação Orientada a Objetos em Python.

O sistema representa diferentes tipos de funcionários de uma empresa por meio de uma hierarquia de classes.

Foram aplicados conceitos como:

- Classes e objetos
- Classes abstratas
- Encapsulamento
- Herança
- Polimorfismo
- "@property"
- Métodos especiais
- Tratamento de exceções
- PEP 8

Estrutura do projeto

sprint6-poo-python/
│
├── main.py
├── funcionario.py
├── gerente.py
├── desenvolvedor.py
├── estagiario.py
└── README.md

Modelagem

A classe "Funcionario" representa as características comuns a todos os funcionários da empresa.

Ela foi definida como uma classe abstrata utilizando "ABC".

As classes "Gerente", "Desenvolvedor" e "Estagiario" herdam de "Funcionario".

classDiagram

    class Funcionario {
        <<abstract>>
        -str nome
        -str email
        -float salario

        +calcular_bonus() float
        +descricao_cargo() str

        +__str__() str
        +__repr__() str
        +__eq__(outro) bool
        +__lt__(outro) bool
    }

    class Gerente {
        -str setor

        +calcular_bonus() float
        +descricao_cargo() str
    }

    class Desenvolvedor {
        -str linguagem

        +calcular_bonus() float
        +descricao_cargo() str
    }

    class Estagiario {
        -str curso

        +calcular_bonus() float
        +descricao_cargo() str
    }

    Funcionario <|-- Gerente
    Funcionario <|-- Desenvolvedor
    Funcionario <|-- Estagiario

Classe abstrata

A classe "Funcionario" utiliza "ABC" e "@abstractmethod".

from abc import ABC, abstractmethod


class Funcionario(ABC):

    @abstractmethod
    def calcular_bonus(self):
        pass

Isso define um contrato para as subclasses.

Toda classe que herda de "Funcionario" precisa implementar o método "calcular_bonus()".

Herança

Foi utilizada herança porque:

- Gerente é um funcionário;
- Desenvolvedor é um funcionário;
- Estagiário é um funcionário.

As classes filhas utilizam:

super().__init__(nome, email, salario)

Dessa forma, atributos e validações comuns são reaproveitados a partir da classe "Funcionario".

Encapsulamento

Os atributos são protegidos por propriedades utilizando "@property".

Exemplo:

@property
def salario(self):
    return self._salario


@salario.setter
def salario(self, valor):

    if valor < 0:
        raise ValueError(
            "O salário não pode ser negativo."
        )

    self._salario = float(valor)

Essa validação impede que um objeto possua salário negativo.

Também existem validações para:

- Nome
- E-mail
- Salário
- Setor
- Linguagem de programação
- Curso

Validação de e-mail

O e-mail é validado antes de ser armazenado no objeto.

padrao = r"^[\w\.-]+@[\w\.-]+\.\w+$"

Caso o formato seja inválido, é gerada uma exceção:

raise ValueError("E-mail inválido.")

Polimorfismo

O método "calcular_bonus()" é implementado de maneira diferente em cada classe.

Gerente

def calcular_bonus(self):
    return self.salario * 0.20

O gerente recebe bônus correspondente a 20% do salário.

Desenvolvedor

def calcular_bonus(self):
    return self.salario * 0.10

O desenvolvedor recebe bônus correspondente a 10% do salário.

Estagiário

def calcular_bonus(self):
    return self.salario * 0.05

O estagiário recebe bônus correspondente a 5% da bolsa.

O polimorfismo é demonstrado no programa através de:

for funcionario in funcionarios:

    print(
        funcionario.calcular_bonus()
    )

Embora a chamada seja a mesma, cada objeto executa a implementação correspondente à sua classe.

Métodos especiais

Foram implementados métodos especiais da linguagem Python.

"__str__"

Utilizado para apresentar uma representação amigável do objeto.

print(funcionario)

"__repr__"

Apresenta uma representação técnica do objeto.

print(repr(funcionario))

"__eq__"

Permite comparar dois funcionários.

Neste projeto, funcionários são considerados iguais quando possuem o mesmo endereço de e-mail.

funcionario1 == funcionario2

"__lt__"

Permite comparar funcionários pelo salário.

Dessa forma, é possível utilizar:

sorted(funcionarios)

para ordenar os funcionários por salário.

Tratamento de exceções

O sistema utiliza blocos "try/except" para impedir que valores inválidos encerrem o programa inesperadamente.

Exemplo:

try:

    funcionario = Desenvolvedor(
        "José",
        "email_invalido",
        5000,
        "Python"
    )

except ValueError as erro:
    print(f"Erro: {erro}")

O programa apresentará:

Erro: E-mail inválido.

Instâncias utilizadas

O programa cria pelo menos 10 objetos pertencentes às diferentes subclasses:

- 2 gerentes
- 4 desenvolvedores
- 4 estagiários

Todos são armazenados em uma mesma lista.

funcionarios = [
    funcionario1,
    funcionario2,
    funcionario3,
    funcionario4,
    funcionario5,
    funcionario6,
    funcionario7,
    funcionario8,
    funcionario9,
    funcionario10
]

Essa estrutura também permite demonstrar o polimorfismo.

Exemplo de saída

============================================================
FUNCIONÁRIOS DA EMPRESA
============================================================

Gerente: Ana Silva | Setor: Tecnologia | Salário: R$ 8500.00
Descrição: Gerente responsável pelo setor de Tecnologia.
Bônus: R$ 1700.00

------------------------------------------------------------

Desenvolvedor: João Santos | Linguagem: Python | Salário: R$ 5500.00
Descrição: Desenvolvedor especializado em Python.
Bônus: R$ 550.00

------------------------------------------------------------

Estagiário: Beatriz Rocha | Curso: Análise e Desenvolvimento de Sistemas | Bolsa: R$ 1500.00
Descrição: Estagiário do curso de Análise e Desenvolvimento de Sistemas.
Bônus: R$ 75.00

Como executar

É necessário possuir o Python 3 instalado.

Clone o repositório:

git clone URL_DO_REPOSITORIO

Entre na pasta:

cd sprint6-poo-python

Execute:

python main.py

Decisões de modelagem

Foi utilizada herança porque existe uma relação clara do tipo "é um":

- Gerente é um Funcionário;
- Desenvolvedor é um Funcionário;
- Estagiário é um Funcionário.

Os atributos comuns, como nome, e-mail e salário, ficam concentrados na classe abstrata "Funcionario".

Dessa forma, evita-se repetição de código.

O método abstrato "calcular_bonus()" garante que todas as subclasses implementem uma regra para o cálculo de bônus.

A sobrescrita desse método também permite demonstrar o polimorfismo, pois cada tipo de funcionário apresenta um comportamento diferente.

O encapsulamento foi aplicado com "@property" e setters para proteger os atributos dos objetos e impedir estados inválidos.

Objetivo

O projeto demonstra a aplicação prática dos conceitos fundamentais da Programação Orientada a Objetos em Python, utilizando abstração, encapsulamento, herança e polimorfismo para criar um sistema organizado, reutilizável e de fácil manutenção.

classDiagram

    class Funcionario {
        <<abstract>>

        -str nome
        -str email
        -float salario

        +Funcionario(nome, email, salario)

        +nome
        +email
        +salario

        +calcular_bonus() float
        +descricao_cargo() str

        +__str__() str
        +__repr__() str
        +__eq__(outro) bool
        +__lt__(outro) bool
    }

    class Gerente {
        -str setor

        +Gerente(nome, email, salario, setor)

        +calcular_bonus() float
        +descricao_cargo() str
        +__str__() str
    }

    class Desenvolvedor {
        -str linguagem

        +Desenvolvedor(nome, email, salario, linguagem)

        +calcular_bonus() float
        +descricao_cargo() str
        +__str__() str
    }

    class Estagiario {
        -str curso

        +Estagiario(nome, email, salario, curso)

        +calcular_bonus() float
        +descricao_cargo() str
        +__str__() str
    }

    Funcionario <|-- Gerente
    Funcionario <|-- Desenvolvedor
    Funcionario <|-- Estagiario
