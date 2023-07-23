# Title:      Book Classes
# Filename:   check06a.py
# Purpose:    Demonstrates inheritance
#             with different book classes.
# Date:       02/08/2021
###############################################

# Requirements
######################################################################
# Create a class for a Book that has the following member variables:
# 
# title : string
# 
# author : string
# 
# publication_year : int
# 
# Next, create a class for a TextBook that extends a Book and adds the following member variable:
# 
# subject : string
# 
# Finally, create a class for a PictureBook that that extends a Book and adds the following member variable:
# 
# illustrator : string
# 
# In the base Book class, create a method prompt_book_info that
# prompts the user for the title, author, and publication_year,
# and also a method display_book_info that displays the title, author,
# and publication year in the format:
#
#                       "Title (publication_year) by Author".
# 
# In the TextBook class, create methods prompt_subject and display_subject
# that prompt and display the subject of the book.
# 
# In the PictureBook class, create methods prompt_illustrator and
# display_illustrator that prompt and display the Illustrator of the book.
# 
# In main, first create a Book object and call the following methods:
# 
# prompt_book_info
# 
# display_book_info
# 
# Next, create a TextBook object and call the following methods:
# 
# prompt_book_info
# 
# prompt_subject
# 
# display_book_info
# 
# display_subject
# 
# Finally, create a PictureBook object and call the following methods:
# 
# prompt_book_info
# 
# prompt_illustrator
# 
# display_book_info
# 
# display_illustrator

# Sample Output
######################################################################
# Title: The Miracle of Forgiveness
# Author: Spencer W. Kimball
# Publication Year: 1969
# 
# The Miracle of Forgiveness (1969) by Spencer W. Kimball
# 
# Title: Introduction to C++
# Author: James Helfrich
# Publication Year: 2012
# Subject: Computer Science
# 
# Introduction to C++ (2012) by James Helfrich
# Subject: Computer Science
# 
# Title: Click, Clack, Moo
# Author: Doreen Cronin
# Publication Year: 2000
# Illustrator: Betsy Lewin
# 
# Click, Clack, Moo (2000) by Doreen Cronin
# Illustrated by Betsy Lewin

# Book Class
#
#
class Book:
    def __init__(self):
        """
        Initialize the
        book class.
        """
        self.title = ""
        self.author = ""
        self.publication_yr = 0
 
    def prompt_book_info(self):
        """
        Prompts the user for
        book information.
        """
        self.title          = input("Title: ")
        self.author         = input("Author: ")
        self.publication_yr = input("Publication Year: ")
         
    def display_book_info(self):
        print("\n{} ({}) by {}".format(self.title, \
                                     self.publication_yr, \
                                     self.author))

# TextBook Class
#
#
class TextBook(Book):
                  
    def __init__(self):
        """
        Initialize the
        Textbook class
        inheriting from
        the Book class.
        """
        # First call the base class version
        super().__init__()              
        
        # Now define subject member variable
        self.subject = ""
                  
    def prompt_subject(self):
        """
        Prompt the user
        for the textbook
        subject.
        """
        self.subject = input("Subject: ")
                  
    def display_subject(self):
        """
        Display the subject
        of the Textbook.
        """

        print("Subject: {}\n".format(self.subject))
              
# PictureBook Class
#
#
class PictureBook(Book):
    
    def __init__(self):
        """
        Initialize the
        Picture book
        class inheriting
        from the book
        class.
        """
        # First call the base class version
        super().__init__()              
        
        # Now define illustrator member variable              
        self.illustrator = ""
              
    def prompt_illustrator(self):
        """
        Prompt the user
        for the illustrator
        of the Picture book.
        """
        self.illustrator = input("Illustrator: ")
              
    def display_illustrator(self):
        """
        Display the
        Picture book
        illustrator.
        """
        print("Illustrated by {}".format(self.illustrator))
              
def main():
    """
    Where the book program
    tasks are carried out.
    """
              
    # In main, first create a Book object and call the following methods:
    # 
    # prompt_book_info
    # 
    # display_book_info
    book = Book()
    book.prompt_book_info()
    book.display_book_info()
    print("")
    # Next, create a TextBook object and call the following methods:
    # 
    # prompt_book_info
    # 
    # prompt_subject
    # 
    # display_book_info
    # 
    # display_subject
    text_book = TextBook()
    text_book.prompt_book_info()
    text_book.prompt_subject()
    print(' ')
    text_book.display_book_info()
    text_book.display_subject()

    # Finally, create a PictureBook object and call the following methods:
    # 
    # prompt_book_info
    # 
    # prompt_illustrator
    # 
    # display_book_info
    # 
    # display_illustrator
    picture_book = PictureBook()
    picture_book.prompt_book_info()
    picture_book.prompt_illustrator()
    picture_book.display_book_info()
    picture_book.display_illustrator()
              
if __name__ == "__main__":
    main()