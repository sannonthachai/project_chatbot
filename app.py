from flask import Flask
from flask_restful import Resource, Api
from database.mongoengine import MongoEngine
from flask_socketio import SocketIO
import setting

app = Flask(__name__)
api = Api(app)

mongoengine = MongoEngine(setting.MONGODB_NAME , setting.MONGODB_URI)
pmongoengine_conn = mongoengine.connector()

###################### Test ########################
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


##################### End Point ####################
api.add_resource(HelloWorld, '/')


if __name__ == '__main__':
    app.run(port=5000,  host='0.0.0.0')