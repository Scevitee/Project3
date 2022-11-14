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
    # Want to check if the user is inputting a positive integer value for max capacity
    initializing = True
    while initializing:
        try:
            max_capacity = int(input("Enter max capacity of the Pakudex: "))
            if max_capacity < 1:
                print("Please enter a valid size")
                continue
            initializing = False
        except:
            print("Please enter a valid size.")
            continue

        print(f"The Pakudex can hold {max_capacity} species of Pakuri.")

        pakudex = Pakudex(max_capacity)

    playing = True
    while playing:
        menu()
        choice = input("What would you like to do? ")
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
            if len(pakudex.get_species_array()) == pakudex.capacity:
                print("Error: Pakudex is full!")
                continue
            pak_added = input('Enter the name of the species to add: ')
            if pak_added in pakudex.get_species_array():
                print("Error: Pakudex already contains this species!")
            else:
                pakudex.add_pakuri(pak_added)
                print(f"Pakuri species {pak_added} successfully added!")

        elif choice == 4:
            pak_evolvee = input("Enter the name of the species to evolve: ")
            if pakudex.evolve_species(pak_evolvee) == True:
                print(f"{pak_evolvee} has evolved!")
            else:
                print("Error: No such Pakuri!")

        elif choice == 5:
            pakudex.sort_pakuri()
            print("Pakuri have been sorted!")

        elif choice == 6:
            print("Thanks for using Pakudex! Bye!")
            playing = False

        else:
            print("Unrecognized menu selection!")
