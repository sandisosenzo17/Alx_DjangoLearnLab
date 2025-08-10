from relationship_app.models import models

#List all books in a library.
library = models.Library.objects.create(name="Lib")
models.Library.objects.get(name="Lib")

#Query all books by a specific author.
books = library.books.all()
#Retrieve the librarian for a library.