# com resolução
import json
from aula206_a_ex import FILE_PATH, Person, do_dump

do_dump()

with open(FILE_PATH, 'r', encoding='utf8') as file:
    data = json.load(file)
    p1 = Person(**data[0])
    p2 = Person(**data[1])
    p3 = Person(**data[2])

    print(
        p1.name,
        p2.name,
        p3.name
    )

