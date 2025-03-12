import dataclasses
import random
from dataclasses import dataclass

class Tea:
    def __init__(self, nume, yip, pret):
        self.id = random.randint(1, 1000)

@dataclass
class Ceai:
    id: int = dataclasses.field(init=False, default=0)
    nume: str
    tip: str
    pret: float
    _id = 0

    def __post_init__(self):
        self.id = Ceai.id
        Ceai.id = random.randint(1, 1000)
