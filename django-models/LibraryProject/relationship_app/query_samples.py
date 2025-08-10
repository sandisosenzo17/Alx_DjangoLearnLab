from relationship_app.models import models

#List all books in a library.
library_name = models.Library.objects.create(name="Lib")
models.Library.objects.get(name=library_name)

#Query all books by a specific author.
author_name = models.Author.objects.create(name="Michio Kaku")
book1 = models.Book.objects.create(title="The book of Mad Libs", author=author_name)
book2 = models.Book.objects.create(title="The Physics of the Impossible", author=author_name)
books = models.Library.books.all()
author = models.Author.objects.get(name=author_name)
bk = models.Book.objects.filter(author=author)

#Retrieve the librarian for a library.
models.Librarian.objects.get(library=library_name)