from flask import Blueprint, request, jsonify, make_response
import json
from src import db


buyers = Blueprint('buyers', __name__)

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


# Textbooks Search Page
# /textbooks/{isbn} - GET
# Gets the textbook with the given ISBN number



# Joins with the listing ID for that textbook (null if no listing)
# /textbooks - GET
# Gets the textbooks matching 1 of three query parameters
# author={id}
# title={title}
# author={name}




# Joins with the listing ID for that textbook (null if no listing)
# /listings/{listingId} - GET
# Gets listing with given ISBN





# Listing Search Page
# /users - GET
# Get a list of all the user in the database to popular the user drop down





# /authors/{id} - GET
# Returns details on the author and other book they wrote





# /tags{isbn} - GET
# Gets all of the tags associated with the given book





# /purchases - POST
# Add a new purchase for a given user and listing





# /purchases/{UserId}/{ListingId} - PUT
# Changes destination of purchase




# /purchases/{UserId}/{ListingId} - DELETE
# Cancels a purchase order by deleting it from the database



