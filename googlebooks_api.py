import requests
#class that connects to the Google Books API with methods for getting book data
class BookApi():
    #Retrieving volume information does not require authentication, so you do not have to provide the Authorization HTTP header with the GET request.
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
        authors = [volume.get('authors') for volume in volumes]
        ids =  [data["id"] for data in datas]
        dates =   [volume['publishedDate'] for volume in volumes]
        links = [volume['infoLink'] for volume in volumes]       
        return titles, authors, dates, links, ids
