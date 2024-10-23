import math
from molecules import Molecule

class MoleculeManager:
    def __init__(self):
        self.molecules = {}

    def load_molecule(self, molecule_name):
        # when molecule is already loaded stop the function
        if molecule_name in self.molecules:
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
            print(f"The molecule {molecule_name} is not loaded.")
            return

        # count the number of atoms with the given element
        count = 0
        for atom in self.molecules[molecule_name].atoms:
            if atom.element == element:
                count += 1

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
        x1, y1, z1 = self.atom1.coordinates
        x2, y2, z2 = self.atom2.coordinates

        x_difference = x1 - x2
        y_difference = y1 - y2
        z_difference = z1 - z2

        #euclidian distance formula
        distance = math.sqrt(x_difference**2 + y_difference**2 + z_difference**2)

        print(f"The 3D distance between atoms {atom1} and {atom2} of the aspirine molecule is {distance}.")

    def filter_by_atoms(self, molecule_name, element):
        pass

    def top_bond(self, molecule_name):
        pass

    # Optional
    def subgroup_matching(self, molecule_name, substructure):
        pass