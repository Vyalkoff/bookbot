BOOK_PATH = 'book/Чистый-Python.-Тонкости-программирования-для-профи-_-PDFDrive-_.txt'
PAGE_SIZE = 1050
book: dict[int, str] = {}


# Функция, возвращающая строку с текстом страницы и ее размер
def _get_part_text(text: str, start: int, size: int):
    marks = ',.!:;?'
    new_txt = text[start:start+size]
    if new_txt[-1] == '.':
        for i in text[start+size + 1:]:
            if i == '.':
                new_txt += i
            else:
                break

    if new_txt[-1] not in marks:
        for i in range(1, len(new_txt)):
            if new_txt[-1 - i] in marks:
                new_txt = new_txt[:- i]
                break
    return new_txt, len(new_txt)


# Функция, формирующая словарь книги
def prepare_book(path: str) -> None:
    with open(path, 'r') as file:
        text = file.read()
    start, page_number = 0, 1
    while start < len(text):
        page_text, page_size = _get_part_text(text, start, PAGE_SIZE)
        start += page_size
        book[page_number] = page_text.strip()
        page_number += 1


# Вызов функции prepare_book для подготовки книги из текстового файла
prepare_book(BOOK_PATH)


