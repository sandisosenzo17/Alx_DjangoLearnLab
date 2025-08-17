from relationship_app.models import Author, Book, Library, Librarian

#List all books in a library.
library_name = Library.objects.create(name="Lib")
Library.objects.get(name=library_name)

#Query all books by a specific author.
author_name = Author.objects.create(name="Michio Kaku")
book1 = Book.objects.create(title="The book of Mad Libs", author=author_name)
book2 = Book.objects.create(title="The Physics of the Impossible", author=author_name)
books = Library.books.all()
author = Author.objects.get(name=author_name)
bk = Book.objects.filter(author=author)

#Retrieve the librarian for a library.
Librarian.objects.get(library=library_name)
