class Admins:
    def admins():
        ADMINS = []
        import configparser

        config = configparser.ConfigParser()
        config.read('config.ini')
        for i in config['admins']:
            ADMINS.append(int(config['admins'][i]))
        return ADMINS