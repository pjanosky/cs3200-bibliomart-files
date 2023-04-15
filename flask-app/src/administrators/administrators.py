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
@administrators.route('/textbooks', methods=['GET'])
def get_textbooks():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM Textbooks')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    txbks = cursor.fetchall()
    for row in txbks:
         json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


# /listings/{Title} - GET
# Gets listing with given isbn
@administrators.route('/listings/{ISBN}', methods=['GET'])
def get_listing(isbn):
    cursor = db.get_db().cursor()
    cursor.execute("SELECT * FROM Textbooks WHERE isbn = %s", (isbn,))
    result = cursor.fetchone()
    cursor.close()
    db.get_db().close()
    if result is not None:
        return jsonify(result)
    else:
        return jsonify({"message": "Listing not found"}), 404


# /listings/ - POST
# Adds a new listing for a given textbook
@administrators.route('/listings/', methods=['GET'])
def create_listing():
    cursor = db.get_db().cursor()
    cursor.execute(
        "INSERT INTO Listings (ListingId, Quantity, Price, EmployeeId, ShipperName, ISBN) VALUES (%s, %s, %s, %s, %s, %s)",
        (listing_id, quantity, price, employee_id, shipper_name, isbn)
    )
    db.get_db().commit()
    cursor.close()
    db.get_db().close()

    # return success message
    return jsonify({"message": "Listing added successfully"})



# /listings/{listingId} - PUT
# Updates attributes of listing 
@administrators.route('/listings/{listingId}', methods=['GET'])
def edit_listing():
    cursor = db.get_db().cursor()
    cursor.execute(
        "UPDATE Listings SET Quantity = %s, Price = %s, EmployeeId = %s, ShipperName = %s, ISBN = %s WHERE ListingId = %s",
        (quantity, price, employee_id, shipper_name, isbn, listing_id)
    )
    db.get_db().commit()
    cursor.close()
    db.get_db().close()

    # return success message
    return jsonify({"message": "Listing updated successfully"})




# /listings/{listingId} - DELETE
# Removes a given listing
@administrators.route('/listings/{listingId}', methods=['GET'])
def delete_listing(listing_id):
    cursor = db.get_db().cursor()
    cursor.execute("DELETE FROM Listings WHERE ListingId = %s", (listing_id,))
    db.get_db().commit()
    cursor.close()
    db.get_db().close()

    # return success message
    return jsonify({"message": f"Listing {listing_id} deleted successfully"})



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




