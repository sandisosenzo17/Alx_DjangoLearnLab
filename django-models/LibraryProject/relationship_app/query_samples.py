from relationship_app.models import models

#List all books in a library.
library_name = models.Library.objects.create(name="Lib")
models.Library.objects.get(name=library_name)

#Query all books by a specific author.
books = models.Library.books.all()
#Retrieve the librarian for a library.