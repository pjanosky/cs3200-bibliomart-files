import random
from sqlite3 import IntegrityError
import string
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

    #execute the querey
    cursor = db.get_db().cursor()
    cursor.execute(insert_stmt)
    db.get_db().commit()

    return "Success"


# /listings/{listingId} - DELETE
# Removes a given listing
@administrators.route('/Listings/<ListingId>', methods=['DELETE'])
def delete_listing(ListingId):
    cursor = db.get_db().cursor()
    query = f"DELETE FROM Listings WHERE ListingId = '{ListingId}'"
    current_app.logger.info(query)
    cursor.execute(query)

    try: 
        cursor.execute(query)
        db.get_db().commit()
    except IntegrityError as e:
        return make_response(str(e), 400)
    
    return "Success"


# Reviews Edit Page
# /reviews/{userid} - GET
#  Gets all reviews associated with a given user

@administrators.route('/UserReviews/<UserId>', methods = ['GET'])
def get_UserReviews(UserId):
    cursor = db.get_db().cursor()
    query = f"select UserId, ReviewId, ReviewDate, Rating, ReviewComment from UserReviews WHERE UserId = '{UserId}'"
    current_app.logger.info(query)
    cursor.execute(query)
    row_heaader = [x[0] for x in cursor.description]
    JSON_DATA = []
    theData = cursor.fetchall()
    for row in theData:
        JSON_DATA.append(dict(zip(row_heaader, row)))
    the_resposne = make_response(jsonify(JSON_DATA))
    the_resposne.status_code = 200
    the_resposne.mimetype = 'UserReviews/json'
    return the_resposne



# /reviews/{userid}/{reviewID} - GET
# Gets a selected review of the given user
@administrators.route('/UserReviews/<UserId>/<ReviewId>', methods = ['GET'])
def get_One_UserReview(UserId, ReviewId):
    cursor = db.get_db().cursor()
    query = f"select UserId, ReviewId, ReviewDate, Rating, ReviewComment from UserReviews WHERE UserId = '{UserId}' AND ReviewId = '{ReviewId}'"
    current_app.logger.info(query)
    cursor.execute(query)
    row_heaader = [x[0] for x in cursor.description]
    JSON_DATA = []
    theData = cursor.fetchall()
    for row in theData:
        JSON_DATA.append(dict(zip(row_heaader, row)))
    the_resposne = make_response(jsonify(JSON_DATA))
    the_resposne.status_code = 200
    the_resposne.mimetype = 'UserReviews/json'
    return the_resposne



# /reviews/{userId}/{reviewID} -DELETE
# Deletes a selected review
@administrators.route('/UserReviews/<UserId>/<ReviewId>', methods = ['DELETE'])
def delete_UserReviews(UserId, ReviewId):
    cursor = db.get_db().cursor()
    query = f"DELETE FROM UserReviews WHERE UserId = '{UserId}' and ReviewId = '{ReviewId}'"
    current_app.logger.info(query)
    cursor.execute(query)

    try: 
        cursor.execute(query)
        db.get_db().commit()
    except IntegrityError as e:
        return make_response(str(e), 400)
    
    return "Success"

# /reviews/{userid} - POST - DONE
# Adds a new review for a given user

@administrators.route('/UserReviews/<UserId>', methods = ['POST']) 
def post_UserReviews(UserId):

    req_data = request.json
    ReviewId = "".join(random.choice(string.ascii_letters + string.digits) for _ in range(10))
    comment = req_data['Comment']
    ReviewDate = req_data['ReviewDate']
    Rating = req_data['Rating']

    cursor = db.get_db().cursor()
    query = f"INSERT INTO UserReviews (UserId, ReviewId, ReviewComment, ReviewDate, Rating) VALUES ('{UserId}', '{ReviewId}', '{comment}', '{ReviewDate}', {Rating})"
    current_app.logger.info(query)

    try: 
        cursor.execute(query)
        db.get_db().commit()
    except IntegrityError as e:
        return make_response(str(e), 400)
    return "Success"



# /reviews/{userId}/{reviewID} -PUT - done
# Updates a selected review

@administrators.route('/UserReviews/<UserId>/<ReviewId>', methods=['PUT'])
def update_UserReviews(UserId, ReviewId):
    
    req_data = request.json
    ReviewComment = req_data['ReviewComment']
    ReviewDate = req_data['ReviewDate']
    Rating = req_data['Rating']
    
    cursor = db.get_db().cursor()
    query = f"UPDATE UserReviews SET ReviewComment = '{ReviewComment}', ReviewDate = '{ReviewDate}', Rating = '{Rating}' WHERE UserId = '{UserId}' AND  ReviewId = '{ReviewId}' "
    # Comment = %s, ReviewDate = %s, Rating = %s, WHERE UserId = %s AND ReviewId = %s", (Comment, ReviewDate, Rating, UserId, ReviewId)
    current_app.logger.info(query)
    
    try: 
        cursor.execute(query)
        db.get_db().commit()
    except IntegrityError as e:
        return make_response(str(e), 400)

    return "Success"
 


# /users - GET
# Get a list of all users in the database





