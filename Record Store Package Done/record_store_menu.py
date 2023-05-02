from record_store import Record, Inventory, Store
if __name__ == '__main__':
    print("\nWelcome to the Vinyl Record Store!\n")
    store = Store()
    
    def add_record(store):
        title = input("\nEnter the record's title: ")
        artist = input("Enter the artist's name: ")
        date = input("Enter the date released: ")
        cost = float(input("Enter the record's cost: "))
        condition = input("Enter the record's condition: ")
        speed = input("Enter the record's playing speed: ")

        record = Record(cost, title, artist, date, condition, speed)
        store.add_record(record)
    def sell_record(store):
        record = input("\nWhat record would you like to sell")
    def remove_record(store):
        title = input("\nEnter the title of the record to remove: ")
        store.del_record(title)
    def search_inventory(store):
        attr = input("\nEnter the title of the record your looking for: ")
        record = store.search_inventory(attr)
        print(record)
    def set_price(store):
        title = input("\nEnter the title of the record to set the price for: ")
    while True:
        # display the menu and get the user's choice
        print("1. Display Inventory")
        print("2. Add Record")
        print("3. Remove Record")
        print("4. Search Inventory")
        print("5. Set Price")
        print("6. Sell Record")
        print("7. Clear Inventory")
        print("8. Save Inventory")
        print("9. Load Inventory")
        print("10. Quit")
        choice = input("\nPlease enter a number to select an option: ")

        # execute the appropriate function based on the user's choice
        if choice == "1":
            store.display_inventory()
        elif choice == "2":
            add_record(store)
        elif choice == "3":
            remove_record(store)
        elif choice == "4":
            search_inventory(store)
        elif choice == "5":
            set_price(store)
        elif choice == "6":
            sell_record(store)
        elif choice == "7":
            store.clear_inventory()
        elif choice == "8":
            store.save_inventory("menu inventory")
        elif choice == "9":
            store.load_inventory("menu inventory")
        elif choice == "10":
            break
        else:
            print("\nInvalid choice. Please enter a number from 1 to 10.")

   

