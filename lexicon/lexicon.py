LEXICON_RU = {'edit_bookmarks': '<b>Редактировать закладки</b>',
              '/start': '<b>Привет, читатель!</b>\n\nЭто бот, в котором ты можешь прочитать книгу Рэя Брэдбери "Марсианские хроники"\n\nЧтобы посмотреть список доступных команд - набери /help',
             }

LEXICON_EN = {'edit_bookmarks': '<b>Edit bookmarks</b>',
              '/start': "<b>Hello reader!</b>\n\nThis is a bot where you can read Ray Bradbury's The Martian Chronicles\n\nTo see a list of available commands, type /help",
             }


LEXICON: dict[str, str] = {
    'forward': '>>',
    'backward': '<<',
    '/start': '<b>Привет, читатель!</b>\n\nЭто бот, в котором '
              'ты можешь прочитать книгу Рэя Брэдбери "Марсианские '
              'хроники"\n\nЧтобы посмотреть список доступных '
              'команд - набери /help',
    '/help': '<b>Это бот-читалка</b>\n\nДоступные команды:\n\n/beginning - '
             'перейти в начало книги\n/continue - продолжить '
             'чтение\n/bookmarks - посмотреть список закладок\n/help - '
             'справка по работе бота\n\nЧтобы сохранить закладку - '
             'нажмите на кнопку с номером страницы\n\n<b>Приятного чтения!</b>',
    '/bookmarks': '<b>Это список ваших закладок:</b>',
    'edit_bookmarks': '<b>Редактировать закладки</b>',
    'edit_bookmarks_button': '❌ РЕДАКТИРОВАТЬ',
    'del': '❌',
    'cancel': 'ОТМЕНИТЬ',
    'no_bookmarks': 'У вас пока нет ни одной закладки.\n\nЧтобы '
                    'добавить страницу в закладки - во время чтения '
                    'книги нажмите на кнопку с номером этой '
                    'страницы\n\n/continue - продолжить чтение',
    'cancel_text': '/continue - продолжить чтение'}

LEXICON_COMMANDS: dict[str, str] = {
    '/beginning': 'В начало книги',
    '/continue': 'Продолжить чтение',
    '/bookmarks': 'Мои закладки',
    '/help': 'Справка по работе бота'
}