from project.bookstore import Bookstore
from unittest import TestCase, main


# from bookstore import Bookstore


class BookStoreTest(TestCase):
    BOOK_LIMIT = 5

    def setUp(self) -> None:
        self.book_store = Bookstore(self.BOOK_LIMIT)

    def test_book_total_sold(self):
        r = self.book_store.total_sold_books
        self.assertEqual(r, 0)

    def test_available_books_dict(self):
        r = self.book_store.availability_in_store_by_book_titles
        self.assertEqual(r, {})

    def test_book_limit(self):
        r = self.book_store.books_limit
        self.assertEqual(r, 5)

    def test_init(self):
        self.assertEqual(self.BOOK_LIMIT, self.book_store.books_limit)

    def test_book_store_limiter(self):
        self.store = Bookstore(10)
        self.assertEqual(self.store.books_limit, 10)

    def test_len_of_store_no_books(self):
        self.store = Bookstore(10)
        self.assertEqual(len(self.store), 0)

    def test_initialize_of_wrong_instance(self):
        with self.assertRaises(ValueError) as error:
            count = -100
            self.store = Bookstore(count)
        self.assertEqual(f"Books limit of {count} is not valid", str(error.exception))

    def test_len_of_store_with_books(self):
        self.store = Bookstore(10)
        self.store.receive_book('Test', 1)
        self.store.receive_book('Test2', 1)
        self.store.receive_book('Test3', 1)
        self.assertEqual(len(self.store), 3)

    def test_book_store_initialize_limit_zero_raises(self):
        with self.assertRaises(ValueError) as error:
            count = 0
            self.store = Bookstore(count)
        self.assertEqual(f"Books limit of {count} is not valid", str(error.exception))

    def test_book_store_initialize_limit_below_zero_raises(self):
        with self.assertRaises(ValueError) as error:
            count = -5
            self.store = Bookstore(count)
        self.assertEqual(f"Books limit of {count} is not valid", str(error.exception))

    def test_store_raises_when_book_limit_reached(self):
        with self.assertRaises(Exception) as error:
            self.book_store.receive_book('Test', 6)
        self.assertEqual("Books limit is reached. Cannot receive more books!", str(error.exception))

    def test_book_available_books_store(self):
        book = 'Test'
        count = 2
        self.book_store.receive_book(book, count)
        d = self.book_store.availability_in_store_by_book_titles
        cap = 0
        for v in d.values():
            cap += v
        self.assertEqual(2, cap)

    def test_book_sell_function(self):
        self.store = Bookstore(5)
        self.store.receive_book('Test', 3)
        self.store.sell_book('Test', 2)
        solds = self.store.total_sold_books
        available_books = self.store.availability_in_store_by_book_titles['Test']
        self.assertEqual(solds, 2)
        self.assertEqual(available_books, 1)

    def test_validate_correct_append_of_book_which_is_not_presented_in_store(self):
        name = 'Test4'
        count = 1
        self.book_store.receive_book(name, count)
        d = self.book_store.availability_in_store_by_book_titles
        a = [x for x in d.keys()]
        b = [x for x in d.values()]
        self.assertEqual(a[0], name)
        self.assertEqual(b[0], count)

    def test_store_returns_proper_result_when_receiving_books(self):
        self.store = Bookstore(5)
        copies = 2
        name = 'Test'
        result = self.store.receive_book(name, copies)
        self.assertEqual(f"{copies} copies of {name} are available in the bookstore.", result)

    def test_store_raises_when_selling_books_unavailable_books(self):
        name = 'Test2'
        with self.assertRaises(Exception) as error:
            self.book_store.sell_book(name, 2)
        self.assertEqual(f"Book {name} doesn't exist!", str(error.exception))

    def test_count_of_books_in_store(self):
        self.book_store.receive_book('Test', 1)
        self.book_store.receive_book('Test2', 1)
        self.book_store.receive_book('Test3', 1)
        length = len(self.book_store)
        self.assertEqual(length, 3)

    def test_store_counting_for_unwanted_length(self):
        self.book_store.receive_book('Test', 3)
        self.book_store.receive_book('Test2', 1)
        self.book_store.receive_book('Test3', 1)
        length = len(self.book_store)
        self.assertEqual(length, 5)


    def test_store_raises_when_selling_books(self):
        name = 'Test'
        self.book_store.receive_book(name, 2)

        with self.assertRaises(Exception) as error:
            self.book_store.sell_book(name, 3)
        self.assertEqual(f"{name} has not enough copies to sell. Left: 2", str(error.exception))

    def test_store_returns_proper_result_when_sells_books(self):
        self.book_store.receive_book('Test', 2)
        r = self.book_store.sell_book('Test', 1)
        self.assertEqual("Sold 1 copies of Test", r)

    def test_store_proper_sell_function_worker(self):
        with self.assertRaises(Exception) as error:
            self.book_store.receive_book('Test',10)
        self.assertEqual('Books limit is reached. Cannot receive more books!',str(error.exception))

    def test_store_returns_proper_result_when_sells_books_1(self):
        name = 'Test'
        self.book_store.receive_book('Test', 2)
        with self.assertRaises(Exception) as error:
            self.book_store.sell_book('Test', 3)
        r = self.book_store.sell_book('Test', 1)
        self.assertEqual(f"{name} has not enough copies to sell. Left: 2", str(error.exception))
        self.assertEqual("Sold 1 copies of Test", r)

    def test_str_returns_proper_result(self):
        self.book_store.receive_book('Test', 2)
        self.book_store.sell_book('Test', 1)
        self.book_store.sell_book('Test', 1)
        result = str(self.book_store)
        expected = '''Total sold books: 2
Current availability: 0
 - Test: 0 copies'''
        self.assertEqual(expected, result)

    def test_str_returns_empty(self):
        result = str(self.book_store)
        expected = '''Total sold books: 0
Current availability: 0'''
        self.assertEqual(expected, result)

    def test_str_returns_empty_1(self):
        result_1 = str(self.book_store)
        expected_1 = '''Total sold books: 0
Current availability: 0'''

        self.book_store.receive_book('Test', 2)
        self.book_store.sell_book('Test', 1)
        self.book_store.sell_book('Test', 1)
        result_2 = str(self.book_store)
        expected_2 = '''Total sold books: 2
Current availability: 0
 - Test: 0 copies'''

        self.assertEqual(expected_1, result_1)
        self.assertEqual(expected_2, result_2)


if __name__ == '__main__':
    main()
