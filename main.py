def get_book_text(book_path):
    with open(book_path) as f:
        file_contents = f.read()
    print(file_contents)
    


get_book_text("/home/kylev/workspace/github.com/kylev/bookbot/books/frankenstein.txt")

