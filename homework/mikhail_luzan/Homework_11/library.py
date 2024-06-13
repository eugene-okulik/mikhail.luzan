class Book:
    material = 'Hardcover'
    text = True
    books = []

    def __init__(self, title, author, page_count, isbn):
        self.title = title
        self.author = author
        self.page_count = page_count
        self.isbn = isbn
        self.reserved = False
        Book.books.append(self)

    def __str__(self):
        book_txt = (
            f'Title: {self.title}, author: {self.author}, page count: {self.page_count}, material: {self.material}'
        )

        if self.reserved:
            return book_txt + ', reserved'
        return book_txt


class SchoolBooks(Book):
    school_books = []

    def __init__(self, title, author, page_count, isbn, subject, classroom, tasks):
        super().__init__(title, author, page_count, isbn)
        self.subject = subject
        self.classroom = classroom
        self.tasks = tasks
        SchoolBooks.school_books.append(self)

    def __str__(self):
        school_book_txt = (
            f'Title: {self.title}, author: {self.author}, page count: {self.page_count}, subject: {self.subject},'
            f' classroom: {self.classroom}'
        )

        if self.reserved:
            return school_book_txt + ', reserved'
        return school_book_txt


book_1 = Book(
    'Fourth Wing',
    'Rebecca Yarros',
    528,
    '978-1649374042'
)

book_2 = Book(
    'The Future',
    'Naomi Alderman',
    432,
    '978-1668025680'
)

book_3 = Book(
    'Hell Bent',
    'Leigh Bardugo',
    496,
    '978-1250313102'
)

book_4 = Book(
    'Murtagh: The World of Eragon',
    'Christopher Paolini',
    704,
    '978-0593650868'
)

book_5 = Book(
    'Starling House',
    'Alix E. Harrow',
    320,
    '978-1250799050'
)

book_1.reserved = True

print('\nBooks:')
for book in Book.books:
    print(book)

school_book_1 = SchoolBooks(
    'Algebra',
    'Ivanov',
    200,
    '978-1250791111',
    'Mathematics',
    'Grade 9',
    True
)

school_book_2 = SchoolBooks(
    'Geometry',
    'Petrov',
    150,
    '978-1250792222',
    'Mathematics',
    'Grade 9',
    True
)

school_book_3 = SchoolBooks(
    'Belarusian Literature',
    'Sidorov',
    300,
    '978-1250793333',
    'Belarusian',
    'Grade 7',
    False
)

school_book_3.reserved = True

print('\nSchool Books:')
for school_book in SchoolBooks.school_books:
    print(school_book)
