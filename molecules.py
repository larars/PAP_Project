import os

# Folder with the molecule files
MOLECULES_FOLDER = "molecules"

# the organic elements for the atoms: H, B, C, N, O, P, S, F, Cl, Br, and I
ORGANIC_ELEMENTS = {"H", "B", "C", "N", "O", "P", "S", "F", "Cl", "Br", "I"}

class Atom:
    def __init__(self, index, element, x, y, z):
        self.index = index              # atom index
        self.element = element          # element symbol
        self.coordinates = (x, y, z)    # tuple to show coordinates

class Bond:
    def __init__(self, atom1, atom2, bond_type):
        self.atom1 = atom1              # atom 1 of the bond
        self.atom2 = atom2              # atom 2 of the bond
        self.bond_type = bond_type      # type of chemical bond

class Molecule:
    def __init__(self, name):
        self.name = name        # molecule name
        self.atoms = []         # list of atoms
        self.bonds = []         # list of bonds

    def load_from_mol_file(self, molecule_name):
        molecule_file_path = os.path.join(MOLECULES_FOLDER, molecule_name)
        if not os.path.exists(molecule_file_path):
            return False

        # Read molecule file
        file = open(molecule_file_path, 'r')
        lines = file.readlines()
        file.close()

        # Getting header and atom/bond counts
        self.name = lines[0].strip()
        # number of bonds and atoms
        atom_count = int(lines[3][:3])
        bond_count = int(lines[3][3:6])

        # Atom block
        atom_start = 4
        atom_end = atom_start + atom_count
        atom_ids = []
        for i in range(atom_start, atom_end):
            parts = lines[i].split()
            x = float(parts[0])     # x coordinate
            y = float(parts[1])     # y coordinate
            z = float(parts[2])     # z coordinate
            element = parts[3]      # element symbol

            # Check if the element is organic
            # 2nd validation step
            if element not in ORGANIC_ELEMENTS:
                print(f"File {molecule_name} could not be loaded. Contains non-organic elements.")
                return False

            atom_id = i - atom_start + 1
            self.atoms.append(Atom(atom_id, element, x, y, z))
            atom_ids.append(atom_id)

        # Bond block
        bond_start = atom_end
        bond_end = bond_start + bond_count
        # Check if there are enough lines for the bonds block
        # #3rd validation step part 1
        if bond_end > len(lines):
            print(f"File {molecule_name} could not be loaded. Bonds block is incomplete.")
            return False

        for i in range(bond_start, bond_end):
            parts = lines[i].split()
            atom1 = int(parts[0])
            atom2 = int(parts[1])
            bond_type = int(parts[2])
            self.bonds.append(Bond(atom1, atom2, bond_type))

        # Check if number of bonds matches the number from the header
        # 3rd validation step part 2
        if len(self.bonds) != bond_count:
            print(f"File {molecule_name} could not be loaded. Bonds block is incomplete.")
            return False

        # Check that all atoms are referenced in at least one bond
        # 4th validation step
        bonded_atoms = {bond.atom1 for bond in self.bonds} | {bond.atom2 for bond in self.bonds}
        if not atom_ids.issubset(bonded_atoms):
            print(f"File {molecule_name} could not be loaded. Bonds block does not cover all atoms.")
            return False

        # If all checks passed, the molecule is valid
        print(f"File {molecule_name} validated and loaded!")
        return True
