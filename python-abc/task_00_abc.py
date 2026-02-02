#!/usr/bin/env python3
"""
Defines an abstract Animal class and its subclasses Dog and Cat.
"""


from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        return "Bark"


class Cat(Animal):
    def sound(self):
        return "Meow"
