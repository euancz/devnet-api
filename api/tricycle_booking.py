from flask import Flask, jsonify, request
 
tricycle_booking = Flask(__name__)
 
rides = [
    {"id": 1,"name": "Renejay", "pickup": "Mabiga", "dropoff": "Madapdap", "status": "Completed"},
    {"id": 2,"name": "Gilbert", "pickup": "Atlu Bola", "dropoff": "Dolores", "status": "Pending"},
    {"id": 3,"name": "Albert", "pickup": "Saudi", "dropoff": "Camachilles", "status": "Cancelled"},
    {"id": 4,"name": "Berto", "pickup": "Madapdap", "dropoff": "Bundagul", "status": "Completed"},
    {"id": 5,"name": "Jipre", "pickup": "Xevera", "dropoff": "Tabun", "status": "Pending"},
]
 
 ## Endpoint 1 
@tricycle_booking.route('/rides', methods=['GET'])
def get_rides():
    return jsonify(rides), 200

 ## endpoint 2
@tricycle_booking.route("/rides/<int:ride_id>", methods=["GET"])
def get_ride(ride_id):
    for ride in rides:
        if ride["id"] == ride_id:
            return jsonify(ride)

    return jsonify({"error": "Ride not found"}), 404




































 # endpoint 3

@tricycle_booking.route("/rides", methods=["POST"])
def book_ride():
    data = request.get_json(silent=True) or {}

    for field in ["name", "pickup", "dropoff"]:
        if not data.get(field):
            return jsonify({"error": "Missing required fields"}), 400

    new_booking = {
        "id": max([ride["id"] for ride in rides], default=0) + 1,
        "name": data["name"],
        "pickup": data["pickup"],
        "dropoff": data["dropoff"],
        "status": "Pending"
    }

    rides.append(new_booking)

    return jsonify(new_booking), 201

























 # endpoint 4
 
