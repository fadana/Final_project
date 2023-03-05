rom API_testing.Requests_folder.get_all_books import get_all_books
class TestGetBooks:
    def test_get_all_books_filter_by_type_non_fiction(self):
        response = get_all_books("non-fiction").json()
        assert len(response) == 3, f"Expected: 3, Actual: {len(response)}"
        for i in range(len(response)):
            assert response[i]["type"] == "non-fiction", f"Error: Book {response[i]['Just as I Am']} has an invalid type"
            self.test_get_all_books_filter_by_type_non_fiction('non-fiction', "Untamed")
            assert self.test_get_all_books_filter_by_type_non_fiction() ==1