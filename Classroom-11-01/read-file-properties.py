#with open ('config.ini', 'w') as configfile:
#    config.write(configfile)


import configparser


config2 = configparser.ConfigParser()
config2.read('config.ini')

database= config2['DEFAULT'].get('database')
user = config2['DEFAULT'].get('user')
password = config2['DEFAULT'].get('password')

print(database)