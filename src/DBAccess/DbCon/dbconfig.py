import configparser
import os.path


#
#   This class for the conncetion to DataBase
#
class DBConfig:
    __dbname = 'postgres'
    __dbhost = '46.146.234.141'
    __dbuser = 'postgres'
    __dbport = 5432
    __dbpassword = 'passVVord#'

    __path_to_config = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/config/config.ini'

    #
    #   Return dict
    #
    @staticmethod
    def to_dict():
        db_dict = {
            'dbhost': DBConfig.__dbhost,
            'dbport': DBConfig.__dbport,
            'dbuser': DBConfig.__dbuser,
            'dbname': DBConfig.__dbname,
            'dbpassword': DBConfig.__dbpassword
        }

        return db_dict

    # 
    #   Load connection string from config file (DEV)
    #
    @staticmethod
    def load_from_config_dev():
        config = configparser.ConfigParser()
        config.read(DBConfig.__path_to_config)
        DBConfig.__dbname = config.get('dev_database', 'DbName')
        DBConfig.__dbhost = config.get('dev_database', 'DbHost')
        DBConfig.__dbuser = config.get('dev_database', 'DbUser')
        DBConfig.__dbpassword = config.get('dev_database', 'DbPassword')

    # 
    #   Load connection string from config file (PROD)
    #
    @staticmethod
    def load_from_config_prod():
        config = configparser.ConfigParser()
        config.read(DBConfig.__path_to_config)
        DBConfig.__dbname = config.get('prod_database', 'DbName')
        DBConfig.__dbhost = config.get('prod_database', 'DbHost')
        DBConfig.__dbuser = config.get('prod_database', 'DbUser')
        DBConfig.__dbpassword = config.get('prod_database', 'DbPassword')

    #
    #   Save connection string to config file
    #
    @staticmethod
    def apply(type):
        config = configparser.ConfigParser()
        if type == 'prod':
            config.add_section('prod_database')
            config.set('prod_database', 'DbName', DBConfig.__dbname)
            config.set('prod_database', 'DbHost', DBConfig.__dbhost)
            config.set('prod_database', 'DbUser', DBConfig.__dbuser)
            config.set('prod_database', 'DbPassword', DBConfig.__dbpassword)
        elif type == 'dev':
            config.add_section('dev_database')
            config.set('dev_database', 'DbName', DBConfig.__dbname)
            config.set('dev_database', 'DbHost', DBConfig.__dbhost)
            config.set('dev_database', 'DbUser', DBConfig.__dbuser)
            config.set('dev_database', 'DbPassword', DBConfig.__dbpassword)

        with open(DBConfig.__path_to_config, "w") as config_file:
            config.write(config_file) 


DBConfig.load_from_config_dev()
