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
    manager = MoleculeManager()
    while True:
        command = input("Command to execute: ")
        # EXIT command
        if command == "EXIT":
            print("Goodbye!")
            break
        # LOAD VERIFY command
        elif command.startswith("LOAD VERIFY"):
            _, _, molecule_name = command.split(maxsplit=2)
            manager.load_molecule(molecule_name)
        # LIST MOLECULES command
        elif command == "LIST MOLECULES":
            manager.list_molecules()
        else:
            print("Unknown command.")

# Run the whole program
if __name__ == "__main__":
    main()
