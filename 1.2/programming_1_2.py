class Atom:
    def __init__(self, symbol: str, atomic_number: int, neutrons: int):
        """
        Represents an atom with a symbol, atomic number, and number of neutrons.

        Args:
            symbol (str): The symbol of the atom.
            atomic_number (int): The atomic number of the atom.
            neutrons (int): The number of neutrons in the atom.
        """
        self.symbol = symbol
        self.atomic_number = atomic_number
        self.neutrons = neutrons

    def proton_number(self) -> int:
        """
        Returns the atomic number (number of protons) of the atom.

        Returns:
            int: The atomic number of the atom.
        """
        return self.atomic_number

    def mass_number(self) -> int:
        """
        Returns the mass number (sum of protons and neutrons) of the atom.

        Returns:
            int: The mass number of the atom.
        """
        return self.atomic_number + self.neutrons

    def isotope(self, neutrons: int):
        """
        Changes the number of neutrons in the atom.

        Args:
            neutrons (int): The new number of neutrons.
        """
        self.neutrons = neutrons

    def __lt__(self, other) -> bool:
        """
        Compares two atoms based on their mass numbers.

        Raises a ValueError if the atoms are of different elements.

        Args:
            other (Atom): The other atom to compare.

        Returns:
            bool: True if the mass number of self is less than other, False otherwise.
        """
        if not isinstance(other, Atom) or self.symbol != other.symbol:
            raise ValueError("Cannot compare atoms of different elements")
        return self.mass_number() < other.mass_number()

    def __le__(self, other) -> bool:
        """
        Compares two atoms based on their mass numbers.

        Raises a ValueError if the atoms are of different elements.

        Args:
            other (Atom): The other atom to compare.

        Returns:
            bool: True if the mass number of self is less than or equal to other, False otherwise.
        """
        if not isinstance(other, Atom) or self.symbol != other.symbol:
            raise ValueError("Cannot compare atoms of different elements")
        return self.mass_number() <= other.mass_number()

    def __gt__(self, other) -> bool:
        """
        Compares two atoms based on their mass numbers.

        Raises a ValueError if the atoms are of different elements.

        Args:
            other (Atom): The other atom to compare.

        Returns:
            bool: True if the mass number of self is greater than other, False otherwise.
        """
        if not isinstance(other, Atom) or self.symbol != other.symbol:
            raise ValueError("Cannot compare atoms of different elements")
        return self.mass_number() > other.mass_number()

    def __ge__(self, other) -> bool:
        """
        Compares two atoms based on their mass numbers.

        Raises a ValueError if the atoms are of different elements.

        Args:
            other (Atom): The other atom to compare.

        Returns:
            bool: True if the mass number of self is greater than or equal to other, False otherwise.
        """
        if not isinstance(other, Atom) or self.symbol != other.symbol:
            raise ValueError("Cannot compare atoms of different elements")
        return self.mass_number() >= other.mass_number()


class Molecule:
    def __init__(self, atom_counts: list[tuple[Atom, int]]):
        """
        Represents a molecule composed of atoms.

        Args:
            atom_counts (list[tuple[Atom, int]]): A list of tuples where each tuple contains an Atom object and its count in the molecule.
        """
        self.atom_counts = atom_counts

    def __str__(self) -> str:
        """
        Returns a string representation of the molecule.

        The string representation consists of the symbols of the atoms in the molecule along with their counts.
        For example, if the molecule contains two hydrogen atoms and one oxygen atom, the string representation would be "H2O".

        Returns:
            str: The string representation of the molecule.
        """
        formula = ""
        for atom, count in self.atom_counts:
            symbol = atom.symbol
            if count > 1:
                formula += symbol + str(count)
            else:
                formula += symbol
        return formula

    def __add__(self, other) -> "Molecule":
        """
        Adds two molecules together and returns a new Molecule object.

        Raises a ValueError if the other object is not a Molecule.

        Args:
            other (Molecule): The other molecule to add.

        Returns:
            Molecule: A new Molecule object that is the combination of self and other.
        """
        if not isinstance(other, Molecule):
            raise ValueError("Only molecules can be added together")
        atom_counts = self.atom_counts + other.atom_counts
        return Molecule(atom_counts)
class Chloroplast:
    def __init__(self):
        """
        Represents a chloroplast that performs photosynthesis.

        The chloroplast keeps track of the number of water and CO2 molecules available for photosynthesis.
        """
        self.water = 0
        self.co2 = 0

    def add_molecule(self, molecule: Molecule) -> list[tuple[Molecule, int]]:
        """
        Adds a molecule to the chloroplast and triggers photosynthesis if conditions are met.

        Args:
            molecule (Molecule): The molecule to add.

        Returns:
            list[tuple[Molecule, int]]: A list of tuples representing the products of photosynthesis, if it occurs.
        Raises:
            ValueError: If the molecule is not water or CO2.
        """
        if molecule == water:
            self.water += 1
        elif molecule == co2:
            self.co2 += 1
        else:
            raise ValueError("Invalid molecule")
        return self.photosynthesis()

    def photosynthesis(self) -> list[tuple[Molecule, int]]:
        """
        Performs photosynthesis if conditions are met.

        Photosynthesis occurs when there are at least 6 CO2 molecules and 12 water molecules available.
        If conditions are met, the chloroplast consumes the required molecules and produces sugar and oxygen gas.

        Returns:
            list[tuple[Molecule, int]]: A list of tuples representing the products of photosynthesis, if it occurs.
        """
        if self.co2 >= 6 and self.water >= 12:
            self.co2 -= 6
            self.water -= 12
            sugar = Molecule([(carbon, 6), (hydrogen, 12), (oxygen, 6)])
            oxygen_gas = Molecule([(oxygen, 12)])
            return [(sugar, 1), (oxygen_gas, 6)]
        return []

    def __str__(self) -> str:
        """
        Returns a string representation of the chloroplast.

        Returns:
            str: A string representation of the chloroplast including the number of water and CO2 molecules.
        """
        return f"Water: {self.water} molecules, CO2: {self.co2} molecules"


# Constants
HYDROGEN_SYMBOL = 'H'
CARBON_SYMBOL = 'C'
OXYGEN_SYMBOL = 'O'

# Atom objects
hydrogen = Atom(HYDROGEN_SYMBOL, 1, 1)
carbon = Atom(CARBON_SYMBOL, 6, 6)
oxygen = Atom(OXYGEN_SYMBOL, 8, 8)

# Molecule objects
water = Molecule([(hydrogen, 2), (oxygen, 1)])
co2 = Molecule([(carbon, 1), (oxygen, 2)])

demo = Chloroplast()
els = [water, co2]

while True:
    print('\nWhat molecule would you like to add?')
    print('[1] Water')
    print('[2] Carbon dioxide')
    print('[0] Exit')
    print('Please enter your choice: ', end='')
    try:
        choice = int(input())
        if choice == 0:
            break
        elif choice == 1 or choice == 2:
            res = demo.add_molecule(els[choice - 1])
            if len(res) == 0:
                print(demo)
            else:
                print('\n=== Photosynthesis!')
                print(res)
                print(demo)
        else:
            print('\n=== Invalid choice. Please choose again.')
    except ValueError:
        print('\n=== That is not a valid choice.')


