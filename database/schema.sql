DROP TABLE IF EXISTS Items;
DROP TABLE IF EXISTS Members;
DROP TABLE IF EXISTS Personnel;
DROP TABLE IF EXISTS Loans;
DROP TABLE IF EXISTS Fines;
DROP TABLE IF EXISTS Rooms;
DROP TABLE IF EXISTS Events;
DROP TABLE IF EXISTS Donations;
DROP TABLE IF EXISTS HelpRequests;
DROP TABLE IF EXISTS Registrations;

CREATE TABLE Items (
    itemID INT UNSIGNED PRIMARY KEY,
    name VARCHAR(128),
    type VARCHAR(16),           -- e.g., book, cd, etc.
    format VARCHAR(16),         -- e.g., print, digital, etc.
    available BOOL DEFAULT TRUE,
    dateAdded DATE,
    price SMALLINT UNSIGNED,
);

CREATE TABLE Members (
    memberID INT UNSIGNED PRIMARY KEY,
    fname VARCHAR(16),
    lname VARCHAR(16),
    phone VARCHAR(16),
    email VARCHAR(64),
    address VARCHAR(256),
    CHECK (phone REGEXP '^[0-9]{3}-[0-9]{3}-[0-9]{4}$'),
    CHECK (email LIKE '_%@_%._%')
);

CREATE TABLE Personnel (
    memberID INT UNSIGNED PRIMARY KEY,
    jobTitle VARCHAR(16),       -- e.g., librarian, clerk, archivist, etc.
    startDate DATE,
    FOREIGN KEY (memberID) REFERENCES Members(memberID)
);

CREATE TABLE Loans (
    loanID INT UNSIGNED PRIMARY KEY,
    memberID INT UNSIGNED NOT NULL,
    itemID INT UNSIGNED NOT NULL,
    borrowDate DATE,
    dueDate DATE,
    returnDate DATE,             -- NULL if not returned
    FOREIGN KEY (memberID) REFERENCES Members(memberID),
    FOREIGN KEY (itemID) REFERENCES Items(itemID)
);

CREATE TABLE Fines (
    loanID INT UNSIGNED PRIMARY KEY,
    amount SMALLINT UNSIGNED,
    FOREIGN KEY (loanID) REFERENCES Loans(loanID)
);

CREATE TABLE Rooms (
    roomID INT UNSIGNED PRIMARY KEY,
    name VARCHAR(64),           -- e.g., John A. MacDonald Theater, Conference 2, Main Hall, etc.
    floor TINYINT UNSIGNED,
    capacity SMALLINT UNSIGNED,
    PRIMARY KEY (roomID)
);

CREATE TABLE Events (
    eventID INT UNSIGNED PRIMARY KEY,
    roomID INT UNSIGNED,
    name VARCHAR(64),
    date DATE,                  -- format: YYYY-MM-DD
    time TIME,
    type VARCHAR(32),           -- e.g., book club, art show, writer signing, etc.
    targetAudience VARCHAR(32), -- e.g., seniors, advanced readers, children, etc.
    FOREIGN KEY (roomID) REFERENCES Rooms(roomID)
);

CREATE TABLE Donations (
    donationID INT UNSIGNED PRIMARY KEY,
    memberID INT UNSIGNED,
    description VARCHAR(128),
    status VARCHAR(10),         -- e.g., approved, pending, denied
    numItems SMALLINT UNSIGNED,
    FOREIGN KEY (memberID) REFERENCES Members(memberID)
);

CREATE TABLE HelpRequest (
    requestID INT UNSIGNED PRIMARY KEY,
    requesterID INT UNSIGNED NOT NULL,
    librarianID INT UNSIGNED DEFAULT NULL, -- Null on request creation
    issue VARCHAR(256),         -- description of issue
    solved BOOL DEFAULT FALSE,
    FOREIGN KEY (requesterID) REFERENCES Members(memberID),
    FOREIGN KEY (librarianID) REFERENCES Members(memberID)
);

CREATE TABLE Registers (
    eventID INT UNSIGNED NOT NULL,
    memberID INT UNSIGNED NOT NULL,
    PRIMARY KEY (eventID, memberID),
    FOREIGN KEY (eventID) REFERENCES Events(eventID),
    FOREIGN KEY (memberID) REFERENCES Members(memberID)
);
