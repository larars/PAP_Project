from molecule_manager import MoleculeManager

# Commands
#EXIT check
#LOAD VERIFY check
#LIST MOLECULES
#COUNT ELEMENT
#3D DISTANCE
#FILTER BY ATOMS
#TOP BOND
#SUBGROUP MATCHING

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
        elif command.startswith("LOAD VERIFY"):
            # first splitting the input to get the molecule name
            _, _, molecule_name = command.split(maxsplit=2)
            molecule_manager.load_molecule(molecule_name)
        # LIST MOLECULES command
        elif command == "LIST MOLECULES":
            molecule_manager.list_molecules()
        # COUNT ELEMENT command
        elif command.startswith("COUNT ELEMENT"):
            pass
        # 3D DISTANCE command
        elif command.startswith("3D DISTANCE"):
            pass
        # FILTER BY ATOMS command
        elif command.startswith("FILTER BY ATOMS"):
            pass
        # TOP BOND command
        elif command == "TOP BOND":
            pass
        # SUBGROUP MATCHING command
        elif command.startswith("SUBGROUP MATCHING"):
            pass
        else:
            print("Unknown command.")

# Run the whole program
main()
