# Update the title
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
print(book)

# Output:
# <Book: Nineteen Eighty-Four by George Orwell (1949)>
