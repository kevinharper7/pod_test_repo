class Booklist():
	def __init__(self):
            self.books = [] 
                
	def add(self, title, author):
            book = {}
            book['title'] = title
            book['author'] = author
            self.books.append(book)

	def count_books(self):
            total_books = 0 
            for book in self.books:
                total_books += 1
            return f"Total books: {total_books}"

	def remove_title(self, title):
            for book in self.books:
                if title == book['title']:
                    self.books.pop(self.books.index(book))

	def display_titles(self):
            titles = []
            for book in self.books:
                titles.append(book['title'])
            titles.sort()
            print(titles)