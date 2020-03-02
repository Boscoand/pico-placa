from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

DAY_RULES = {
    0: ['1', '2'],
    1: ['3', '4'],
    2: ['5', '6'],
    3: ['7', '8'],
    4: ['9', '0']
}

TIME_RANGES = [
    ['07:00', '09:30'],
    ['16:00', '19:30']
]

@app.route('/api/query', methods=['GET'])
def query():
    query_parameters = request.args
    
    license_plate = query_parameters.get('license_plate')
    date = query_parameters.get('date')
    time = query_parameters.get('time')
    
    latest_number = license_plate[-1]
    day = datetime.strptime(date, '%Y-%m-%d').weekday()

    response = {
        'available': True
    }

    if day > 4:
        return response

    else:
        if latest_number in DAY_RULES[day] and time_in_range(time):
            response['available'] = False
            
    return response

def time_in_range(time):
    """Return true if time is within the ranges defined in TIME_RANGES"""

    time = datetime.strptime(time, '%H:%M').time()

    for time_rules in TIME_RANGES: 

        start = datetime.strptime(time_rules[0], '%H:%M').time()
        end = datetime.strptime(time_rules[1], '%H:%M').time()
        
        if start <= time <= end:
            return True

    return False

if __name__ == '__main__':
    app.run(debug=True)