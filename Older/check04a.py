# Write a Python 3 program according to the following:

# Person:

#   Create a class for a Person that contains a name and a birth year. The author of a book will be a Person object.

#   Create an initializer for your Person class to set the default name to be "anonymous" and the year to be "unknown".

#   Create a method, display that displays the Person's name and birth year in the format "name (b. year)"

# Book:

#   Create a class for a Book that contains a title, an author (of type Person), and a publisher.

#   Create an initializer for your Book class to set the default title to be "untitled", the author to be a Person, and the publisher to be "unpublished".

#   Create a method, display that displays the Book's information as follows (don't forget to have the book display method call the author's display method):


# The Great Divorce
# Publisher:
# Geoffrey Bles
# Author:
# C.S. Lewis (b. 1898)


# Then, create a main function that does the following:

#   Create a new book

#   Call that book's display function

#   Prompts the user for each of the following: author name and birth year, and the books title and publisher.

#   Sets these values for the current book and it's author.

#   Calls the book's display function again.


# Sample Output
##################################

# The following is an example of output for this program:


# untitled
# Publisher:
# unpublished
# Author:
# anonymous (b. unknown)

# Please enter the following:
# Name: C.S. Lewis
# Year: 1898
# Title: The Great Divorce
# Publisher: Geoffrey Bles

# The Great Divorce
# Publisher:
# Geoffrey Bles
# Author:
# C.S. Lewis (b. 1898)

class Person:

    def __init__(self):
        self.name = "anonymous"
        self.birth_yr = "unknown"

        
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_birth_yr(self):
        return self.birth_yr

    def set_birth_yr(self, birth_yr):
        self.birth_yr = birth_yr

    def display(self):
        if self.get_name() == "anonymous":
            print (self.get_name() + " (b. " + self.get_birth_yr() + ")\n")
        else:
            print (self.get_name() + " (b. " + self.get_birth_yr() + ")")

class Book(Person):

    def __init__(self, Person):
        
        self.title = "untitled"
        self.author = Person
        self.publisher = "unpublished"

        
    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def get_publisher(self):
        return self.publisher

    def set_publisher(self, publisher):
        self.publisher = publisher

    def display(self):
        if self.get_title() == "untitled":
            print (self.get_title() + "\nPublisher:\n" + self.get_publisher() + "\nAuthor:" )
            self.author.display()
        else:
            print ("\n" + self.get_title() + "\nPublisher:\n" + self.get_publisher() + "\nAuthor:" )
            self.author.display()

def prompt_user(book):
    
    print("Please enter the following:")
    book.author.set_name(input("Name: "))
    book.author.set_birth_yr(input("Year: "))
    book.set_title(input("Title: "))
    book.set_publisher(input("Publisher: "))
    return book

def main():
    
    a1 = Person()
    b1 = Book(a1)
    b1.display()
    b1 = prompt_user(b1)
    b1.display()

if __name__=="__main__": 
    main()    

    
    
