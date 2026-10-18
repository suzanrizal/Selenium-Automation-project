import configparser


# This helps to read hardcoded value from the config.ini file 

config = configparser.RawConfigParser()
config.read("Endpoint E-commerce Admin Demo\configurations\config.ini")

class readconfig:
    @staticmethod
    def getapplicationURL():
        url= config.get('common info','baseURL')
        return url

    @staticmethod
    def getUsername():
        Username = config.get('common info','username')
        return Username

    @staticmethod
    def getpassword():
        password = config.get('common info','password')
        return password



    



