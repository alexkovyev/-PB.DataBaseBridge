import configparser
import os.path

#
#   This class for the conncetion to DataBase
#
class dbconfig:
    __dbname = 'postgres'
    __dbhost = '46.146.234.141'
    __dbuser = 'postgres'
    __dbport = 5432
    __dbpassword = 'passVVord#'

    __path_to_config = os.path.abspath('..') + '/config/config.ini'

    #
    #   Return dict
    #
    @staticmethod
    def to_dict():
        dbDict = {}
        dbDict['dbhost'] = dbconfig.__dbhost
        dbDict['dbport'] = dbconfig.__dbport
        dbDict['dbuser'] = dbconfig.__dbuser
        dbDict['dbname'] = dbconfig.__dbname
        dbDict['dbpassword'] = dbconfig.__dbpassword

        return dbDict

    # 
    #   Load connection string from config file (DEV)
    #
    @staticmethod
    def load_from_config_dev():
        config = configparser.ConfigParser()
        config.read(dbconfig.__path_to_config)
        dbconfig.__dbname = config.get('dev_database', 'DbName')
        dbconfig.__dbhost = config.get('dev_database', 'DbHost')
        dbconfig.__dbuser = config.get('dev_database', 'DbUser')
        dbconfig.__dbpassword = config.get('dev_database', 'DbPassword')

    # 
    #   Load connection string from config file (PROD)
    #
    @staticmethod
    def load_from_config_prod():
        config = configparser.ConfigParser()
        config.read(dbconfig.__path_to_config)
        dbconfig.__dbname = config.get('prod_database', 'DbName')
        dbconfig.__dbhost = config.get('prod_database', 'DbHost')
        dbconfig.__dbuser = config.get('prod_database', 'DbUser')
        dbconfig.__dbpassword = config.get('prod_database', 'DbPassword')

    #
    #   Save connection string to config file
    #
    @staticmethod
    def apply(type):
        config = configparser.ConfigParser()
        if type == 'prod':
            config.add_section('prod_database')
            config.set('prod_database', 'DbName', dbconfig.__dbname)
            config.set('prod_database', 'DbHost', dbconfig.__dbhost)
            config.set('prod_database', 'DbUser', dbconfig.__dbuser)
            config.set('prod_database', 'DbPassword', dbconfig.__dbpassword)
        elif type == 'dev':
            config.add_section('dev_database')
            config.set('dev_database', 'DbName', dbconfig.__dbname)
            config.set('dev_database', 'DbHost', dbconfig.__dbhost)
            config.set('dev_database', 'DbUser', dbconfig.__dbuser)
            config.set('dev_database', 'DbPassword', dbconfig.__dbpassword)

        with open(dbconfig.__path_to_config, "w") as config_file:
            config.write(config_file) 

dbconfig.load_from_config_dev()
