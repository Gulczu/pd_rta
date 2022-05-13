
from flask import Flask
from flask_restful import Resource, Api
from flask import request, jsonify

app = Flask(__name__)
api = Api(app)

@app.route('/hello', methods=['GET'])
def hello():
    name = request.args.get('name', "")
    
    return f"<h1 style='color:red'>hello {name} </h1>"

@app.route('/')
@app.route('/index')
def home():
    return "aplikacja ze srodowiskiem produkcyjnym API"


class Main(Resource):
    def get(self):
        return jsonify("to jest tresc")

    
class Irys(Resource):
    def get(self):
        conn = engine.connect()
        query= conn.execute("select * from dane")
        result = {"dane": [i for i in query.cursor.fetchall()]}
        return jsonify(result)
    
api.add_resource(Main, '/test')
api.add_resource(Irys, '/irys')    

if __name__ == '__main__':
    app.run(port=5004)
