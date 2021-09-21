import requests
class Post:
    def __init__(self):
        self.url = "https://api.npoint.io/82975389c85afb34e389"
        connection = requests.get(self.url)
        connection.raise_for_status()
        self.data = connection.json()

    def return_dict(self,num):
        return  self.data[int(num)]

    def get_data(self):
        return self.data