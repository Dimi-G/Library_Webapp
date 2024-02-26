import requests
from pprint import pprint

#Retrieving volume information does not require authentication, so you do not have to provide the Authorization HTTP header with the GET request.

#class that connects to the Google Books API with methods for getting book data
class BookApi():
    def __init__(self):
        self.URL="https://www.googleapis.com/books/v1/volumes"
    
    def find_books(self, book_title):
        parameters = {
            "q" : book_title,
            "orderBy" : "relevance",
            "langRestrict" : "en"
        }
        response = requests.get(self.URL, params= parameters)
        response.raise_for_status()
        datas = response.json()["items"]   
        volumes = [data["volumeInfo"] for data in datas]
        titles = [volume['title'] for volume in volumes]
        #due to potential errors if the key 'authors' is not present in a particular dictionary, we are using the get method, which allows to provide a default value (in this case, an empty list []) 
        authors = [volume.get('authors', []) for volume in volumes]
        ids =  [data["id"] for data in datas]         
        return volumes, titles, authors, ids
    
    def find_by_id(self, id):
        url=f"https://www.googleapis.com/books/v1/volumes/{id}"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        image_link = data['volumeInfo']['imageLinks']['large']
        return image_link


# book_api =BookApi()
# results=book_api.find_by_id("V_A4EAAAQBAJ")
# # volumes = [result["volumeInfo"] for result in results]
# # titles = [volume['title'] for volume in volumes]
# pprint(results)