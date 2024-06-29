# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """
    # Included USER and PASS as parameters to prevent it being har
    def __init__(self, USER, PASS):
        # Initializing the MongoClient. This helps to
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        #USER = 'aacuser'
        #PASS = 'ABC321'
        HOST = 'localhost'
        PORT = 27017
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT)) # Starts connection
        self.database = self.client['%s' % (DB)] #Looks for database using DB variable - AAC
        self.collection = self.database['%s' % (COL)] # Looks for collection within the Database using the COL variable - animals
        print ("Successfully connected")

# Complete this create method to implement the C in CRUD.
    def create(self, doc): # defines create method passing the self and data
        # If the doc exists, try to insert into collection
        if doc:
            # Try to insert into collection and return true if able to
            try:
                self.collection.insert_one(doc)
                print("Document inserted: ", doc) # Print confirmation of document inserted
                return True

            # Return false and print error message if exception occurs
            except Exception as e:
                print(f"An Error has occurred: {e}")
                return False
        # Else, raise ValueError
        else:
            raise ValueError("Nothing to save, because data parameter is empty")

# Create method to implement the R in CRUD.
    def read(self, prompt):
        # Try to find document based on prompt and assign it to result variable
        try:
            result = self.collection.find(prompt)
            """if len(list(result))==0:
                print(f"No matches were found.")
            else:"""
            return list(result) # Return result as a list based on mongoDB query
        # Print error message if exception occurs, return empty dictionary.
        except Exception as e:
            print(f"An error has occurred: {e}")
            return []

# Update method to implement U in CRUD
    def update(self, query, newVals):
        if query and newVals is not None:
            # Call update_many function with query and new values
            try:
                updated_docs = self.collection.update_many(query, {"$set": newVals})
                # Check if there were any matches
                if updated_docs.modified_count == 0:
                    print(f"No matches found, nothing updated.")
                else:
                    # print(updated_docs.modified_count, " documents updated.") # Print the number of documents updated
                    return updated_docs.modified_count # return number of modified documents
            # Print error message if exception occurs
            except Exception as e:
                print(f"An error has occurred: {e}")
        # Otherwise, if query or newVals is empty, print error message
        else:
            raise ValueError("Unable to update, query or new values cannot be empty")



# Delete method to implement D in CRUD
    def delete(self, query):
        if query is not None:
            # Call delete_many function with query
            try:
                deleted_docs = self.collection.delete_many(query)
                # Check if there were any matches
                if deleted_docs.deleted_count == 0:
                    print(f"No matches found, nothing was deleted.")
                else:
                    return deleted_docs.deleted_count # Return number of deleted documents
                # Print error message if exception occurs
            except Exception as e:
                print(f"An error has occurred: {e}")
            # Otherwise, if query is empty, print error message
            else:
                raise ValueError("Unable to continue, query cannot be empty")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
