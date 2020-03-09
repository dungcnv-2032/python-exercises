# Bookshop App
# (1) Allows clerks to enter a list of books (including titles and quantities – using a
# dictionary) that are available in his/her shop
# (2) Allows customers to check whether an item is in stock or not by inputting a title:
# just show “N items available” or “Out of stock!” on sc

books = {}

def input_book_name():
    name = input('Please input book name: ')
    if not name:
        print('name cannot empty')
        input_book_name()
    else:
       return name

def input_book_quantity():
    try:
        quantity = float(input('Please input book quantity: '))
        return quantity
    except:
        print('You need input book quantity is number!')
        input_book_quantity()

def check_book():
    name = input('Please input book name to check :')
    if name in books:
        print('%d items available' % books[name])
    else:
        print('Out of Stock!')

def input_book():
    name = input_book_name()
    books[name] = input_book_quantity()
    choose = float(input('Please input 1 to insert book, input 2 to check book in stock, input 3 to exit, choose: '))
    if choose == 1:
        input_book()
    elif choose == 2:
        check_book()
    elif choose == 3:
        print('Thank you !')
    else:
        print('Sorry, input invalid!')

input_book()