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
                print(f"- {name}")

    def count_element(self, molecule_name, element):
        # molecule not loaded
        if molecule_name not in self.molecules:
            print(f"The molecule {molecule_name} is not loaded.")
            return

        # count the number of atoms with the given element
        count = 0
        for atom in self.molecules[molecule_name].atoms:
            if atom["element"] == element:
                count += 1

        if count == 0:
            # atom does not exist in mol
            print(f"The atom element {element} does not exist in the {molecule_name} molecule.")
        else:
            print(f"The number of {element} atom elements in the {molecule_name} molecule is {count}.")

    def three_d_distance(self, molecule_name, atom1, atom2):
        pass

    def filter_by_atoms(self, molecule_name, element):
        pass

    def top_bond(self, molecule_name):
        pass

    # Optional
    def subgroup_matching(self, molecule_name, substructure):
        pass