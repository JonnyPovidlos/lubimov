import database
import os


def get_info_from_book(book_name):
    with open(book_name, 'r') as book:
        for line in book:
            info = line.split()
            book_info  = {
                'last_name': info[0],
                'first_name': info[1],
                'second_name': info[2],
                'series': info[3],
                'number': info[4],
                'date_of_issue': info[5],
                'obtaining': info[6],
                'issuing': info[7],
                'consent': info[8]
            }
            # print(book_info)
            database.insert_into_db('books.db', book_info)

if not os.path.exists(os.path.join(os.getcwd(), 'books.db')):
    database.create_db('books.db')

if not database.db_is_empty('books.db'):
    get_info_from_book('books_1')
    get_info_from_book('books_2')
    get_info_from_book('books_3')
    get_info_from_book('books_4')
    get_info_from_book('books_8')
    get_info_from_book('books_9')

while True:
    last_name = input('Введите фамилию: ')
    if last_name == 'exit':
        break
    info_result = database.get_line('books.db', last_name)
    for row in info_result:
        print(row)