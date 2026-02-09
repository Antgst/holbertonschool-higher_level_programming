#!/usr/bin/env python3
"""
task_00_abc.py

Defines an abstract base class Animal with an abstract method sound(),
and two concrete subclasses Dog and Cat that implement sound().
"""


from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract base class representing an animal.

    Subclasses must implement the sound() method.
    """
    @abstractmethod
    def sound(self):
        """
        Return the sound made by the animal.

        Returns:
            str: The sound of the animal.

        Raises:
            NotImplementedError: If not implemented by a subclass.
        """
        pass


class Dog(Animal):
    """
    Concrete Animal subclass representing a dog.
    """
    def sound(self):
        """
        Return the sound made by a dog.

        Returns:
            str: "Bark"
        """
        return "Bark"


class Cat(Animal):
    """
    Concrete Animal subclass representing a cat.
    """
    def sound(self):
        """
        Return the sound made by a cat.

        Returns:
            str: "Meow"
        """
        return "Meow"
