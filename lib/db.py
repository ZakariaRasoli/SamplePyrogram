import json, sqlite3
from clients import db_file

class db:

    def __init__(self):
        self.db = sqlite3.connect(db_file) 
        self.cur = self.db.cursor()
    
    def query(self, query: str):
        self.cur.execute(query)
        self.db.commit()
        return True

    def select(self, query: str):
        self.cur.execute(query)
        result = []
        for row in self.cur.fetchone():
            result.append(row)
        return result
    
    def create(self, table: str, values: list):
        self.cur.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='%s' ''' %(table))
        if self.cur.fetchone()[0] == 1:
            self.drop(table)
        value = ''
        for i in values:
            if i == values[-1]:
                value += "%s" %(i)
            else:
                value += "%s, " %(i)
        return self.db.execute('''CREATE TABLE %s (%s)''' %(table, value))

    def insert(self, table: str, column: str, values: str):
        return self.query("INSERT INTO %s (%s) VALUES (%s);" %(table, column, values))
        
    def delete(self, table: str, where: str):
        return self.query(f"DELETE FROM {table} WHERE {where};")

    def drop(self, table: str):
        return self.query(f'''DROP TABLE {table};''')

    def update(self, table: str, sets: str, where: str):
        query = f'''UPDATE {table} SET {sets} WHERE {where};'''
        return self.query(query)

    def __del__(self):
        return self.db.close()



    def insert_into_plugins(self, plug_name: str, plug_commands: json, plug_help: json, plug_status = None, update_from_id: int = None):
        return self.insert(
            'plugins', 
            'plug_name, plug_commands, plug_help, plug_status, update_from_id', 
            f"'{plug_name}', '{plug_commands}', '{plug_help}', '{plug_status}', '{update_from_id}'"
        )

    def update_by_plug_name(self, plug_name: str, sets: str):
        return self.update('plugins', sets, f"plug_name='{plug_name}'")

    def select_with_plug_name(self, plug_name: str):
        return self.select('''SELECT * FROM plugins WHERE plug_name='%s';''' %(plug_name))
