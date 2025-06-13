from dataclasses import dataclass

@dataclass
class Constructor:
    constructorId: int
    constructorRef: str
    name: str
    nationality: str
    url: str

    def __hash__(self):
        return hash(self.constructorId)

    def __str__(self):
        return f"{self.name} ({self.nationality})"
