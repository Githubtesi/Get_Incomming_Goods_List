import configparser
import os

FILE_NAME = "config.ini"
PAIRENT_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(PAIRENT_DIR, FILE_NAME)

config = configparser.ConfigParser()
# config.read("config.ini")
config.read(filenames=FILE_PATH, encoding="utf-8")

ID = config['ACCOUNT']['ID']
PASS = config['ACCOUNT']['PASS']
