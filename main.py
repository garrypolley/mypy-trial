""""
Example file of trying to do the type from attribute
"""
from enum import Enum
from dataclasses import dataclass
from sre_constants import ANY
from typing import Any, Final, List, Type, Union, ClassVar
from typing_extensions import reveal_type


class Fruit(str, Enum):
    apple = "apple"
    orange = "orange"
    grape = "grape"


class Vegetable(str, Enum):
    carrot = "carrot"
    potato = "potato"
    broccoli = "broccoli"


class Meat(str, Enum):
    chicken = "chicken"
    beef = "beef"
    pork = "pork"

from typing import NewType

class MetaPerson(type):
    def __new__(cls, name: str, bases: Any, attrs: dict) -> ANY: # type: ignore
        print(name, bases, attrs)
        annotations = attrs.get('__annotations__', {})
        for var_key, annotation in annotations.items():
            jj = 'hi'
            new_type = NewType(jj, annotation)
            setattr(cls, var_key, new_type)
        return super().__new__(cls, name, bases, attrs)


@dataclass
class Person(metaclass=MetaPerson):
    all_food_likes: List[Union[Fruit, Vegetable, Meat]]
    name: str
    fruit_likes: Fruit
    vegetable_likes: Vegetable
    meat_likes: Meat



def make_person(
    name: Person.name,
    all_foods: Person.all_food_likes
) -> Person:
    return Person(name=name, fruit_likes=Fruit.apple, vegetable_likes=Vegetable.broccoli, meat_likes=Meat.chicken, all_food_likes=all_foods)


