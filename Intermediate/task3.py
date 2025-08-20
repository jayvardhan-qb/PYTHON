'''
Develop a simple library system using classes for `Book`, `Member`, and
`Library`, with methods to add/remove books and members.
'''

class Books:
    
    def __init__(self, author, title):
        self.author = author
        self.title = title
        self.is_available = True

    def __str__(self):
        status = 'Available' if self.is_available else "Not Available"
        return f"{self.title} by {self.author} - {status} "

class Members:
    
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.is_borrowed = []

    def __str__(self):
        return f"{self.member_id} - {self.name} : Books borrowed: {book.title for book in self.is_borrowed}"

class Library:
    pass