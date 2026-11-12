from flask import Flask, jsonify, request
 
tricycle_booking = Flask(__name__)
 
rides = [
    {"id": 1,"name": "Renejay", "pickup": "Mabiga", "dropoff": "Madapdap", "status": "Completed"},
    {"id": 2,"name": "Gilbert", "pickup": "Atlu Bola", "dropoff": "Dolores", "status": "Pending"},
    {"id": 3,"name": "Albert", "pickup": "Saudi", "dropoff": "Camachilles", "status": "Cancelled"},
    {"id": 4,"name": "Berto", "pickup": "Madapdap", "dropoff": "Bundagul", "status": "Completed"},
    {"id": 5,"name": "Jipre", "pickup": "Xevera", "dropoff": "Tabun", "status": "Pending"},
]
 
 
 
