from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def read_root():
    return '''
        <h1>Hello!</h1>
        <p>Welcome you can access the next links</p>
        <ul>
            <li><a href="/hello">Hello</a></li>
            <li><a href="/books">Books</a></li>
            <li><a href="/songs">Songs</a></li>
            <li><a href="/movies">Movies</a></li>
        </ul>
    '''

@app.get("/hello", response_class=HTMLResponse)
def get_hello():
    return "<h1>Hello World!</h1>"

@app.get("/books", response_class=HTMLResponse)
def get_books_list():
    books = [
        '"The Great Gatsby" by F. Scott Fitzgerald',
        '"1984" by George Orwell',
        '"War and Peace" by Leo Tolstoy',
        '"Ready Player One" by Ernest Cline',
        '"The Catcher in the Rye" by J.D. Salinger',
    ]
    books_html = "<ul>" + "".join(f"<li>{book}</li>" for book in books) + "</ul>"
    return "<p>Books list:</p>" + books_html

@app.get("/songs", response_class=HTMLResponse)
def get_songs_list():
    songs = [
        '"Imagine" by John Lennon',
        '"Billie Jean" by Michael Jackson',
        '"Hotel California" by The Eagles',
        '"Bohemian Rhapsody" by Queen',
        '"Hey Jude" by The Beatles',
        '"Mr Brightside" by The Killers',
        '"Mr Blue Sky" by Electric Light Orchestra',
        '"Thriller" by Michael Jackson',
    ]
    songs_html = "<ul>" + "".join(f"<li>{song}</li>" for song in songs) + "</ul>"
    return "<p>Songs list:</p>" + songs_html

@app.get("/movies", response_class=HTMLResponse)
def get_movies_list():
    movies = [
        '"Pulp Fiction" (1994)',
        '"The Godfather" (1972)',
        '"The Dark Knight" (2008)',
        '"The Guardians of the Galaxy" (2014)',
        '"Logan" (2017)',
        '"The Truman Show" (1998)',
        '"The Matrix" (1999)',
        '"Once Upon a Time in Hollywood" (2019)"'
    ]
    movies_html = "<ul>" + "".join(f"<li>{movie}</li>" for movie in movies) + "</ul>"
    return "<p>Movies list:</p>" + movies_html