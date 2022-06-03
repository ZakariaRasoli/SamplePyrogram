import sqlite3

class db:

    def __init__(self):
        self.db = sqlite3.connect('database.db') 
        self.cur = self.db.cursor()
    
    def create(self, table: str, values: list):
        ex = self.cur.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='%s' ''' %(table))
        if self.cur.fetchone()[0] == 1:
            self.drop(table)
        value = ''
        for i in values:
            if i == values[-1]:
                value += "%s" %(i)
            else:
                value += "%s, " %(i)
        return self.db.execute('''CREATE TABLE %s (%s)''' %(table, value))

    def insert(self, table: str, values: list):
        value = '('
        for i in values:
            if i == values[-1]:
                value += "'%s'" %(i)
            else:
                value += "'%s', " %(i)
        value += ')'
        self.cur.execute("INSERT INTO %s VALUES %s" %(table, value))
        self.db.commit()
        return True
    
    def select(self, query: str):
        self.cur.execute(query)
        result = []
        for row in self.cur.fetchall():
            result.append(row)
        return result
    
    def delete(self, table: str, row_id: int):
        self.cur.execute("DELETE FROM %s WHERE id=%s" %(table, str(row_id)))
        self.db.commit()
        return True

    def drop(self, table: str):
        self.cur.execute('''DROP TABLE %s''' %(table))
        self.db.commit()
        return True

    def update(self, table: str, id: int, sets: str):
        query = '''UPDATE %s SET %s WHERE id = %s ''' %(table, sets, str(id))
        self.cur.execute(query)
        self.db.commit()
        return True

    def __del__(self):
        return self.db.close()



    def insert_with_id(self, table: str, values: list):
        all = self.select('''SELECT * FROM %s''' %(table))
        id = len(all) + 1
        value = '(%s, ' %(id)
        for i in values:
            if i == values[-1]:
                value += "'%s'" %(i)
            else:
                value += "'%s', " %(i)
        value += ')'
        self.cur.execute("INSERT INTO %s VALUES %s" %(table, value))
        self.db.commit()
        return True

    def select_with_plug_name(self, plug_name: str):
        return self.select('''SELECT * FROM plugins WHERE plug_name='%s' ''' %(plug_name))



