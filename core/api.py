from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/api/query', methods=['GET'])
def query():
    query_parameters = request.args
    
    return None

if __name__ == '__main__':
    app.run(debug=True)