'''
Package Structure
-----------------
AirBnB_clone/
|_ __init__.py
|_ models/
	|_base_model.py, 
	|_ __init__.py, 
|_tests/
	|_test_base_model.py
	|_ __init__.py
    '''
'''
Write a class BaseModel that defines all common attributes/methods for other classes:
'''
# imports ->


# models/base_model.py


from datetime import datetime
from uuid import uuid4


class BaseModel(object):
    '''BaseModel Class'''
   
    def __init__(self):
        '''
        Public instance attributes:

                id = uuid.uuid4() # to generate unique id but don’t forget to convert to a string

                created_at: datetime - assign with the current datetime when an instance is created

                updated_at: datetime - assign with the current datetime when an instance is created 
        and it 	will be updated every time you change your object
        '''
        self.id = str(uuid4())
        # datetime.datetime(2017, 9, 28, 21, 5, 54, 119427)
        self.created_at = datetime.now()
        # datetime.datetime(2017, 9, 28, 21, 5, 54, 119434) (add++)
        self.updated_at = datetime.now()

    def __str__(self):
        '''
	    __str__: should print: [<class name>] (<self.id>) <self.__dict__>
        '''
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    
    '''
	Public instance methods:
    '''
    def save(self):
        '''
        save(self): updates the public instance attribute updated_at with the current 
        datetime
        '''
        self.updated_at = datetime.now()
		
    def to_dict(self):
        '''
		to_dict(self): returns a dictionary containing all keys/values of __dict__ of the 			
        instance:

			by using self.__dict__, only instance attributes set will be returned

			a key __class__ must be added to this dictionary with the class name of the 			
            object

			created_at and updated_at must be converted to string object in ISO format:
			format: %Y-%m-%dT%H:%M:%S.%f (ex: 2017-06-14T22:31:03.285259)

			you can use isoformat() of datetime object
            '''
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["update_at"] = self.updated_at.isoformat()
        return new_dict
        
        '''
                This method will be the first piece of the serialization/deserialization process: 		
        create a dictionary representation with “simple object type” of our BaseModel
        '''


'''
Final Output
Query->
'''
my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)
print()
my_model.save()
print(my_model)
print()
my_model_json = my_model.to_dict()
print(my_model_json)
print()
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

