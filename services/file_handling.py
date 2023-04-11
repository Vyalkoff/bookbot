BOOK_PATH = '/Users/vlad/BOT/bookbot/book/book_python.txt'
PAGE_SIZE = 1050
book: dict[int, str] = {}


# Функция, возвращающая строку с текстом страницы и ее размер
def _get_part_text(text: str, start: int, size: int):
    marks = ',.!:;?'
    new_txt = text[start:start + size]
    ln_size = 0
    if new_txt[-1] == '.' and new_txt[-2] in marks:
        for i in range(start + size - 2, 0, -1):
            if text[i] == ' ' and text[i - 1] in marks:
                break
            ln_size += 1

        return text[start:start + size - ln_size - 2], len(text[start:start + size - ln_size - 2])

    if new_txt[-1] not in marks:
        for i in range(1, len(new_txt)):
            if new_txt[-1 - i] in marks:
                new_txt = new_txt[:- i]
                break
    return new_txt, len(new_txt)


# Функция, формирующая словарь книги
def prepare_book(path: str) -> None:
    with open(path) as file:
        text = file.read()
        start, page_number = 0, 1
        while start < len(text):
            page_text, page_size = _get_part_text(text, start, PAGE_SIZE)
            start += page_size
            book[page_number] = page_text.strip()
            page_number += 1


# Вызов функции prepare_book для подготовки книги из текстового файла
prepare_book(BOOK_PATH)


