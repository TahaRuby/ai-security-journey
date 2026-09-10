# Modules and global variables
from abc import ABC, abstractmethod
import random
import string


# Abstract password generator class
class PasswordGeneratorAbstract(ABC):

    @abstractmethod
    def generate_password(self, length=8):
        pass


# Numeric password generator
class NumericPasswordGenerator(PasswordGeneratorAbstract):
    characters = string.digits

    def generate_password(self, length=8):
        return "".join(
            random.choice(self.characters)
            for _ in range(length)
        )


# Letters password generator
class LettersPasswordGenerator(PasswordGeneratorAbstract):
    characters = string.ascii_letters

    def generate_password(self, length=8):
        return "".join(
            random.choice(self.characters)
            for _ in range(length)
        )


# Mixed password generator
class MixedPasswordGenerator(PasswordGeneratorAbstract):
    characters = string.digits + string.ascii_letters

    def generate_password(self, length=8):
        return "".join(
            random.choice(self.characters)
            for _ in range(length)
        )


# Run the application
generator = MixedPasswordGenerator()
#generator = NumericPasswordGenerator()
#generator = LettersPasswordGenerator()


print(generator.generate_password())