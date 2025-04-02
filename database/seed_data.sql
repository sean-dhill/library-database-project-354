--Member Table 
INSERT INTO Member (fname, lname, phone, email, address) VALUES
('Sean', 'Dhillon', '123-456-7890', 'sean@example.com', '123 Library St'),
('Lana', 'Smith', '987-654-3210', 'lana@example.com', '456 Book Ave'),
('Tom', 'Brown', '555-555-5555', 'tom@example.com', '789 Paper Rd'),
('Nina', 'Li', '111-222-3333', 'nina@example.com', '234 Shelf Blvd'),
('Jack', 'Black', '444-333-2222', 'jack@example.com', '654 Bookmark Way'),
('Alice', 'Wong', '321-654-9870', 'alice@example.com', '101 Stack St'),
('Bob', 'Lee', '999-888-7777', 'bob@example.com', '202 Archive Ave'),
('Charlie', 'Kim', '333-444-5555', 'charlie@example.com', '303 Dewey Dr'),
('Diana', 'Zhao', '777-888-9999', 'diana@example.com', '404 Fiction Ln'),
('Eva', 'Cruz', '222-111-0000', 'eva@example.com', '505 Reader Rd');

--Personnel Table 
INSERT INTO Personnel (personnelID, memberID, jobTitle, startDate) VALUES
(1, 1, 'Librarian', '2022-01-10'),
(2, 2, 'Archivist', '2021-06-20'),
(3, 3, 'Clerk', '2023-03-14');

--Item Table 
INSERT INTO Item (title, type, format, available, dateAdded, price) VALUES
('1984', 'book', 'print', 1, '2024-01-01', 20),
('Great Expectations', 'book', 'print', 1, '2024-01-02', 18),
('Science Monthly', 'journal', 'digital', 1, '2024-01-03', 12),
('Time Magazine', 'magazine', 'print', 1, '2024-01-04', 10),
('The Beatles Collection', 'cd', 'digital', 1, '2024-01-05', 25),
('World History', 'book', 'digital', 1, '2024-01-06', 15),
('Nature Weekly', 'journal', 'print', 1, '2024-01-07', 13),
('Moby Dick', 'book', 'print', 1, '2024-01-08', 22),
('Guinness Records', 'book', 'print', 1, '2024-01-09', 30),
('Art and Soul', 'cd', 'digital', 1, '2024-01-10', 17);

--Loan Table 
INSERT INTO Loan (memberID, itemID, borrowDate, dueDate, returnDate) VALUES
(4, 1, '2024-03-01', '2024-03-14', '2024-03-12'),
(5, 2, '2024-03-02', '2024-03-16', NULL),
(6, 3, '2024-03-03', '2024-03-17', NULL),
(7, 4, '2024-03-04', '2024-03-18', '2024-03-17'),
(8, 5, '2024-03-05', '2024-03-19', NULL),
(9, 6, '2024-03-06', '2024-03-20', '2024-03-21'),
(10, 7, '2024-03-07', '2024-03-21', NULL),
(1, 8, '2024-03-08', '2024-03-22', '2024-03-22'),
(2, 9, '2024-03-09', '2024-03-23', NULL),
(3, 10, '2024-03-10', '2024-03-24', '2024-03-23');

--Fine Table 
INSERT INTO Fine (loanID, amount) VALUES
(6, 5),
(10, 3),
(1, 0),
(4, 0),
(7, 2),
(9, 0),
(2, 0),
(3, 0),
(5, 0),
(8, 0);

--Room Table 
INSERT INTO Room (name, floor, capacity) VALUES
('Main Hall', 1, 100),
('Conference Room A', 2, 50),
('Childrens Room', 1, 30),
('Reading Lounge', 3, 25),
('Art Gallery', 2, 40),
('Screening Room', 1, 60),
('Workshop Studio', 3, 20),
('Poetry Nook', 2, 15),
('Archive Basement', 0, 10),
('Lecture Theater', 2, 80);

--Events Table 
INSERT INTO Events (name, date, time, type, targetAudience) VALUES
('Book Club: Mystery Night', '2024-04-01', '18:00', 'book club', 'adults'),
('Art Show: Local Talent', '2024-04-05', '14:00', 'art show', 'all'),
('Childrens Storytime', '2024-04-10', '10:00', 'reading', 'children'),
('Film Screening: Classics', '2024-04-12', '19:00', 'film screening', 'seniors'),
('Poetry Slam', '2024-04-14', '17:00', 'literature', 'teens'),
('Historical Lecture', '2024-04-15', '15:00', 'lecture', 'adults'),
('Science Fair', '2024-04-20', '13:00', 'education', 'all'),
('Local Author Talk', '2024-04-22', '16:00', 'lecture', 'adults'),
('Music Recital', '2024-04-25', '18:00', 'performance', 'all'),
('Craft Workshop', '2024-04-27', '11:00', 'workshop', 'children');

--Scheduled Table 
INSERT INTO Scheduled (eventID, roomID, dateTime) VALUES
(1, 1, '2024-04-01 18:00'),
(2, 5, '2024-04-05 14:00'),
(3, 3, '2024-04-10 10:00'),
(4, 6, '2024-04-12 19:00'),
(5, 8, '2024-04-14 17:00'),
(6, 10, '2024-04-15 15:00'),
(7, 7, '2024-04-20 13:00'),
(8, 4, '2024-04-22 16:00'),
(9, 6, '2024-04-25 18:00'),
(10, 2, '2024-04-27 11:00');

-- Registrations Table
INSERT INTO Registrations (personID, eventID, registrationDate, role) VALUES
(1, 1, '2024-04-01', 'attendee'),
(2, 2, '2024-04-02', 'attendee'),
(3, 3, '2024-04-03', 'speaker'),
(4, 4, '2024-04-04', 'host'),
(5, 5, '2024-04-05', 'attendee'),
(6, 6, '2024-04-06', 'attendee'),
(7, 7, '2024-04-07', 'speaker'),
(8, 8, '2024-04-08', 'host'),
(9, 9, '2024-04-09', 'attendee'),
(10, 10, '2024-04-10', 'attendee');

--Donation Table 
INSERT INTO Donation (memberID, description, status, numItems) VALUES
(1, 'Box of old magazines', 'accepted', 15),
(2, 'Childrens books collection', 'pending', 20),
(3, 'Rare vinyl records', 'rejected', 5),
(4, 'Science fiction novels', 'accepted', 10),
(5, 'Educational DVDs', 'pending', 8),
(6, 'Classic literature', 'accepted', 12),
(7, 'Art prints', 'pending', 7),
(8, 'DIY guides', 'accepted', 6),
(9, 'Textbooks', 'pending', 9),
(10, 'Travel journals', 'rejected', 4);

--HelpRequest Table 
INSERT INTO HelpRequest (memberID, personnelID, issue, solved) VALUES
(4, 1, 'Need help finding study material', 0),
(5, 2, 'Can’t log in to library account', 1),
(6, 1, 'Overdue book not showing return option', 0),
(7, 3, 'Want to volunteer for events', 1),
(8, 2, 'Where is the art section?', 0),
(9, 1, 'Need assistance with e-books', 0),
(10, 2, 'Forgot password', 1),
(1, 3, 'Request for quiet study room', 0),
(2, 1, 'Late fee clarification needed', 1),
(3, 2, 'Problem with online catalog', 0);
