import configparser


# This helps to read hardcoded value from the config.ini file 

config = configparser.RawConfigParser()
config.read("configurations/config.ini")

class readconfig:
    @staticmethod
    def getapplicationURL():
        url= config.get('Common info','baseURL')
        return url

    @staticmethod
    def getUsername():
        Username = config.get('Common info','username')
        return Username

    @staticmethod
    def getpassword():
        password = config.get('Common info','password')
        return password



    



