import pytest
from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    # тестирование добавления новой книги
    @pytest.mark.parametrize('book_name', (("Мастер и Маргарита"), ("Гарри Поттер")))
    def test_add_new_book_with_right_lenght(self, book_name):
        books = BooksCollector()
        books.add_new_book(book_name)
        assert book_name in books.books_genre

    @pytest.mark.parametrize('book_name', (("numbernumbernumbernumbernumbernumbernumber"), (""),))
    def test_add_new_book_with_wrong_lenght(self, book_name):
        books = BooksCollector()
        books.add_new_book(book_name)
        assert book_name not in books.books_genre

    def test_add_new_book_when_book_already_added(self):
        books = BooksCollector()
        books.add_new_book('Книга')
        books.add_new_book('Книга')
        assert len(books.books_genre) == 1

    # тестирование установки жанра книги
    @pytest.mark.parametrize("book_name, book_genre", (('Книга', 'Фантастика'),
                                                       ("Книга", 'Ужасы')))
    def test_set_book_genre_with_right_genre(self, book_name, book_genre):
        books = BooksCollector()
        books.add_new_book(book_name)
        books.set_book_genre(book_name, book_genre)
        assert books.books_genre[book_name] == book_genre

    @pytest.mark.parametrize("book_name, book_genre", (('Книга', 'Другое'),
                                                       ("Книга", '12345'),
                                                       ("Книга", ' ')))
    def test_set_book_genre_with_wrong_genre(self, book_name, book_genre):
        books = BooksCollector()
        books.add_new_book(book_name)
        books.set_book_genre(book_name, book_genre)
        assert books.books_genre[book_name] != book_genre

    # тестирование получения жанра книги по её имени
    @pytest.mark.parametrize('name, genre', (('Книга', 'Фантастика'),
                                             ("Книга", 'Детективы')))
    def test_get_book_genre_book_with_genre_in_list(self, name, genre):
        books = BooksCollector()
        books.add_new_book(name)
        books.set_book_genre(name, genre)
        assert books.get_book_genre(name) == genre

    @pytest.mark.parametrize('name, genre', (('Книга', 'Другое'),
                                             ("", 'Не ужасы')))
    def test_get_book_genre_book_with_genre_not_in_list(self, name, genre):
        books = BooksCollector()
        books.add_new_book(name)
        books.set_book_genre(name, genre)
        assert books.get_book_genre(name) != genre

    # тестирование вывода списка книг с определённым жанром

    def test_get_books_with_specific_genre(self, books_list):
        filtered_books = books_list.get_books_with_specific_genre(books_list.books_genre['Книга_1'])
        assert len(filtered_books) == 2 and all(book in filtered_books for book in ['Книга_1', 'Книга_2'])

    # тестирование вывода словаря books_genre

    def test_get_books_genre(self, favorites_books_list):
        dict_books = favorites_books_list.get_books_genre()
        assert len(dict_books) == 2 and all(book in dict_books for book in ['Книга_1', 'Книга_2'])

    # тестирование вывода книг, подходящим детям
    def test_get_books_for_children(self, books_list):
        child_books = books_list.get_books_for_children()
        assert len(child_books) == 4 and all(book in child_books for book in ['Книга_1', 'Книга_2',
                                                                              'Книга_5', 'Книга_6'])

    # тестирование добавления книги в Избранное
    @pytest.mark.parametrize('name', (('Книга_1'), ("Книга_2")))
    def test_add_book_in_favorites_for_new_book(self, name):
        books = BooksCollector()
        books.add_new_book(name)
        books.add_book_in_favorites(name)
        assert name in books.favorites

    # тестирование добавления книги в Избранное, которая уже добавлена
    def test_add_book_in_favorites_book_already_in_list(self):
        books = BooksCollector()
        name_book = 'Книга'
        books.add_new_book(name_book)
        books.add_book_in_favorites(name_book)
        books.add_book_in_favorites(name_book)
        assert books.favorites.count(name_book) == 1

    # тестирование удаление книги из Избранного
    def test_delete_book_from_favorites_when_book_in_list(self, favorites_books_list):
        favorites_books_list.delete_book_from_favorites('Книга_1')
        assert 'Книга_1' not in favorites_books_list.favorites

    def test_delete_book_from_favorites_when_book_not_in_list(self, favorites_books_list):
        favorites_books_list.delete_book_from_favorites('Книга_4')
        assert len(favorites_books_list.favorites) == 1

    # тестирование получения списка Избранных книг
    def test_get_list_of_favorites_books(self, favorites_books_list):
        favourite_books = favorites_books_list.get_list_of_favorites_books()
        assert len(favourite_books) == 1 and 'Книга_1' in favourite_books
