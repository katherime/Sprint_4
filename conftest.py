import pytest
from main import BooksCollector

    #фикстура с готовым списком книг для использования в тестах
@pytest.fixture
def books_list():
    books_list = BooksCollector()
    books_list.add_new_book('Книга_1')
    books_list.set_book_genre('Книга_1', 'Фантастика')
    books_list.add_new_book('Книга_2')
    books_list.set_book_genre('Книга_2', 'Фантастика')
    books_list.add_new_book('Книга_3')
    books_list.set_book_genre('Книга_3', 'Ужасы')
    books_list.add_new_book('Книга_4')
    books_list.set_book_genre('Книга_4', 'Детективы')
    books_list.add_new_book('Книга_5')
    books_list.set_book_genre('Книга_5', 'Мультфильмы')
    books_list.add_new_book('Книга_6')
    books_list.set_book_genre('Книга_6', 'Комедии')
    books_list.add_new_book('Книга_7')
    books_list.set_book_genre('Книга_7', 'Не фантастика')
    return books_list

    #фикстура с списком книг и наличие списка избранных книг для использования в тестах
@pytest.fixture
def favorites_books_list():
    favorites_books_list = BooksCollector()
    favorites_books_list.add_new_book('Книга_1')
    favorites_books_list.set_book_genre('Книга_1', 'Фантастика')
    favorites_books_list.add_new_book('Книга_2')
    favorites_books_list.set_book_genre('Книга_2', 'Ужасы')
    favorites_books_list.add_book_in_favorites('Книга_1')
    return favorites_books_list
