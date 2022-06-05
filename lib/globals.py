import configparser, os
import json
from lib.db import db

class Global:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')

    def admins(self):
        ADMINS = []
        
        for i in self.config['admins']:
            ADMINS.append(int(self.config['admins'][i]))
        return ADMINS

    def prefixes(self):
        return ['.', '!', '#']

    def helperID(self):
        return self.config['helper']['id']

    def get_commands(self, file):
        plug_name = os.path.basename(file).split('.', 1)[0]
        js = json.loads(db().select_with_plug_name(plug_name)[2])
        result = []
        for key in js.keys():
            result.append(js[key])
        return result

PREFIXES = Global().prefixes()
ADMINS = Global().admins()
HelperID = Global().helperID()
