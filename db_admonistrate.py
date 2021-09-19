from connection import connect

import psycopg2


class DateBaseA:
    def __init__(self):
        connection = psycopg2.connect(connect)
        self.cursor = connection.cursor()

    def read_quotes_in_table(self, quote_id):
        """Возвращает строку из таблицы QueBook"""
        self.cursor.execute(f'SELECT * FROM QuoBook WHERE QuoBook.Id = %s', (quote_id,))
        return self.cursor.fetchall()

    def write_new_quote_on_table(self, quot):
        """Записывает новую цитату в таблицу QueBook"""
        return self.cursor.execute('INSERT INTO QuoBook VALUES (%s, %s, %s)',
                                   (quot['Автор'], quot['Название произведения'], quot['Цитата']))

    def change_quote_in_table(self):
        pass

    def delete_quote(self):
        """Удаляет нужную строку из таблицы QueBook"""
        pass

    def count_id(self):
        """Выводит колличество строк в таблицу QuoBook"""
        self.cursor.execute("""SELECT COUNT(*) FROM QuoBook;""")
        return self.cursor.fetchone()[0]