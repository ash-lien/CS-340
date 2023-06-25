
from pymongo import MongoClient
from bson.objectid import ObjectId

  
class Animal_Shelter (object):
    #"""CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #\n",
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        USER = 'aacuser'
        PASS = 'SNHU1234'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 31070
        DB = 'AAC'
        COL = 'animals'
           
        # Initialize Connection
        
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client[(DB)]
        self.collection = self.database['%s' % (COL)]
        # Complete this create method to implement the C in CRUD
       
    def create(self, data):
            if data is not None:
                insert = self.database.animals.insert(data)  # data should be dictionary
                if insert!=0:
                    return True
                else:
                    return False    
            else:
                raise Exception("Nothing to save, because data parameter is empty.")
                
                # Complete this create method to implement the R in CRUD

    def read(self, criteria=None):
            if criteria is not None:
                data = self.database.animals.find(criteria,{"_id": False})
                for document in data:
                    print(document)
                
            else:
                data = self.database.animals.find({},{"_id": False})
            
            return data
       
       # Method U in CRUD
    def update(self, initial, change):
            if initial is not None:
                if self.database.animals.count_documents(initial, limit=1) != 0:
                    update_result = self.database.animals.update_many(initial, {"$set": change})
                    result = update_result.raw_result
                else:
                    result = ("Document not found.") 
                return result
            else: 
                  raise Exception("Nothing to update, because data parameter is empty")  
       
        # Method D in CRUD   
    def delete(self, remove):
            if remove is not None:
                if self.database.animals.count_documents(remove, limit=1) != 0:
                    delete_result = self.database.animals.delete_many(remove)
                    result = delete_result.raw_result
                else:
                    result = ("Document not found.") 
                    return result
            else: 
                  raise Exception("Nothing to delete, because data parameter is empty")  
                          
   
  
