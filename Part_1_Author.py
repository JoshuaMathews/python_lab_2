
# Our main author class.
class Author:
    # Initialization of new class
    def __init__(self, name):
        self.name = name
        self.books = list()

    # Function (I can't stop calling everything a function) that takes book names to add to list.
    def publish(self, book_name):
        self.books.append(book_name)

    # What to do with this class when we want to convert it to a string, which is outputting name and list of books published.
    def __str__(self):
        return f'{self.name} {self.books}'


author_j = Author("Josh")

author_j.publish("Pi 3.14")
author_j.publish("See clearer with C#.")
author_j.publish("Test Example Book")

print(author_j)

author_test = Author("Testing")

author_test.publish("Testing for dummies.")
author_test.publish("Why a crashtest dummy is for you!")
author_test.publish("Get rich quick by testing this one weird trick!")
author_test.publish("Test Example Book #2 (Best selling book of 2022)")

print(author_test)