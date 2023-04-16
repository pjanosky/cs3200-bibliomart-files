from flask import Blueprint, request, jsonify, make_response, current_app
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
    cursor.execute('SELECT * FROM Textbooks JOIN Listings')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    txbks = cursor.fetchall()
    for row in txbks:
         json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


# /listings/get/{Title} - GET
# Gets listing with given isbn
@administrators.route('/listings/<ISBN>', methods=['GET'])
def get_listing(ISBN):
    cursor = db.get_db().cursor()
    cursor.execute("SELECT * FROM Listings WHERE ISBN = %s", (ISBN,))
    result = cursor.fetchall()
    cursor.close()
    db.get_db().close()
    if result:
        return jsonify(result)
    else:
        return jsonify({"message": "Listing not found"}), 404

# /listings/ - POST
# Adds a new listing for a given textbook
@administrators.route('/listings/', methods=['POST'])
def create_listing():
    current_app.logger.info('Processing Info')
    req_data = request.get_json()
    current_app.logger.info(req_data)

    listing_id = req_data['ListingId']
    quantity = req_data['Quantity']
    price = req_data['Price']
    employee_id = req_data['EmployeeId']
    shipper_name = req_data['ShipperName']
    isbn = req_data['ISBN']

    insrt_stmt = "INSERT INTO Listings (ListingId, Quantity, Price, EmployeeId, ShipperName, ISBN) \
        VALUES (%s, %s, %s, %s, %s, %s)"
    insrt_values = (listing_id, quantity, price, employee_id, shipper_name, isbn)

    current_app.logger.info('Insert statement: %s, Values: %s', insrt_stmt, insrt_values)

    cursor = db.get_db().cursor()
    try:
        cursor.execute(insrt_stmt, insrt_values)
        db.get_db().commit()
    except Exception as e:
        db.get_db().rollback()
        cursor.close()
        db.get_db().close()
        current_app.logger.error(f"Failed to insert listing: {e}")
        return jsonify({"message": "Failed to create listing"}), 500

    cursor.close()
    db.get_db().close()

    return jsonify({"message": "Listing created successfully"}), 201



# /listings/{listingId} - PUT
@administrators.route('/listings/<int:listingId>', methods=['PUT'])
def edit_listing(listingId):
    if request.content_type != 'application/json':
        return jsonify({"error": "Invalid Content-Type"}), 400
    
    req_data = request.get_json()
    quantity = req_data['Quantity']
    price = req_data['Price']
    employee_id = req_data['EmployeeId']
    shipper_name = req_data['ShipperName']
    isbn = req_data['ISBN']
    
    cursor = db.get_db().cursor()
    cursor.execute(
        "UPDATE Listings SET Quantity = %s, Price = %s, EmployeeId = %s, ShipperName = %s, ISBN = %s WHERE ListingId = %s",
        (quantity, price, employee_id, shipper_name, isbn, listingId)
    )
    db.get_db().commit()
    cursor.close()
    db.get_db().close()

    # return success message
    return jsonify({"message": "Listing updated successfully"})



# /listings/{listingId} - DELETE
# Removes a given listing
@administrators.route('/listings/delete/<listingId>', methods=['DELETE'])
def delete_listing(listingId):
    cursor = db.get_db().cursor()
    cursor.execute("DELETE FROM Listings WHERE ListingId = %s", (listingId,))
    rows_deleted = cursor.rowcount

    db.get_db().commit()
    cursor.close()
    db.get_db().close()

    if rows_deleted == 0:
        return jsonify({"message": f"Failed to delete listing {listingId}"})
    else:
        return jsonify({"message": f"Listing {listingId} deleted successfully"})



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




