DROP DATABASE Biblio; -- USED TO CREATE DATABASE FROM SCRATCH FOR TESTING


CREATE DATABASE Biblio;
USE Biblio;


CREATE TABLE Textbooks
(
   ISBN          VARCHAR(13) PRIMARY KEY,
   YearPublished YEAR         NOT NULL,
   Title         VARCHAR(500) NOT NULL,
   Edition       INT          NOT NULL,
   Summary       VARCHAR(500) NOT NULL,
   BookFormat    VARCHAR(100) NOT NULL,
   BookSubject   VARCHAR(100) NOT NULL,
   BoomCondition VARCHAR(100) NOT NULL
);


CREATE TABLE Tags
(
   Tag  VARCHAR(100) NOT NULL,
   ISBN VARCHAR(13)  NOT NULL UNIQUE,


   PRIMARY KEY (Tag, ISBN),


   FOREIGN KEY (ISBN) REFERENCES Textbooks (ISBN)
);


CREATE TABLE Authors
(
   AuthorId  CHAR(10) PRIMARY KEY,
   FirstName VARCHAR(100) NOT NULL,
   LastName  VARCHAR(100) NOT NULL,
   Bio       Varchar(500) NOT NULL
);


CREATE TABLE AuthorDetails
(
   AuthorId VARCHAR(50) NOT NULL,
   ISBN     VARCHAR(13) NOT NULL,


   PRIMARY KEY (AuthorId, ISBN),


   FOREIGN KEY (AuthorId) REFERENCES Authors (AuthorId),
   FOREIGN KEY (ISBN) REFERENCES Textbooks (ISBN)
);






CREATE TABLE Users
(
   UserId    CHAR(10) PRIMARY KEY,
   Email     VARCHAR(100) UNIQUE,
   FirstName VARCHAR(100) NOT NULL,
   LastName  VARCHAR(100) NOT NULL,
   Street    VARCHAR(100) NOT NULL,
   City      VARCHAR(100) NOT NULL,
   State     CHAR(2)      NOT NULL,
   Zip       CHAR(5)      NOT NULL
);


CREATE TABLE UserReviews
(
   UserId   CHAR(10)     NOT NULL,
   ReviewId CHAR(10)     NOT NULL,
   Date     DATE         NOT NULL,
   Rating   INT          NOT NULL,
   Comment  VARCHAR(500),


   PRIMARY KEY (UserId, ReviewId),


   FOREIGN KEY (UserId) REFERENCES Users (UserId)
);




CREATE TABLE Employees
(
   EmployeeId CHAR(10) PRIMARY KEY,
   FirstName  VARCHAR(100) NOT NULL,
   LastName   VARCHAR(100) NOT NULL,
   SSN        CHAR(9)      NOT NULL UNIQUE,
   Title      VARCHAR(100) NOT NULL,
   YearlySalary     INT          NOT NULL
);


CREATE TABLE Shippers
(
   ShipperName VARCHAR(100) PRIMARY KEY,
   PhoneNumber CHAR(10),
   ContactRep  VARCHAR(100)
);


CREATE TABLE Listings
(
   ListingId   CHAR(10) PRIMARY KEY,
   Quantity    INT          NOT NULL,
   Price       FLOAT        NOT NULL,
   EmployeeId  CHAR(10)     NOT NULL,
   ShipperName VARCHAR(100),
   ISBN        VARCHAR(13)  UNIQUE NOT NULL,


   FOREIGN KEY (EmployeeId) REFERENCES Employees (EmployeeId),
   FOREIGN KEY (ISBN) REFERENCES Textbooks (ISBN),
   FOREIGN KEY (ShipperName) REFERENCES Shippers (ShipperName)
);




CREATE TABLE Sales
(
   SaleNumber     INT PRIMARY KEY,
   UserId         CHAR(10)     NOT NULL,
   Street         VARCHAR(100) NOT NULL,
   City           VARCHAR(100) NOT NULL,
   State          CHAR(2)      NOT NULL,
   Zip            CHAR(5)      NOT NULL,
   Price          FLOAT        NOT NULL,
   SaleDate       DATE         NOT NULL,
   EmployeeId     CHAR(10),
   ShipperName    VARCHAR(100),
   ISBN           VARCHAR(13)  NOT NULL,
   FulfilmentDate DATE,


   FOREIGN KEY (UserId) REFERENCES Users (UserId),
   FOREIGN KEY (EmployeeId) REFERENCES Employees (EmployeeId),
   FOREIGN KEY (ShipperName) REFERENCES Shippers (ShipperName),
   FOREIGN KEY (ISBN) REFERENCES Textbooks (ISBN)
);






CREATE TABLE RentalInfo
(
   UserId      CHAR(10)     NOT NULL,
   ListingId   CHAR(10)     NOT NULL,
   OrderNumber INT          NOT NULL UNIQUE,
   Street      VARCHAR(100) NOT NULL,
   City        VARCHAR(100) NOT NULL,
   State       CHAR(2)      NOT NULL,
   Zip         CHAR(5)      NOT NULL,
   RentalStart DATE         NOT NULL,
   RentalEnd   DATE         NOT NULL,


   PRIMARY KEY (UserId, ListingId),


   FOREIGN KEY (UserId) REFERENCES Users (UserId),
   FOREIGN KEY (ListingId) REFERENCES Listings (ListingId)
);




CREATE TABLE PurchaseInfo
(
   UserId           CHAR(10)     NOT NULL,
   ListingId        CHAR(10)     NOT NULL,
   OrderNumber      INT          NOT NULL UNIQUE,
   Street           VARCHAR(100) NOT NULL,
   City             VARCHAR(100) NOT NULL,
   State            CHAR(2)      NOT NULL,
   Zip              CHAR(5)      NOT NULL,
   PurchaseDate     DATE         NOT NULL,
   PurchaseQuantity INT          NOT NULL,


   PRIMARY KEY (UserId, ListingId),


   FOREIGN KEY (UserId) REFERENCES Users (UserId),
   FOREIGN KEY (ListingId) REFERENCES Listings (ListingId)
);




