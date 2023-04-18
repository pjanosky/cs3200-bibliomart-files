import random
from sqlite3 import IntegrityError
import string
from flask import Blueprint, request, jsonify, make_response, current_app 
from src import db


administrators = Blueprint('administrators', __name__)

# Listing Edit Page

# /textbooks - GET
# Get a list of textbooks and their associated listings
@administrators.route('/textbooks', methods=['GET'])
def get_textbooks():
    query = '''SELECT * FROM Textbooks LEFT OUTER JOIN Listings
    ON Textbooks.ISBN = Listings.ISBN;'''
    current_app.logger.info(query)

    cursor = db.get_db().cursor()
    cursor.execute(query)

    row_headers = [x[0] for x in cursor.description]
    json_data = []
    rows = cursor.fetchall()
    for row in rows:
         json_data.append(dict(zip(row_headers, row)))

    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


# /listings/{isbn} - GET
# Gets listing with given isbn
@administrators.route('/listings/<isbn>', methods=['GET'])
def get_listing(isbn):
    query = f'''SELECT * FROM Listings
    WHERE ISBN = '{isbn}'; '''
    current_app.logger.info(query)

    cursor = db.get_db().cursor()
    cursor.execute(query)

    row_headers = [x[0] for x in cursor.description]
    json_data = []
    results = cursor.fetchall()

    if len(results) == 0:
        error_msg = {'error': 'No listings found for this ISBN.'}
        the_response = make_response(jsonify(error_msg))
        the_response.status_code = 400
        return the_response

    for row in results:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


# /listings/ - POST
# Adds a new listing for a given textbook
@administrators.route('/listings/', methods=['POST'])
def make_listing():
    data = request.json
    listing_id = "".join(random.choice(string.ascii_letters + string.digits) for _ in range(10))
    quantity = data['Quantity']
    price = data['Price']
    employee_id = data['EmployeeId']
    shipper_name = data['ShipperName']
    isbn = data['ISBN']

    # add the new listing
    query = f'''INSERT INTO Listings
    (ListingId, Quantity, Price, EmployeeId, ShipperName, ISBN)
    VALUES ('{listing_id}', '{quantity}', '{price}', '{employee_id}', '{shipper_name or 'NULL'}', '{isbn}');'''
    current_app.logger.info(query)

    cursor = db.get_db().cursor()
    try:
        cursor.execute(query)
        db.get_db().commit()
        return jsonify({"message": "Listing created successfully"}, 200)
    except KeyError as e:
        # if a required field is missing from the JSON data
        return make_response(f"Missing field: {e}", 400)
    except IntegrityError as e:
        # if the listing or user ids are invalid
        db.get_db().rollback()
        return make_response(str(e), 400)
    except Exception as e:
        # for any other exception
        db.get_db().rollback()
        return make_response(str(e), 500)
    

# /listings/{listingId} - PUT
# Updates attributes of listing 
@administrators.route('/listings/<isbn>', methods=['PUT'])
def edit_listing(isbn):
    req_data = request.get_json()
    quantity = req_data.get('Quantity')
    price = req_data.get('Price')
    employee_id = req_data.get('EmployeeId')
    shipper_name = req_data.get('ShipperName')
    
    query = f'''UPDATE Listings
    SET Quantity = {quantity}, Price = {price}, EmployeeId = '{employee_id}', ShipperName = '{shipper_name}'
    WHERE ISBN = '{isbn}';'''
    current_app.logger.info(query)

    cursor = db.get_db().cursor()
    try:
        cursor.execute(query)
        db.get_db().commit()
    except IntegrityError as e:
        return jsonify({"message": f"Listing {isbn} not found"}, 400)

    # return success message
    return jsonify({"message": "Listing updated successfully"})



# /listings/{listingId} - DELETE
# Removes a given listing
@administrators.route('/listings/<isbn>', methods=['DELETE'])
def delete_listing(isbn):
    query = f"DELETE FROM Listings WHERE ISBN = '{isbn}';"
    current_app.logger.info(query)

    cursor = db.get_db().cursor()
    try: 
        cursor.execute(query)
        db.get_db().commit()
    except IntegrityError as e:
        return make_response(str(e), 400)
    
    return "Success"



# Reviews Edit Page

# /reviews/{UserId} - GET
#  Gets all reviews associated with a given user

@administrators.route('/UserReviews/<UserId>', methods = ['GET'])
def get_user_review(UserId):
    query = f'''select UserId, ReviewId, ReviewDate, Rating, ReviewComment
    FROM UserReviews
    WHERE UserId = '{UserId}';'''
    current_app.logger.info(query)

    cursor = db.get_db().cursor()
    cursor.execute(query)

    row_header = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_header, row)))
    
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response



# /reviews/{UserId}/{ReviewId} - GET
# Gets a selected review of the given user
@administrators.route('/UserReviews/<user_id>/<review_id>', methods = ['GET'])
def get_one_review(user_id, review_id):
    query = f'''select UserId, ReviewId, ReviewDate, Rating, ReviewComment
    FROM UserReviews
    WHERE UserId = '{user_id}' and ReviewId = '{review_id}';'''
    current_app.logger.info(query)

    cursor = db.get_db().cursor()
    cursor.execute(query)

    row_header = [x[0] for x in cursor.description]
    json_data = []
    the_data = cursor.fetchall()
    for row in the_data:
        json_data.append(dict(zip(row_header, row)))

    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# /reviews/{userId}/{reviewID} - DELETE
# Deletes a selected review
@administrators.route('/UserReviews/<user_id>/<review_id>', methods = ['DELETE'])
def delete_selected_review(user_id, review_id):
    query = f"DELETE FROM UserReviews WHERE UserId = '{user_id}' and ReviewId = '{review_id}';"
    current_app.logger.info(query)
    
    cursor = db.get_db().cursor()
    try: 
        cursor.execute(query)
        db.get_db().commit()
    except IntegrityError as e:
        return make_response(str(e), 400)
    
    return "Success"


# /reviews/{UserId} - POST
# Adds a new review for a given user
@administrators.route('/UserReviews/<user_id>', methods = ['POST']) 
def add_user_review(user_id):
    req_data = request.json
    review_id = "".join(random.choice(string.ascii_letters + string.digits) for _ in range(10))
    comment = req_data['Comment']
    rating = req_data['Rating']

    query = f'''INSERT INTO UserReviews (UserId, ReviewId, ReviewComment, Rating) 
    VALUES ('{user_id}', '{review_id}', '{comment}', {rating})'''
    current_app.logger.info(query)
    
    cursor = db.get_db().cursor()
    try: 
        cursor.execute(query)
        db.get_db().commit()
    except IntegrityError as e:
        return make_response(str(e), 400)
    return "Success"



# /reviews/{userId}/{reviewID} -PUT
# Updates a selected review
@administrators.route('/UserReviews/<user_id>/<review_id>', methods=['PUT'])
def update_review_info(user_id, review_id):
    req_data = request.json
    ReviewComment = req_data['ReviewComment']
    Rating = req_data['Rating']
    
    query = f'''UPDATE UserReviews
    SET ReviewComment = '{ReviewComment}', Rating = '{Rating}'
    WHERE UserId = '{user_id}' AND ReviewId = '{review_id}';'''
    current_app.logger.info(query)

    cursor = db.get_db().cursor()
    try: 
        cursor.execute(query)
        db.get_db().commit()
    except IntegrityError as e:
        return make_response(str(e), 400)

    return "Success"
 


# /users - GET
# Get a list of all users in the database
@administrators.route('/Users', methods=['GET'])
def get_users():
    query = f'''SELECT CONCAT(FirstName, ' ', LastName) as label, UserId as value
    FROM Users;'''
    current_app.logger.info(query)

    cursor = db.get_db().cursor()
    try: 
        cursor.execute(query)
        db.get_db().commit()
    except IntegrityError as e:
        return make_response(str(e), 400)

    row_header = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_header, row)))
        
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response



# /employees - GET
# get all of the employees in the database
@administrators.route('/employees', methods=['GET'])
def get_employees():
    query = f'''SELECT CONCAT(FirstName, ' ', LastName) as label, EmployeeId as value 
    FROM Employees;'''
    current_app.logger.info(query)

    cursor = db.get_db().cursor()
    try: 
        cursor.execute(query)
        db.get_db().commit()
    except IntegrityError as e:
        return make_response(str(e), 400)
    
    row_headers = [x[0] for x in cursor.description]
    the_data = cursor.fetchall()
    json_data = []
    for row in the_data:
        json_data.append(dict(zip(row_headers, row)))

    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


# /shippers - GET
# get all of the shippers in the database
@administrators.route('/shippers', methods=['GET'])
def get_shippers():
    query = f'SELECT ShipperName AS label, ShipperName AS value FROM Shippers;'
    current_app.logger.info(query)

    cursor = db.get_db().cursor()
    try: 
        cursor.execute(query)
        db.get_db().commit()
    except IntegrityError as e:
        return make_response(str(e), 400)
    
    row_headers = [x[0] for x in cursor.description]
    the_data = cursor.fetchall()
    json_data = []
    for row in the_data:
        json_data.append(dict(zip(row_headers, row)))

    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response
