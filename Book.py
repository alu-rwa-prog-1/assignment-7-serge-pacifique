# Calling the parent class
from item import Item

# Calling a second parent class
from audiobook import Audiobook

# Creating a child class
class Book(Item, Audiobook):
    def borrow(self):
    # pseudo code
        '''
        This method will help the library do the Borrowing service
        as they will ask dor the Book title and add it mark it as borrowed
        and they will see the number of books left in the library
            '''