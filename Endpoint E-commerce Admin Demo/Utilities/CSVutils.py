import csv

class CSVfiles:

    def get_login_data():
            with open("TestData/Login_test_data.csv", "r", newline="") as file:
                reader = csv.DictReader(file)
    
                data = []
                for row in reader:
                    data.append((
                        row["username"],
                        row["password"],
                        row["exp"]
                    ))
    
                return data