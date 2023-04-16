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





# /listings/{Title} - GET
# Gets listing with given ISBN





# /listings/ - POST
# Adds a new listing for a given textbook





# /listings/{listingId} - PUT
# Updates attributes of listing 
@administrators.route('/Listings/<ListingId>')
def update_listing(ListingID):
    # access json data from requeted object
    current_app.logger.info('Processing form data')
    req_data = request.get_json()
    current_app.logger.info(req_data)
  
    ListingId = req_data['ListingId']
    Quantity = req_data['Quantity']
    Price = req_data['Price']
    EmployeeId = req_data['EmployeeId']
    ShipperName = req_data['ShipperName']
    ISBN = req_data ['ISBN']
    

    # construct the insert statement
    insert_stmt = 'INSERT INTO Listings WHERE ListingId = ListingID (Quantity, Price, EmployeeId, ShipperName, ISBN) VALUES ("'
    insert_stmt += ListingId + '","' + Quantity + '","' + Price + '","' + EmployeeId + '","' + ShipperName + '",' + ISBN + ')'

    current_app.logger.info(insert_stmt)

    #execute the querey
    cursor = db.get_db().cursor()
    cursor.execute(insert_stmt)
    db.get_db().commit()

    return "Success"


# /listings/{listingId} - DELETE
# Removes a given listing
@administrators.route('/Listings/<ListingId>')
def delete_listing(ListingId):
     # access json data from requeted object
    current_app.logger.info('Processing form data')
    req_data = request.get_json()
    current_app.logger.info(req_data)

    ListingId = req_data['ListingID']
    Quantity = req_data['Quantity']
    Price = req_data['Price']
    EmployeeId = req_data['EmployeeId']
    ShipperName = req_data['ShipperName']
    ISBN = req_data ['ISBN']
    

    # construct the insert statement
    insert_stmt = 'DELETE FROM Listings (ListingId, Quantity, Price, EmployeeId, ShipperName, ISBN) VALUES ("'
    insert_stmt += ListingId + '","' + Quantity + '","' + Price + '","' + EmployeeId + '","' + ShipperName + '",' + ISBN + ')'

    current_app.logger.info(insert_stmt)

    #execute the querey
    cursor = db.get_db().cursor()
    cursor.execute(insert_stmt)
    db.get_db().commit()

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
    UserId = req_data['UserId']
    ReviewId = req_data['ReviewId']
    comment = req_data['Comment']
    ReviewDate = req_data['ReviewDate']
    Rating = req_data['Rating']

    cursor = db.get_db().cursor()
    query = f"INSERT INTO UserReviews (UserId, ReviewId, ReviewComment, ReviewDate, Rating) VALUES (UserId, ReviewId, '{comment}', '{ReviewDate}', {Rating})"
    current_app.logger.info(query)

    try: 
        cursor.execute(query)
        db.get_db().commit()
    except IntegrityError as e:
        return make_response(str(e), 400)
    
    return "Success"




# /users - GET
# Get a list of all users in the database





