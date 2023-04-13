Use Biblio;

INSERT INTO Textbooks(ISBN, YearPublished, Title, Edition, Summary, BookFormat, BookSubject, BookCondition)
VALUES ('053365406-8', 2020, 'suspendisse potenti cras in purus eu', 4, 'Duis bibendum. Morbi non quam nec dui luctus rutrum. Nulla tellus.

In sagittis dui vel nisl. Duis ac nibh. Fusce lacus purus, aliquet at, feugiat non, pretium quis, lectus.', 'hardcover',
        'engineering', 'terrible');
INSERT INTO Textbooks(ISBN, YearPublished, Title, Edition, Summary, BookFormat, BookSubject, BookCondition)
VALUES ('064742696-X', 2018, 'sollicitudin', 1,
        'Integer tincidunt ante vel ipsum. Praesent blandit lacinia erat. Vestibulum sed magna at nunc commodo placerat.',
        'paperback', 'anthropology', 'great');
INSERT INTO Textbooks(ISBN, YearPublished, Title, Edition, Summary, BookFormat, BookSubject, BookCondition)
VALUES ('734310323-7', 2019, 'vitae', 2,
        'Aliquam quis turpis eget elit sodales scelerisque. Mauris sit amet eros. Suspendisse accumsan tortor quis turpis.',
        'hardcover', 'business', 'great');
INSERT INTO Textbooks(ISBN, YearPublished, Title, Edition, Summary, BookFormat, BookSubject, BookCondition)
VALUES ('052149935-6', 2020, 'massa donec dapibus duis at', 4,
        'Proin eu mi. Nulla ac enim. In tempor, turpis nec euismod scelerisque, quam turpis adipiscing lorem, vitae mattis nibh ligula nec sem.',
        'paperback', 'anthropology', 'great');
INSERT INTO Textbooks(ISBN, YearPublished, Title, Edition, Summary, BookFormat, BookSubject, BookCondition)
VALUES ('421991988-0', 2020, 'ut suscipit a feugiat et eros', 3, 'Morbi porttitor lorem id ligula. Suspendisse ornare consequat lectus. In est risus, auctor sed, tristique in, tempus sit amet, sem.

Fusce consequat. Nulla nisl. Nunc nisl.

Duis bibendum, felis sed interdum venenatis, turpis enim blandit mi, in porttitor pede justo eu massa. Donec dapibus. Duis at velit eu est congue elementum.',
        'paperback', 'anthropology', 'terrible');
INSERT INTO Textbooks(ISBN, YearPublished, Title, Edition, Summary, BookFormat, BookSubject, BookCondition)
VALUES ('625938923-X', 2018, 'tortor sollicitudin', 1,
        'Praesent id massa id nisl venenatis lacinia. Aenean sit amet justo. Morbi ut odio.', 'hardcover',
        'anthropology', 'good');
INSERT INTO Textbooks(ISBN, YearPublished, Title, Edition, Summary, BookFormat, BookSubject, BookCondition)
VALUES ('773204739-7', 2020, 'nunc vestibulum ante ipsum primis', 3, 'Etiam vel augue. Vestibulum rutrum rutrum neque. Aenean auctor gravida sem.

Praesent id massa id nisl venenatis lacinia. Aenean sit amet justo. Morbi ut odio.

Cras mi pede, malesuada in, imperdiet et, commodo vulputate, justo. In blandit ultrices enim. Lorem ipsum dolor sit amet, consectetuer adipiscing elit.',
        'hardcover', 'anthropology', 'terrible');
INSERT INTO Textbooks(ISBN, YearPublished, Title, Edition, Summary, BookFormat, BookSubject, BookCondition)
VALUES ('911041658-7', 2019, 'ultrices phasellus id sapien in sapien iaculis', 1, 'Curabitur in libero ut massa volutpat convallis. Morbi odio odio, elementum eu, interdum eu, tincidunt in, leo. Maecenas pulvinar lobortis est.

Phasellus sit amet erat. Nulla tempus. Vivamus in felis eu sapien cursus vestibulum.

Proin eu mi. Nulla ac enim. In tempor, turpis nec euismod scelerisque, quam turpis adipiscing lorem, vitae mattis nibh ligula nec sem.',
        'hardcover', 'engineering', 'poor');
INSERT INTO Textbooks(ISBN, YearPublished, Title, Edition, Summary, BookFormat, BookSubject, BookCondition)
VALUES ('383115824-X', 2020, 'ante', 4,
        'In quis justo. Maecenas rhoncus aliquam lacus. Morbi quis tortor id nulla ultrices aliquet.', 'paperback',
        'anthropology', 'great');
INSERT INTO Textbooks(ISBN, YearPublished, Title, Edition, Summary, BookFormat, BookSubject, BookCondition)
VALUES ('543921061-X', 2020, 'et ultrices posuere', 1, 'In quis justo. Maecenas rhoncus aliquam lacus. Morbi quis tortor id nulla ultrices aliquet.

Maecenas leo odio, condimentum id, luctus nec, molestie sed, justo. Pellentesque viverra pede ac diam. Cras pellentesque volutpat dui.

Maecenas tristique, est et tempus semper, est quam pharetra magna, ac consequat metus sapien ut nunc. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Mauris viverra diam vitae quam. Suspendisse potenti.',
        'paperback', 'anthropology', 'terrible');

INSERT INTO Tags(ISBN, Tag)
VALUES ('383115824-X', 'beginner');
INSERT INTO Tags(ISBN, Tag)
VALUES ('625938923-X', 'beginner');
INSERT INTO Tags(ISBN, Tag)
VALUES ('421991988-0', 'advanced');
INSERT INTO Tags(ISBN, Tag)
VALUES ('064742696-X', 'advanced');
INSERT INTO Tags(ISBN, Tag)
VALUES ('773204739-7', 'beginner');

INSERT INTO Authors(AuthorID, FirstName, LastName, Bio)
VALUES ('Qd85I93Y79', 'Thorny', 'Cansdale',
        'Maecenas leo odio, condimentum id, luctus nec, molestie sed, justo. Pellentesque viverra pede ac diam. Cras pellentesque volutpat dui.');
INSERT INTO Authors(AuthorID, FirstName, LastName, Bio)
VALUES ('byt9Q8B961', 'Sherie', 'Bolle',
        'Quisque porta volutpat erat. Quisque erat eros, viverra eget, congue eget, semper rutrum, nulla. Nunc purus.');
INSERT INTO Authors(AuthorID, FirstName, LastName, Bio)
VALUES ('nuE7450RWc', 'Lexie', 'Mudge',
        'Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Vivamus vestibulum sagittis sapien. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.');
INSERT INTO Authors(AuthorID, FirstName, LastName, Bio)
VALUES ('5du1QYT6e6', 'Leena', 'Crocombe',
        'Morbi porttitor lorem id ligula. Suspendisse ornare consequat lectus. In est risus, auctor sed, tristique in, tempus sit amet, sem.');
INSERT INTO Authors(AuthorID, FirstName, LastName, Bio)
VALUES ('d3y290Dv47', 'Lishe', 'Dorken',
        'Mauris enim leo, rhoncus sed, vestibulum sit amet, cursus id, turpis. Integer aliquet, massa id lobortis convallis, tortor risus dapibus augue, vel accumsan tellus nisi eu orci. Mauris lacinia sapien quis libero.');

INSERT INTO AuthorDetails(AuthorId, ISBN)
VALUES ('nuE7450RWc', '053365406-8');
INSERT INTO AuthorDetails(AuthorId, ISBN)
VALUES ('Qd85I93Y79', '064742696-X');
INSERT INTO AuthorDetails(AuthorId, ISBN)
VALUES ('5du1QYT6e6', '734310323-7');
INSERT INTO AuthorDetails(AuthorId, ISBN)
VALUES ('d3y290Dv47', '052149935-6');
INSERT INTO AuthorDetails(AuthorId, ISBN)
VALUES ('byt9Q8B961', '421991988-0');
INSERT INTO AuthorDetails(AuthorId, ISBN)
VALUES ('nuE7450RWc', '625938923-X');
INSERT INTO AuthorDetails(AuthorId, ISBN)
VALUES ('Qd85I93Y79', '773204739-7');
INSERT INTO AuthorDetails(AuthorId, ISBN)
VALUES ('byt9Q8B961', '911041658-7');
INSERT INTO AuthorDetails(AuthorId, ISBN)
VALUES ('byt9Q8B961', '383115824-X');
INSERT INTO AuthorDetails(AuthorId, ISBN)
VALUES ('Qd85I93Y79', '543921061-X');

INSERT INTO Users(UserId, Email, FirstName, LastName, Street, City, State, Zip)
VALUES ('T803968849', 'sclose0@yellowbook.com', 'Shandeigh', 'Close', '035 Manley Hill', 'Dadiharja', 'MA', 05448);
INSERT INTO Users(UserId, Email, FirstName, LastName, Street, City, State, Zip)
VALUES ('E143555389', 'agoulden1@friendfeed.com', 'Adan', 'Goulden', '89332 Straubel Avenue', 'Nancaicun', 'CA',
        33938);
INSERT INTO Users(UserId, Email, FirstName, LastName, Street, City, State, Zip)
VALUES ('n929832943', 'emccahey2@blogtalkradio.com', 'Emmeline', 'McCahey', '67970 Heffernan Alley', 'Lewobelek', 'LA',
        33780);
INSERT INTO Users(UserId, Email, FirstName, LastName, Street, City, State, Zip)
VALUES ('O002020929', 'tdeetlof3@upenn.edu', 'Town', 'Deetlof', '1295 Monterey Crossing', 'Tulay na Lupa', 'ME',
        41631);
INSERT INTO Users(UserId, Email, FirstName, LastName, Street, City, State, Zip)
VALUES ('c130155857', 'wcrudgington4@comsenz.com', 'Woody', 'Crudgington', '74 Pierstorff Circle', 'Changlu', 'OR',
        95557);

INSERT INTO UserReviews(UserId, ReviewId, ReviewDate, Rating, ReviewComment)
VALUES ('c130155857', 'rC7739Cz06', '2022-12-19 14:16:51', 3,
        'ipsum aliquam non mauris morbi non lectus aliquam sit amet diam in magna bibendum');
INSERT INTO UserReviews(UserId, ReviewId, ReviewDate, Rating, ReviewComment)
VALUES ('O002020929', '483Jv83245', '2021-12-27 14:46:42', 7, NULL);
INSERT INTO UserReviews(UserId, ReviewId, ReviewDate, Rating, ReviewComment)
VALUES ('E143555389', 'W631rvL3fu', '2022-03-06 11:01:05', 2,
        'eget rutrum at lorem integer tincidunt ante vel ipsum praesent blandit lacinia erat vestibulum sed magna at nunc');
INSERT INTO UserReviews(UserId, ReviewId, ReviewDate, Rating, ReviewComment)
VALUES ('E143555389', 'f7YB78kma6', '2023-02-18 00:18:58', 8, NULL);
INSERT INTO UserReviews(UserId, ReviewId, ReviewDate, Rating, ReviewComment)
VALUES ('O002020929', '51Mf3K1K68', '2022-12-13 01:54:58', 6,
        'odio cras mi pede malesuada in imperdiet et commodo vulputate justo in');

INSERT INTO Employees(EmployeeId, FirstName, LastName, SSN, Title, YearlySalary)
VALUES ('Ofa738EhF0', 'Arney', 'Dennehy', '354624070', 'Assistant Media Planner', 67450);
INSERT INTO Employees(EmployeeId, FirstName, LastName, SSN, Title, YearlySalary)
VALUES ('8Y3Oi50jg3', 'Brandy', 'Janeway', '570495635', 'Research Associate', 99247);
INSERT INTO Employees(EmployeeId, FirstName, LastName, SSN, Title, YearlySalary)
VALUES ('px6u2FC89w', 'Don', 'Georges', '167138945', 'Budget/Accounting Analyst III', 92590);
INSERT INTO Employees(EmployeeId, FirstName, LastName, SSN, Title, YearlySalary)
VALUES ('z743t0g38c', 'Portie', 'Joseph', '885914551', 'Senior Editor', 73487);
INSERT INTO Employees(EmployeeId, FirstName, LastName, SSN, Title, YearlySalary)
VALUES ('y4K9p24e1Z', 'Doralia', 'Varnham', '816880291', 'Pharmacist', 74660);

INSERT INTO Shippers(ShipperName, PhoneNumber, ContactRep)
VALUES ('Fedex', 9068646915, 'Jude Sankey');
INSERT INTO Shippers(ShipperName, PhoneNumber, ContactRep)
VALUES ('UPS', 2378590378, 'Nonah Landeaux');
INSERT INTO Shippers(ShipperName, PhoneNumber, ContactRep)
VALUES ('USPS', 6987592438, 'Koral Keepence');

INSERT INTO Listings(ListingId, Quantity, Price, EmployeeId, ShipperName, ISBN)
VALUES ('kX9x74w685', 323, 23.23, 'px6u2FC89w', NULL, '053365406-8');
INSERT INTO Listings(ListingId, Quantity, Price, EmployeeId, ShipperName, ISBN)
VALUES ('vL33NNG01F', 28, 55.75, 'Ofa738EhF0', 'USPS', '064742696-X');
INSERT INTO Listings(ListingId, Quantity, Price, EmployeeId, ShipperName, ISBN)
VALUES ('03X0266VAb', 136, 82.04, '8Y3Oi50jg3', NULL, '734310323-7');
INSERT INTO Listings(ListingId, Quantity, Price, EmployeeId, ShipperName, ISBN)
VALUES ('556C80HB03', 337, 26.5, 'z743t0g38c', NULL, '052149935-6');
INSERT INTO Listings(ListingId, Quantity, Price, EmployeeId, ShipperName, ISBN)
VALUES ('47Qxl67822', 215, 71.2, 'px6u2FC89w', 'USPS', '421991988-0');

INSERT INTO Sales(SaleId, UserId, Street, City, State, Zip, Price, SaleDate, EmployeeId, ShipperName, ISBN,
                  FulfillmentDate)
VALUES ('0ZDPW51OXG', 'c130155857', '15717 Village Place', 'Prinza', 'MA', 81479, 31.99, '2021-03-10 02:32:46',
        'Ofa738EhF0',
        'UPS', '421991988-0', '2021-05-31 17:15:48');
INSERT INTO Sales(SaleId, UserId, Street, City, State, Zip, Price, SaleDate, EmployeeId, ShipperName, ISBN,
                  FulfillmentDate)
VALUES ('54jX58rJ7B', 'E143555389', '95 Riverside Court', 'Tebanah', 'MA', 89263, 88.79, '2020-10-31 12:04:42', NULL,
        NULL,
        '911041658-7', NULL);
INSERT INTO Sales(SaleId, UserId, Street, City, State, Zip, Price, SaleDate, EmployeeId, ShipperName, ISBN,
                  FulfillmentDate)
VALUES ('661CPVoHMZ', 'c130155857', '0578 Havey Drive', 'Las Flores', 'MA', 56443, 37.56, '2022-01-23 06:00:44', NULL,
        NULL,
        '911041658-7', NULL);
INSERT INTO Sales(SaleId, UserId, Street, City, State, Zip, Price, SaleDate, EmployeeId, ShipperName, ISBN,
                  FulfillmentDate)
VALUES ('fnW9MRC82l', 'E143555389', '94 Prairie Rose Alley', 'Bayang', 'SD', 99480, 47.76, '2022-09-02 07:42:37',
        '8Y3Oi50jg3', 'UPS', '383115824-X', '2021-02-12 23:04:10');
INSERT INTO Sales(SaleId, UserId, Street, City, State, Zip, Price, SaleDate, EmployeeId, ShipperName, ISBN,
                  FulfillmentDate)
VALUES ('3yHUf71j4K', 'n929832943', '0 Drewry Alley', 'Naranjo', 'VA', 62587, 112.1, '2021-06-17 09:46:28',
        'Ofa738EhF0',
        'Fedex', '052149935-6', '2022-09-13 10:44:53');

INSERT INTO RentalInfo(UserId, ListingId, Street, City, State, Zip, RentalStart, RentalEnd, FulfillmentDate)
VALUES ('c130155857', 'vL33NNG01F', '4 Buena Vista Plaza', 'Jersey City', 'NJ', 18234, '2020-11-25', '2023-01-11',
        '2023-01-13 00:40:07');
INSERT INTO RentalInfo(UserId, ListingId, Street, City, State, Zip, RentalStart, RentalEnd, FulfillmentDate)
VALUES ('E143555389', '47Qxl67822', '849 Oriole Drive', 'Chattanooga', 'TN', 73179, '2021-05-31', '2022-10-06',
        '2022-11-15 12:14:47');
INSERT INTO RentalInfo(UserId, ListingId, Street, City, State, Zip, RentalStart, RentalEnd, FulfillmentDate)
VALUES ('T803968849', 'vL33NNG01F', '6 Pennsylvania Pass', 'Bismarck', 'ND', 73464, '2021-04-05', '2023-02-27',
        '2023-01-31 03:49:23');
INSERT INTO RentalInfo(UserId, ListingId, Street, City, State, Zip, RentalStart, RentalEnd, FulfillmentDate)
VALUES ('c130155857', 'kX9x74w685', '773 Armistice Court', 'Memphis', 'TN', 50839, '2021-04-16', '2022-05-13',
        '2023-01-11 13:42:45');
INSERT INTO RentalInfo(UserId, ListingId, Street, City, State, Zip, RentalStart, RentalEnd, FulfillmentDate)
VALUES ('O002020929', '556C80HB03', '551 Bellgrove Trail', 'New York City', 'NY', 08340, '2021-08-18', '2022-07-08',
        '2022-11-26 18:35:46');


INSERT INTO PurchaseInfo(UserId, ListingId, Street, City, State, Zip, PurchaseDate, PurchaseQuantity, FulfillmentDate)
VALUES ('T803968849', '03X0266VAb', '0 Lunder Park', 'Garland', 'TX', 18327, '2022-12-29 21:41:24', 3,
        '2021-11-26 05:18:53');
INSERT INTO PurchaseInfo(UserId, ListingId, Street, City, State, Zip, PurchaseDate, PurchaseQuantity, FulfillmentDate)
VALUES ('c130155857', '47Qxl67822', '63 Bluestem Crossing', 'Los Angeles', 'CA', 86433, '2022-01-05 07:27:02', 2,
        '2022-09-10 20:27:08');
INSERT INTO PurchaseInfo(UserId, ListingId, Street, City, State, Zip, PurchaseDate, PurchaseQuantity, FulfillmentDate)
VALUES ('E143555389', '03X0266VAb', '32782 Londonderry Place', 'Pensacola', 'FL', 61673, '2021-12-26 04:37:55', 3,
        NULL);
INSERT INTO PurchaseInfo(UserId, ListingId, Street, City, State, Zip, PurchaseDate, PurchaseQuantity, FulfillmentDate)
VALUES ('c130155857', 'kX9x74w685', '46870 Ludington Trail', 'Sarasota', 'FL', 52585, '2021-12-24 21:29:09', 2, NULL);
INSERT INTO PurchaseInfo(UserId, ListingId, Street, City, State, Zip, PurchaseDate, PurchaseQuantity, FulfillmentDate)
VALUES ('T803968849', '556C80HB03', '99933 Florence Lane', 'Daytona Beach', 'FL', 16399, '2022-10-05 01:33:25', 1,
        '2021-08-21 01:46:00');