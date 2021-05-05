class Booklist():
    def __init__(self):
        self.books = []

    def add(self, title, author):
        book = {}
        book['title'] = title
        book['author'] = author
        self.books.append(book)


    def count_books(self):
        return f'There are {len(self.books)} books in the library.'
        print(f'There are (self.books) books in the library.')

    def remove_title(self, title):
        for book in self.books:
            if book['title'] == title:
                self.books.pop(self.books.index(book))
                print(f'I am now removing the book titled: "{title}" from the booklist.')
                # return f'I am removing the book titled: "{title}" from the booklist.' I dont need this.
        
    # def __init__(self):
    #     self.nyt_bestsellers = []
    
    # def add(self, title, author):
    #     book = {}
    #     book['title'] = title
    #     book['author'] = author
    #     self.books.append(book)
        
    # def count_books(self):
    #     return f"There are {len(self.books)} books in this new NYT BestSellers' library."

    
    def display_titles(self):
        # creating empty booklist
        titles = []
        # going through all the self.book lists/attributes and creating new list of those books.
        for books in self.books:
            titles.append(books['title'])
            print(f'New combined self.book list/attributes:"{books}" from all booklists.')


        # Now arranging/sorting book titles in alphabetical order.
        titles.sort()

        # Printing new alphabetically sorted titles' list.
        print(titles.sort())









