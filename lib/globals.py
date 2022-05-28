import configparser, os
from lib.db import db

class Global():
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')

    def admins(self):
        ADMINS = []
        
        for i in self.config['admins']:
            ADMINS.append(int(self.config['admins'][i]))
        return ADMINS

    def prefixes(self):
        return ['.', '', '!', '#']

    def get_command(self, file):
        plug_name = os.path.basename(file).split('.', 1)[0]
        return [db().select_with_plug_name(plug_name)[0][2]]

    def get_size(self, bytes, suffix="B"):
        factor = 1024
        for unit in ["", "K", "M", "G", "T", "P"]:
            if bytes < factor:
                return f"{bytes:.2f}{unit}{suffix}"
            bytes /= factor



