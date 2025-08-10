from relationship_app.models import models

#List all books in a library.
library_name = models.Library.objects.create(name="Lib")
models.Library.objects.get(name="Lib")

#Query all books by a specific author.

#Retrieve the librarian for a library.