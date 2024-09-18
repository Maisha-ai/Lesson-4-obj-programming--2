class library:
    def __init__(self,listofbooks,name):
        self.booklist=listofbooks
        self.name=name
        self.lenddict={}

    def display_books(self):
        print(f"We have the following books in our library:{self.name}")
        for book in self.booklist:
            print(book)

    def lendbook(self,user,book):
        if book not in self.booklist:
            print("Sorry We don't have that book")
        elif book in self.lenddict:
            print("Sorry the book is used by someone")
        else:
            self.lenddict[book]=user 
            print("Book data-base has been updated. You can take th book now")

    def addbook(self,book):
        self.booklist.append(book)
        print(f"{book} has been added to the booklist")

    def returnbook(self,book):
        if book in self.lenddict:
            del self.lenddict[book]
            print("Your book has been returned")
        else:
            print("The mentioned book hasn't been borrowed")

if __name__=='__main__':
    books=library(["Python", "Caraval", "Legendary", "Finale", "Game of thrones"],"Room of Fantasy")
    user_name=input("Welcome To out Library. Please enter your name:")
    while True:
        print(f"\n Hello{user_name}, Welcome to the {books.name}library. Please choose an option")
        print("1.Display books\n 2.Lend a Book \n 3.Add a Book \n 4.Return a Book \n 5.Quit")
        user_choice=input("Enter your choice to continue")
        if user_choice not in ["1","2","3","4","5"]:
            print("Please enter a valid option.")
            continue
        if user_choice=="1":
            books.display_books()
        elif user_choice=="2":
            book=input("Please enter the name of your desired book to lend")
            books.lendbook(user_name,book)
        elif user_choice=="3":
             book=input("Please enter the name of the book you want to add")
             books.addbook(book)
        elif user_choice=="4":
            book=input("Please enter the name of the book you want to return")
        elif user_choice=="5":
            print("Thanks for using the Library. Goodbye")
            break


        