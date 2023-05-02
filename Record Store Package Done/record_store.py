"""
A virtual vinyl record store made to store and sell records.
"""
import pickle
import math

class Record:
    """
    Class to represent a vinyll record using it's cost, title, artist name, date released,
    condition, and playing speed.
    """
    def __init__(self, cost, title, artist, date, condition, speed):
        """
        Sets a record object using from 6 attributs.
        """
        self.cost = cost
        self.title = title
        self.artist = artist
        self.date = date
        self.condition = condition
        self.speed = speed
        # Creats a price based of the cost to insure 20% profit.
        self.price = math.ceil(self.cost * 1.20) + .99
    def get_price(self):
        """
        Sets a new price for a given record.
        """
        return self.price
    def __repr__(self, ):
        """
        Informal string representation for the Record class.
        """
        return "Title: {}\nArtist: {}\nDate : {}\nPrice: {}\nCost: {}\nCondition: {}\nSpeed: {}\n"\
                .format(self.title, self.artist, self.date, self.price, self.cost, self.condition,\
                        self.speed)
class Inventory:
    """
    Class to virtually represent a store's inventory.
    """
    def __init__(self, inventory):
        self.inventory = inventory
    def display_inventory(self):
        """
        Displays a list of records and there attributes that are in the inventory.
        """
        print("\nCurrent Inventory:\n")
        for record in self.inventory:
            print(record)
    def save_inventory(self, file):
        """
        Saves the an inventory to a pickle file that is named by the user.
        Writes and encrypts the data in the inventory to the file using UTP-8 encryption.
        """
        try:
            with open(str(file)+".pickle","wb") as inventory_out:
                pickle.dump(self.inventory, inventory_out)
                print("Inventory saved!")
        except FileNotFoundError:
            pass
        except EOFError:
            pass
    def load_inventory(self, file):
        """
        Loads a pickle file in the same directory as a program
        """
        try:
            with open(str(file) + ".pickle", "rb") as inventory_in:
                self.inventory = pickle.load(inventory_in)
                print("Loading inventory...")
        except FileNotFoundError:
            pass
        except EOFError:
            pass
    def clear_inventory(self):
        """
        Clears the inventory of all records.
        """
        print("\nClearing inventory")
        self.inventory = []
        print("Inventory cleared.")
    def del_record(self, title):
        """
        Deletes a single record from the inventory.
        """
        record = self.search_inventory(title)
        if record == "\nThere are no records with that attribute in the store's inventory.":
            print("\nThere is no such record.")
        else:
            try:
                self.inventory.remove(record)
                print(title+" removed.")
                self.save_inventory('Record_Inventory')
            except AttributeError:
                pass
    def search_inventory(self, attr):
        """
        Searches the store's inventory for specific attribute.
        """
        desired_attr = attr
        try:
            for record in self.inventory:
                if record.title ==desired_attr:
                    return record
        except TypeError:
            return "\nThere are no records with that attribute in the store's inventory."
    def __repr__(self, ):
        """
        Informal string representation for the Inventory class.
        """
        return "Inventory where record objects are stored."

class Store(Inventory):
    """
    Creates the store object with the attribute debit and credit.
    """
    def __init__(self, debit = 0, credit = 0, inventory = []):
        """
        Sets the stores attributes. An Inventory object is created and to store records.
        """
        super().__init__(inventory)
        self.debit = debit
        self.credit = credit
    def get_debit(self):
        """
        Returns the stores current debit.
        """
        return self.debit
    def get_credit(self):
        """
        Returns the stores current credit.
        """
        return self.credit
    def add_record(self, record):
        """
        Removes cost from the debit and adds record to inventory.
        """
        self.debit -= float(record.cost)
        self.inventory.append(record)
        self.save_inventory('Record_Inventory')
        print("Added record",record.title)
    def del_record(self, title):
        """
        Searches inventory for given record.
        Removes the record from the inventory.
        """
        record = self.search_inventory(title)
        if record == "\nThere are no records with that name in the store's inventory.":
            print("\nThere is no such record.")
        else:
            try:
                self.inventory.remove(record)
                print(title+" removed.")
                self.save_inventory('Record_Inventory')
            except AttributeError:
                pass
    def sell_record(self, title):
        """
        Searches inventory for given record.
        If record exists, removes record from inventory.
        Adds records price to the records credit.
        """
        record = self.search_inventory(title)
        if record == "\nThere are no records with that name in the store's inventory.":
            print("\nThere is no such record.")
        else:
            self.credit += float(record.price)
            print("Sold:",record.title)
            self.inventory.remove(record)
            self.save_inventory('Record_Inventory')

    def set_price(self, title, price):
        """
        Searches inverntory for given record and changes its price.
        """
        record = self.search_inventory(title)
        if record == "There are no records with that name in the store's inventory.":
            print("There is no such record.")
        else:
            for record in self.inventory:
                if record.title == title:
                    record.price = price
            print("Changing the price of "+str(title)+" to "+str(price))
            self.save_inventory('Record_Inventory')
    def get_price(self, title):
        """
        Searches inventory for a given record and returns its price.
        """
        if not self.inventory:
            print("Inventory is empty.")
            return None
        for item in self.inventory:
            if item.title == title:
                return item.price
        raise ValueError("Record not found in inventory.")
    def sort_inventory(self, key):
        """
        Sorts the inventory based on the provided key.
        """
        self.inventory = sorted(self.inventory, key=key)
    def get_inventory_value(self):
        inventory_value = 0
        for record in self.inventory:
            inventory_value += record.price
        return inventory_value
    def __repr__(self, ):
        """
        Informal string representation for the Store class.
        """
        return "Record Store with credit of ${} and debit of ${}. The store currently has"\
                " {} record(s)"\
                .format(self.credit, self.debit, len(self.inventory))

if __name__ == "__main__":
    print("Creates a virtual Record Store with an inventory to store and sell vinyl records.",\
          "Contains a Store, Inventory and Record Classes.")
    r = Record(8.00, "Rumours", "Fleetwood Mac", 1997, "used", 33)
    s = Store()
    i = Inventory([])
