DROP TABLE IF EXISTS HelpRequest;
DROP TABLE IF EXISTS Donation;
DROP TABLE IF EXISTS Fine;
DROP TABLE IF EXISTS Loan;
DROP TABLE IF EXISTS Personnel;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Item;
DROP TABLE IF EXISTS Room;
DROP TABLE IF EXISTS Events;
DROP TABLE IF EXISTS Registrations;

--Member Table
CREATE TABLE Member(
    memberID INTEGER PRIMARY KEY,
    fname TEXT NOT NULL,
    lname TEXT NOT NULL,
    phone TEXT CHECK (length(phone) = 12),
    email TEXT CHECK (instr(email, '@') > 1 AND instr(email, '.') > instr(email, '@')) NOT NULL,
    address TEXT
);

--Personnel Table
CREATE TABLE Personnel (
    memberID INTEGER PRIMARY KEY,
    jobTitle TEXT NOT NULL,
    startDate DATE,
    FOREIGN KEY (memberID) REFERENCES Member(memberID)
);

--Item Table
CREATE TABLE Item (
    itemID INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    type TEXT NOT NULL, --book, cd, journal
    format TEXT CHECK(format IN('print', 'digital')) NOT NULL,
    available BOOLEAN DEFAULT 1,
    dateAdded DATE,
    price INTEGER
);

--Loan Table
CREATE TABLE Loan(
    loanID INTEGER PRIMARY KEY,
    memberID INTEGER NOT NULL,
    itemID INTEGER NOT NULL,
    borrowDate DATE NOT NULL,
    dueDate DATE NOT NULL,
    returnDate DATE,
    FOREIGN KEY (memberID) REFERENCES Member(memberID),
    FOREIGN KEY (itemID) REFERENCES Item(itemID)  
);

--Fine Table
CREATE TABLE Fine(
    loanID INTEGER PRIMARY KEY,
    amount INTEGER NOT NULL,
    FOREIGN KEY (loanID) REFERENCES Loan(loanID)
);

--Room Table
CREATE TABLE Room(
    roomID INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    floor INTEGER,
    capacity INTEGER
);

--Event Table
CREATE TABLE Events(
    eventID INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    date DATE NOT NULL,
    time TIME NOT NULL,
    type TEXT,
    targetAudience TEXT
);


--Donation Table
CREATE TABLE Donation(
    donationID INTEGER PRIMARY KEY,
    memberID INTEGER NOT NULL,
    description TEXT NOT NULL,
    status TEXT CHECK(status IN ('pending', 'accepted', 'rejected')) NOT NULL,
    numItems INTEGER NOT NULL,
    FOREIGN KEY (memberID) REFERENCES Member(memberID)
);

--HelpRequest Table
CREATE TABLE HelpRequest(
    requestID INTEGER PRIMARY KEY,
    memberID INTEGER NOT NULL,
    librarianID INTEGER,
    issue TEXT NOT NULL,
    solved BOOLEAN DEFAULT 0,
    FOREIGN KEY (memberID) REFERENCES Member(memberID),
    FOREIGN KEY (librarianID) REFERENCES Personnel(memberID)
);

CREATE TABLE Registrations (
    registrationID INTEGER PRIMARY KEY,
    personID INTEGER NOT NULL,
    eventID INTEGER NOT NULL,
    registrationDate DATE NOT NULL,
    role TEXT CHECK (role IN ('host', 'attendee', 'speaker')),
    FOREIGN KEY (personID) REFERENCES Member(memberID),
    FOREIGN KEY (eventID) REFERENCES Events(eventID)
);