# Creating a class
class Item:
    def __init__(self, title, genre, no_item, donor_name):
        self.title = title
        self.genre = genre
        self.no_item = no_item
        self.donor_name = donor_name

    # Add method
    def add(self):
        # pseudo code
        '''
            This method will allow the user(Library) to add a new item(Book, Audiobook, Film)
            by asking the user for specific details of the item.
            '''

    # Sell method
    def sell(self):
        # pseudo code
        '''
            This method will allow the user to sell an item by asking the for information of
            the item like the title and the user will let the customer know the price and
            the user will know the number of items left in the library
            '''

    # Donation method
    def donation(self):
        # pseudo code
        '''
            This method will help the user to add new items that were donated to the library
            by adding the name of the donor's name and other item details
            '''
