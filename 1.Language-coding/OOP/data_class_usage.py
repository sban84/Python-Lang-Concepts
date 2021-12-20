from dataclasses import dataclass


@dataclass
class Position:
    name: str
    lon: int
    lat: int
    color: str = "Blue"


pos1 = Position('India', 10.8, 59.9,"Green")
print(pos1)

pos2 = Position("Berlin", 12.0, 13.3)

print(pos1 == pos2)
print(pos1 != pos2)

