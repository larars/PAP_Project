from molecules import Molecule

class MoleculeManager:
    def __init__(self):
        self.molecules = {}

    def load_molecule(self, molecule_name):
        if molecule_name in self.molecules:
            print(f"Molecule {molecule_name} already loaded!")
            return

        molecule = Molecule(molecule_name)
        if molecule.load_from_mol_file(molecule_name):
            self.molecules[molecule_name] = molecule

    def list_molecules(self):
        if not self.molecules:
            print("No molecules loaded.")
        else:
            print(f"Number of molecules loaded: {len(self.molecules)}")
            for name in sorted(self.molecules.keys()):
                print(f"- {name}")

    def count_element(self, molecule_name, element):
        pass

    def three_d_distance(self, molecule_name, atom1, atom2):
        pass

    def filter_by_atoms(self, molecule_name, element):
        pass

    def top_bond(self, molecule_name):
        pass

    # Optional
    def subgroup_matching(self, molecule_name, substructure):
        pass