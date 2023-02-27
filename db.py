import tinydb

class GroceryDB:
    def __init__(self):
        self.db = tinydb.TinyDB('db.json',indent=4, separators=(',', ': '))
        self.table = self.db.table('grocery')

    def add(self, fruit: dict):
        '''Add a fruit to the database
        
        Args:
            fruit (dict): A dictionary containing the fruit name, quantity, price and type
        '''
        self.table.insert(fruit)

    def all(self):
        '''Get all fruits from the database'''
        return self.table.all()
    
    def get_by_type(self, type: str) -> list:
        '''Get all fruits of a specific type from the database
        
        Args:
            type (str): The type of fruit to get
        
        Returns:
            list: A list of fruits of the specified type
        '''
        q = tinydb.Query()
        return self.table.search(q.type == type)

    def get_by_name(self, name: str) -> list:
        '''Get all fruits of a specific name from the database
        
        Args:
            name (str): The name of fruit to get
        
        Returns:
            list: A list of fruits of the specified name
        '''
        q = tinydb.Query()
        return self.table.search(q.name == name)

    def get_by_price(self, price: float) -> list:
        '''Get all fruits of a specific price from the database
        
        Args:
            price (float): The price of fruit to get
        
        Returns:
            list: A list of fruits of the specified price
        '''
        q = tinydb.Query()
        return self.table.search(q.price == price)
    
    