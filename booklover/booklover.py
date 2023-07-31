import pandas as pd
class BookLover:
    
    #constructor:
    def __init__(self, name, email, fav_genre, num_books=0, book_list=pd.DataFrame({'book_name':[], 'book_rating':[]})):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = 0 if num_books is None else num_books 
        self.book_list = pd.DataFrame({'book_name':[], 'book_rating':[]}) if book_list  is None else book_list
    
    def add_book(self, book_name, book_rating):
        if book_name in str(self.book_list['book_name']):
            return 'This book has been added already'
        else:
            new_book = pd.DataFrame({
                'book_name': [book_name],
                'book_rating': [book_rating]
            })
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            return new_book
    
    def has_read(self, book_name):
        if book_name in str(self.book_list['book_name']):
            return True
        else:
            return False
        
    def num_books_read(self):
       return len(self.book_list['book_name'])
    
    def fav_books(self):
        sort = self.book_list.sort_values('book_rating', ascending = False)
        fav = sort[sort.book_rating > 3.0]
        return fav