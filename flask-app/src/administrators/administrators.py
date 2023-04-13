from flask import Blueprint, request, jsonify, make_response
import json
from src import db


administrators = Blueprint('administrators', __name__)

# This is an example route from the boilerplate project
# Get all customers from the DB
# @customers.route('/customers', methods=['GET'])
# def get_customers():
#     cursor = db.get_db().cursor()
#     cursor.execute('select company, last_name,\
#         first_name, job_title, business_phone from customers')
#     row_headers = [x[0] for x in cursor.description]
#     json_data = []
#     theData = cursor.fetchall()
#     for row in theData:
#         json_data.append(dict(zip(row_headers, row)))
#     the_response = make_response(jsonify(json_data))
#     the_response.status_code = 200
#     the_response.mimetype = 'application/json'
#     return the_response


# Listing Edit Page
# /textbooks - GET
# Get a list of textbooks and their associated listings





# /listings/{Title} - GET
# Gets listing with given ISBN





# /listings/ - POST
# Adds a new listing for a given textbook





# /listings/{listingId} - PUT
# Updates attributes of listing 





# /listings/{listingId} - DELETE
# Removes a given listing





# Reviews Edit Page
# /reviews/{userid} - GET
#  Gets all reviews associated with a given user




# /reviews/{userid}/{reviewID} - GET
# Gets the reviews about a user from a listing





# /reviews/{userid} - POST
# Adds a new review for a given user





# /reviews/{userId}/{reviewID} -DELETE
# Deletes a selected review





# /reviews/{userId}/{reviewID} -PUT
# Updates a selected review






# /users - GET
# Get a list of all users in the database




