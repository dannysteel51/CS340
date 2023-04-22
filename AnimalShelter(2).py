from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

        
    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        self.client = MongoClient('mongodb://%s:%s@localhost:46611/?authSource=AAC' % (username, password))
        #self.client = MongoClient('mongodb://%s:%s@localhost:46611/?authMechanism=DEFAULT&authSource=AAC'%(username,password)
        # where xxxx is your unique port number
        self.database = self.client['AAC']
                                
        
        
    # Create
    def create(self, data):
        if data is not None:
            self.database.animals.insert(data) # Data should be a dictionary
            return True
        else:
            raise Exception("Nothing to save due to parameter being empty")
            
            
    # Read
    def read(self, data):
        return self.database.animals.find(data) # Returns a single document as a python dictionary
    
    
    #Update
    def update(self, query, data):
        try:
            result = self.database.animals.update_many(query, {"$set": data})
            if result.modified_count > 0:
                return True
        except Exception as e:
            print(e)
        return False
    
    #Delete
    def delete(self, query):
        try:
            result = self.database.animals.delete_many(query)
            return result.raw_result
        except:
            return "MongoDB returned an error message"