from pakudex import *

# pakudex = Pakudex(capacity=userinput)
# # 1. add pakuri
# pakudex.add_pakuri(userinput2)

def menu():
    print("\nPakudex Main Menu")
    print('-' * 17)
    print('1. List Pakuri\n2. Show Pakuri\n3. Add Pakuri\n4. Evolve Pakuri\n5. Sort Pakuri\n6. Exit\n')



if __name__ == '__main__':
    print("Welcome to Pakudex: Tracker Extrordinaire!")
    max_capacity = int(input("Enter max capacity of the Pakudex: "))
    print(f"The Pakudex can hold {max_capacity} species of Pakuri.")

    pakudex = Pakudex(max_capacity)

    playing = True

    while playing:
        menu()
        choice = int(input("What would you like to do? "))

        if choice == 1:
            if pakudex.get_size() == 0:
                print("No Pakuri in Pakudex yet!")
            else:
                i = 1
                print('\nPakuri In Pakudex:')
                for item in pakudex.pakuri_list:
                    print(f'{i}. {item.species}')
                    i += 1

        elif choice == 2:
            pak_display = input('Enter the name of the species to display: ')
            if pak_display in pakudex.get_species_array():
                stats = pakudex.get_stats(pak_display)
                print(f'\nSpecies: {stats[0]}\nAttack: {stats[1]}\nDefense: {stats[2]}\nSpeed: {stats[3]}')
            else:
                print("Error: No such Pakuri!")

        elif choice == 3:
            pak_added = input('Enter the name of the species to add: ')
            pakudex.add_pakuri(pak_added)

        elif choice == 4:
            pak_evolvee = input("Enter the name of the species to evolve: ")
            pass

        elif choice == 5:
            pass

        elif choice == 6:
            print("Thanks for using Pakudex! Bye!")
            playing = False

        else:
            print("Unrecognized menu selection!")
