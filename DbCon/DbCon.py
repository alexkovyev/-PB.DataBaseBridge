import configparser
from pathlib import Path

#
#   This class for the conncetion to DataBase
#
class dbconfig:
    __dbname = 'postgres'
    __dbhost = '46.146.234.141'
    __dbuser = 'postgres'
    __dbport = 5432
    __dbpassword = 'passVVord#'

    __path_to_config = Path("cfg/cfg.config")

    # 
    #   Load connection string from config file
    #
    @staticmethod
    def load_from_config():
        config = configparser.ConfigParser()
        config.read(dbconfig.__path_to_config)
        dbconfig.__dbname = config.get('DbConnection', 'DbName')
        dbconfig.__dbhost = config.get('DbConnection', 'DbHost')
        dbconfig.__dbuser = config.get('DbConnection', 'DbUser')
        dbconfig.__dbpassword = config.get('DbConnection', 'DbPassword')

        return (dbconfig.__dbhost, dbconfig.__dbport, dbconfig.__dbname, dbconfig.__dbuser, dbconfig.__dbpassword)

    #
    #   Save connection string to config file
    #
    @staticmethod
    def apply():
        config = configparser.ConfigParser()
        config.add_section('DbConnection')
        config.set('DbConnection', 'DbName', dbconfig.__dbname)
        config.set('DbConnection', 'DbHost', dbconfig.__dbhost)
        config.set('DbConnection', 'DbUser', dbconfig.__dbuser)
        config.set('DbConnection', 'DbPassword', dbconfig.__dbpassword)

        with open(dbconfig.__path_to_config, "w") as config_file:
            config.write(config_file)        



