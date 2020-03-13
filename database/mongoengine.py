from mongoengine import connect

class MongoEngine:
    
    def __init__(self, db, host):
        self.connection = connect(db, host=host, authentication_source='admin')

    def connector(self):
        return self.connection
    
    def disconnector(self):
        return self.connection.close()