import unittest
import os
from record_store import Record, Inventory, Store

class TestRecord(unittest.TestCase):
    def setUp(self):
        self.record = Record(20.00, "Test Record", "Test Artist", "2022-01-01", "new", 33)
    
    def test_get_price(self):
        self.assertEqual(self.record.get_price(), 24.99)

class TestInventory(unittest.TestCase):
    def setUp(self):
        self.inventory = Inventory([Record(20.00, "Test Record", "Test Artist", "2022", "new", 33)])
    
    def test_search_inventory(self):
        record = self.inventory.search_inventory("Test Record")
        self.assertEqual(record.title, "Test Record")
    
    def test_load_inventory(self):
        self.inventory.load_inventory("test")
        self.assertEqual(len(self.inventory.inventory), 1)
    
    def test_save_inventory(self):
        self.inventory.save_inventory("test")
        self.assertTrue(os.path.exists("test.pickle"))
    
    def test_clear_inventory(self):
        self.inventory.clear_inventory()
        self.assertEqual(len(self.inventory.inventory), 0)

class TestStore(unittest.TestCase):
    def setUp(self):
        self.store = Store(100.00, 0.00)
    
    def test_add_record(self):
        self.store.add_record(Record(20.0, "Test Record", "Test Artist", "2022", "new", 33))
        self.store.add_record(Record(15.0, "Test Record 2", "Test Artist 2", "2022", "new", 45))
        self.store.add_record(Record(15.0, "Test Record 3", "Test Artist 3", "2022", "new", 45))
        self.assertEqual(len(self.store.inventory), 3)
        self.assertEqual(self.store.get_debit(), 50.0)
        
    def test_get_inventory_value(self):
        value = self.store.get_inventory_value()
        self.assertEqual(value, 37.98)
    def test_del_record(self):
        self.store.del_record("Test Record")
        self.assertEqual(len(self.store.inventory), 2)
    
    def test_sell_record(self):
        self.store.sell_record("Test Record 2")
        self.assertEqual(self.store.get_credit(), 18.99)
        self.assertEqual(len(self.store.inventory), 1)

    def test_set_price(self):
        self.store.set_price("Test Record 3", 20.0)
        record = self.store.search_inventory("Test Record 3")
        record_price = record.get_price()
        self.assertEqual(record_price, 20.0)

if __name__ == '__main__':
    unittest.main()
