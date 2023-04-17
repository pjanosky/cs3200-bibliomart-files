from flask import Blueprint, request, jsonify, make_response, current_app
from pymysql import IntegrityError
from src import db


buyers = Blueprint('buyers', __name__)


# Textbooks Search Page

# Gets the textbooks matching 1 of three query parameters
# Joins with the listing ID for that textbook (null if no listing)
# author={name}
# title={tile}
@buyers.route('/textbooks/<isbn>', methods=['GET'])
def get_textbook(isbn):
    query = f'''SELECT T.ISBN, T.Title, T.Edition, T.YearPublished,
    GROUP_CONCAT(Concat(A.FirstName, ' ', A.LastName) SEPARATOR ', ') as Authors
    FROM Textbooks T
    LEFT OUTER JOIN AuthorDetails AD on T.ISBN = AD.ISBN
    LEFT OUTER JOIN Authors A on AD.AuthorId = A.AuthorId
    WHERE T.ISBN = '{isbn}'
    GROUP BY T.ISBN
    LIMIT 1;'''

    current_app.logger.info(query)
    cursor = db.get_db().cursor()
    cursor.execute(query)
    
    row_headers = [x[0] for x in cursor.description]
    the_data = cursor.fetchall()
    if len(the_data) != 1:
        return make_response(f'no textbook with isbn: {isbn}', 400)
    json_data = dict(zip(row_headers, the_data[0]))

    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Gets the textbooks matching 1 of three query parameters
# Joins with the listing ID for that textbook (null if no listing)
# author={name}
# title={tile}
@buyers.route('/textbooks', methods=['GET'])
def get_textbooks():
    conditions = ['TRUE']

    isbn = request.args.get('isbn')
    if isbn is not None:
        conditions.append(f"ISBN = '{isbn}'")

    author = request.args.get('author')
    if author is not None:
        conditions.append(f"Authors LIKE '%{author}%'")

    title = request.args.get('title')
    if title is not None:
        conditions.append(f"Title LIKE '%{title}%'")

    query = f'''SELECT * FROM
    (SELECT T.ISBN, T.Title, T.Edition, T.YearPublished,
    GROUP_CONCAT(Concat(A.FirstName, ' ', A.LastName) SEPARATOR ', ') as Authors
    FROM Textbooks T
    LEFT OUTER JOIN AuthorDetails AD on T.ISBN = AD.ISBN
    LEFT OUTER JOIN Authors A on AD.AuthorId = A.AuthorId
    GROUP BY T.ISBN) books
    WHERE {' AND '.join(conditions)}
    LIMIT 20;'''

    current_app.logger.info(query)
    cursor = db.get_db().cursor()
    cursor.execute(query)
    
    row_headers = [x[0] for x in cursor.description]
    the_data = cursor.fetchall()
    json_data = []
    for row in the_data:
        json_data.append(dict(zip(row_headers, row)))

    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


# /listings/{listingId} - GET
# Gets listing with given ISBN
@buyers.route('/listings', methods=['GET'])
def get_listings():
    conditions = ['TRUE']

    isbn = request.args.get('isbn')
    if isbn is not None:
        conditions.append(f"ISBN = '{isbn}'")

    query = f'''SELECT ListingId, ISBN
    FROM Listings
    WHERE {' AND '.join(conditions)}
    LIMIT 1;'''

    current_app.logger.info(query)
    cursor = db.get_db().cursor()
    cursor.execute(query)
    
    row_headers = [x[0] for x in cursor.description]
    the_data = cursor.fetchall()
    json_data = []
    for row in the_data:
        json_data.append(dict(zip(row_headers, row)))

    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response



# Listing Search Page
# /users - GET
# Get a list of all the user in the database to populate the user drop down
@buyers.route('/users', methods=['GET'])
def get_users():
    cursor = db.get_db().cursor()
    cursor.execute(f'''SELECT CONCAT(FirstName, ' ', LastName) 
            AS label, UserId AS value
            FROM Users;''')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    users = cursor.fetchall()
    for row in users:
         json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response



# /authors?isbn={isbn} - GET
# Returns details on each author the a given isbn
@buyers.route('/authors', methods=['GET'])
def get_author():
    conditions = ['True']
    isbn = request.args.get('isbn')
    if isbn is not None:
        conditions.append(f"T.ISBN = '{isbn}'")

    query = f"""SELECT FirstName, LastName, Bio FROM Authors
    JOIN AuthorDetails AD on Authors.AuthorId = AD.AuthorId
    JOIN Textbooks T on AD.ISBN = T.ISBN
    WHERE {' AND '.join(conditions)};"""

    current_app.logger.info(query)
    cursor = db.get_db().cursor()
    cursor.execute(query)
    
    row_headers = [x[0] for x in cursor.description]
    the_data = cursor.fetchall()
    json_data = []
    for row in the_data:
        json_data.append(dict(zip(row_headers, the_data[0])))
    
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


# /tags{isbn} - GET
# Gets all of the tags associated with the given book
@buyers.route('/tags', methods=['GET'])
def get_tags():
    conditions = ['TRUE']

    isbn = request.args.get('isbn')
    if isbn is not None:
        conditions.append(f"ISBN = '{isbn}'")

    query = f"SELECT * FROM Tags WHERE {' AND '.join(conditions)};"

    current_app.logger.info(query)
    cursor = db.get_db().cursor()
    cursor.execute(query)
    
    row_headers = [x[0] for x in cursor.description]
    the_data = cursor.fetchall()
    json_data = []
    for row in the_data:
        json_data.append(dict(zip(row_headers, row)))

    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response




# /purchases - POST
# Add a new purchase for a given user and listing
@buyers.route('/purchases', methods=['POST'])
def add_purchase():
    body_data = request.json
    user_id = body_data['user_id']
    listing_id = body_data['listing_id']
    street = body_data['street']
    city = body_data['city']
    state = body_data['state']
    zip = body_data['zip']
    purchase_quantity = body_data['quantity']

    # add the new purchase
    query = f'''INSERT INTO PurchaseInfo
    (UserId,ListingId,Street,City,State,Zip,PurchaseQuantity)
    VALUES ('{user_id}', '{listing_id}', '{street}', '{city}', '{state}', '{zip}', {purchase_quantity});'''

    current_app.logger.info(query)
    cursor = db.get_db().cursor()
    try:
        cursor.execute(query)
        db.get_db().commit()
    except IntegrityError as e:
        # return error if the textbook has already been purchased
        # or if the listing or use ids are invalid
        return make_response(str(e), 400)

    # decrement the number of textbooks in stock
    query = f'''UPDATE Listings 
    SET Quantity = Quantity - {purchase_quantity} 
    WHERE ListingId = '{listing_id}';'''

    current_app.logger.info(query)
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    return make_response('success', 200)



# /listings/{listingId} - GET
# Gets listing with the given listing ID
@buyers.route('/listings/<listing_id>', methods=['GET'])
def get_listing(listing_id):
    query = f'''SELECT ListingId, Quantity, Price, ISBN
    FROM Listings
    WHERE ListingId = '{listing_id}'
    LIMIT 1;'''

    current_app.logger.info(query)
    cursor = db.get_db().cursor()
    cursor.execute(query)
    
    row_headers = [x[0] for x in cursor.description]
    the_data = cursor.fetchall()
    if len(the_data) != 1:
        return make_response(f'invalid listing id: {listing_id}', 400)
    json_data = dict(zip(row_headers, the_data[0]))
    
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response




# /purchases/{UserId}/{ListingId} - PUT
# Changes destination of purchase
@buyers.route('/purchases/<UserId>/<ListingId>', methods=['PUT'])
def update_purchase_info(UserId, ListingId):
    req_data = request.json
    street = req_data['street']
    city = req_data['city']
    state = req_data['state']
    zip = req_data['zip']
    
    cursor = db.get_db().cursor()
    query = f"UPDATE PurchaseInfo SET Street = '{street}', City = '{city}', State = '{state}', Zip = '{zip}' WHERE UserId = '{UserId}' AND  ListingId = '{ListingId}' "
    current_app.logger.info(query)
    try: 
        cursor.execute(query)
        db.get_db().commit()
    except IntegrityError as e:
        return make_response(str(e), 400)

    return "Success"

# /purchases/{UserId}/{ListingId} - DELETE
# Cancels a purchase order by deleting it from the database

@buyers.route('/purchaseinfo/<UserId>/<ListingId>', methods = ['DELETE'])
def delete_purchase_info(UserId, ListingId):
    cursor = db.get_db().cursor()
    query = f"DELETE FROM PurchaseInfo WHERE UserId = '{UserId}' and ListingId = '{ListingId}'"
    current_app.logger.info(query)
    cursor.execute(query)

    try: 
        cursor.execute(query)
        db.get_db().commit()
    except IntegrityError as e:
        return make_response(str(e), 400)
    
    return "Success"

