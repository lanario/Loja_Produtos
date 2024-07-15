from dataclasses import dataclass, asdict

@dataclass
class Produto:
    nome: str
    preco: float
    desconto: float

    def __post_init__(self):
        self.desconto /= 100  # Converte a porcentagem para uma fração (ex.: 10% para 0.10)