import math
from molecules import Molecule
from molecules import ORGANIC_ELEMENTS

class MoleculeManager:
    def __init__(self):
        self.molecules = {}

    def load_molecule(self, molecule_name):
        # when molecule is already loaded stop the function
        if molecule_name in self.molecules:
            molecule_name = molecule_name.replace('.mol', '')
            print(f"Molecule {molecule_name} already loaded!")
            return

        # load the molecule and add it to the dictionary
        molecule = Molecule(molecule_name)
        if molecule.load_from_mol_file(molecule_name):
            self.molecules[molecule_name] = molecule

    def list_molecules(self):
        # no molecules loaded
        if self.molecules == {}:
            print("No molecules loaded.")
        # molecules loaded
        else:
            # gets the number of molecules loaded and prints the names in alphabetical order
            print(f"Number of molecules loaded: {len(self.molecules)}")
            for name in sorted(self.molecules.keys()):
                mol_without_mol = name.replace('.mol', '')
                print(f"- {mol_without_mol}")

    def count_element(self, molecule_name, element):
        # add .mol to the molecule name
        molecule_name += ".mol"
        # molecule not loaded
        if molecule_name not in self.molecules:
            molecule_name = molecule_name.replace('.mol', '')
            print(f"The molecule {molecule_name} is not loaded.")
            return

        # count the number of atoms with the given element
        count = 0
        for atom in self.molecules[molecule_name].atoms:
            if atom.element == element:
                count += 1

        molecule_name = molecule_name.replace('.mol', '')

        if count == 0:
            # atom does not exist in mol
            print(f"The atom element {element} does not exist in the {molecule_name} molecule.")
        else:
            print(f"The number of {element} atom elements in the {molecule_name} molecule is {count}.")

    def three_d_distance(self, molecule_name, atom1, atom2):
        # add .mol to the molecule name
        molecule_name += ".mol"
        # molecule not loaded
        if molecule_name not in self.molecules:
            molecule_name = molecule_name.replace('.mol', '')
            print(f"The molecule {molecule_name} is not loaded.")
            return

        # Get the molecule object
        molecule = self.molecules[molecule_name]

        # get the atom identifiers
        atom1_id = int(atom1)
        atom2_id = int(atom2)

        # Check if the atom identifiers are valid
        if atom1_id < 1 or atom1_id > len(molecule.atoms) or atom2_id < 1 or atom2_id > len(molecule.atoms):
            print("Invalid atom identifier provided.")
            return

        # get the atom objects
        atom1_obj = molecule.atoms[atom1_id - 1]
        atom2_obj = molecule.atoms[atom2_id - 1]

        # check if cordinates are available, when they are all 0, the coordinates are not available
        if atom1_obj.coordinates == (0.0, 0.0, 0.0) or atom2_obj.coordinates == (0.0, 0.0, 0.0):
            print("Cannot compute the 3D distance. Coordinates are not available.")
            return


        # get coordinates of the two atoms
        x1, y1, z1 = atom1_obj.coordinates
        x2, y2, z2 = atom2_obj.coordinates

        x_difference = x1 - x2
        y_difference = y1 - y2
        z_difference = z1 - z2

        #euclidian distance formula
        distance = math.sqrt(x_difference**2 + y_difference**2 + z_difference**2)
        rounded_distance = round(distance, 2)

        print(f"The 3D distance between atoms {atom1} and {atom2} of the aspirine molecule is {rounded_distance}.")

    def filter_by_atoms(self, k, element):
        if element not in ORGANIC_ELEMENTS:
            print("The provided atom is not part of the list of organic atoms.")
            return

        # Check if any molecules are loaded
        if self.molecules == {}:
            print("No molecules loaded.")
            return

        # convert k into an integer
        k = int(k)

        # check for matching mols
        matching_mols = []
        for name, molecule in self.molecules.items():
            # Count the number of atoms of the given type in the molecule
            count = sum(1 for atom in molecule.atoms if atom.element == element)
            # Check if the count is at least k
            if count >= k:
                matching_mols.append(name)

        # get alphabetic order
        matching_mols.sort()

        # print matching mols
        if matching_mols:
            print("List of loaded molecules that meet the specified criteria:")
            for molecule_name in matching_mols:
                mol_without_mol = molecule_name.replace('.mol', '')
                print(f"- {mol_without_mol}")
        # there are no matching mols
        else:
            print("No loaded molecule matches the criteria.")

    def top_bond(self, bond_str, n):

        # Split the bond into two atoms
        atom1_element, atom2_element = bond_str.split('-')

        # convert n to int
        n = int(n)

        # check if atoms are organic
        if atom1_element not in ORGANIC_ELEMENTS or atom2_element not in ORGANIC_ELEMENTS:
            print("The provided atom is not part of the list of organic atoms.")
            return

        # Check if molecules are loaded
        if self.molecules == {}:
            print("No molecules loaded.")
            return

        # Count occurrences of the bond in each molecule
        bond_counts = []
        for name, molecule in self.molecules.items():
            # Count the number of occurrences of both Ai−Aj and Aj−Ai in the molecule's bonds
            count = sum(
                (molecule.atoms[bond.atom1 - 1].element == atom1_element and molecule.atoms[
                    bond.atom2 - 1].element == atom2_element) or
                (molecule.atoms[bond.atom1 - 1].element == atom2_element and molecule.atoms[
                    bond.atom2 - 1].element == atom1_element)
                for bond in molecule.bonds
            )
            if count > 0:
                bond_counts.append((name, count))

        # Sort the list first by count and then by name
        bond_counts = sorted(bond_counts, key=lambda x: (-x[1], x[0]))

        # Select the top n molecules
        top_n = bond_counts[:n]

        # Print the results
        if top_n:
            print("Top of loaded molecules with the provided bond:")
            for molecule_name, count in top_n:
                mol_without_mol = molecule_name.replace('.mol', '')
                print(f"{mol_without_mol} - {count}")
        else:
            print("No molecules with the provided bond.")

    # Optional
    def subgroup_matching(self, molecule_name, substructure):
        pass