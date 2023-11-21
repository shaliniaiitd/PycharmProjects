books = [{"title": 't1', "author": "a1", "publication_year": 1997},
         {"title": 't2', "author": "a2", "publication_year": 1998},
         {"title": 't2', "author": "a3", "publication_year": 1999}]


def search_title(book_dict, title):
    result = []
    for book in book_dict:
        if book["title"] == title:
            result.append(book)
    return result

print(search_title(books, 't2'))



