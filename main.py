from molecule_manager import MoleculeManager

# Project by Lara (71843) and Ricardo (70627)
# Commands
#EXIT works
#LOAD VERIFY works
#LIST MOLECULES works
#COUNT ELEMENT works
#3D DISTANCE works
#FILTER BY ATOMS works
#TOP BOND works
#SUBGROUP MATCHING -> additional task, not implemented

def main():
    molecule_manager = MoleculeManager()
    while True:
        command = input("Command to execute: ")
        # EXIT command
        if command == "EXIT":
            # end the program
            print("Goodbye!")
            break
        # LOAD VERIFY command
        elif command.startswith("LOAD_VERIFY"):
            # first splitting the input to get the molecule name
            _, molecule_name = command.split()
            molecule_manager.load_molecule(molecule_name)
        # LIST MOLECULES command
        elif command.startswith("LIST_MOLECULES"):
            molecule_manager.list_molecules()
        # COUNT ELEMENT command
        elif command.startswith("COUNT_ELEMENT"):
            _, molecule_name, element = command.split()
            molecule_manager.count_element(molecule_name, element)
        # 3D DISTANCE command
        elif command.startswith("3D_DISTANCE"):
            _, molecule_name, atom1, atom2 = command.split()
            molecule_manager.three_d_distance(molecule_name, atom1 , atom2)
        # FILTER BY ATOMS command
        elif command.startswith("FILTER_BY_ATOMS"):
            _, k, element = command.split()
            molecule_manager.filter_by_atoms(k, element)
        # TOP BOND command
        elif command.startswith("TOP_BOND"):
            _, bond_str, n = command.split()
            molecule_manager.top_bond(bond_str, n)
        # SUBGROUP MATCHING command
        elif command.startswith("SUBGROUP_MATCHING"):
            pass
        else:
            print("Unknown command.")

# Run the whole program
main()
