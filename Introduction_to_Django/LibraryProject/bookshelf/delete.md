# ❌ Delete Operation

```python
# Import the model
from bookshelf.models import Book

# Retrieve and delete the book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Confirm deletion
print(Book.objects.all())

# Expected Output:
# <QuerySet []>
