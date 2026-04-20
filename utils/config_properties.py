import configparser

config = configparser.RawConfigParser()
config.read("./Configurations/commonDetails.ini")

class ReadConfig_CommonDetails():

    def getDevUrl(self):
        return config.get("Common Details", "dev_url")

    def getUsername(self):
        return config.get("Login Details", "username")

    def getPassword(self):
        return config.get("Login Details", "password")