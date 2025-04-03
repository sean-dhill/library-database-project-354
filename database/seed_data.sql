INSERT INTO Items VALUES
(1, 'The Great Gatsby', 'book', 'print', TRUE, '2023-01-15', 15),
(2, 'Inception', 'cd', 'digital', TRUE, '2023-03-22', 25),
(3, 'National Geographic', 'magazine', 'print', FALSE, '2022-12-01', 10),
(4, '1984', 'book', 'print', TRUE, '2023-02-10', 12),
(5, 'To Kill a Mockingbird', 'book', 'digital', FALSE, '2023-04-18', 18),
(6, 'Planet Earth', 'dvd', 'digital', TRUE, '2023-05-20', 30),
(7, 'Brave New World', 'book', 'print', TRUE, '2023-06-11', 14),
(8, 'Cosmos', 'cd', 'digital', TRUE, '2023-07-25', 22),
(9, 'Python Programming', 'book', 'print', FALSE, '2023-08-05', 40),
(10, 'The Beatles - Abbey Road', 'cd', 'digital', TRUE, '2023-09-15', 20);

INSERT INTO Members VALUES
(101, 'Alice', 'Smith', '604-555-1234', 'alice@example.com', '123 Elm Street'),
(102, 'Bob', 'Johnson', '604-555-5678', 'bob@example.com', '456 Oak Avenue'),
(103, 'Carol', 'Davis', '604-555-9012', 'carol@example.com', '789 Maple Road'),
(104, 'Dave', 'Martinez', '604-555-3456', 'dave@example.com', '321 Birch Blvd'),
(105, 'Eve', 'Brown', '604-555-7890', 'eve@example.com', '654 Pine Lane'),
(106, 'Frank', 'Wilson', '604-555-2345', 'frank@example.com', '987 Cedar St'),
(107, 'Grace', 'Lee', '604-555-6789', 'grace@example.com', '159 Spruce Dr'),
(108, 'Hank', 'Kim', '604-555-0123', 'hank@example.com', '753 Willow Way'),
(109, 'Ivy', 'Clark', '604-555-4567', 'ivy@example.com', '852 Redwood Ct'),
(110, 'Jake', 'Wright', '604-555-8910', 'jake@example.com', '951 Aspen Pl'),
(111, 'Lily', 'Nguyen', '604-555-1111', 'lily@example.com', '111 Tulip Rd'),
(112, 'Mason', 'Chen', '604-555-2222', 'mason@example.com', '112 Daffodil St'),
(113, 'Sophie', 'Patel', '604-555-3333', 'sophie@example.com', '113 Lily Ln'),
(114, 'Ryan', 'Ali', '604-555-4444', 'ryan@example.com', '114 Rose Blvd');

INSERT INTO Personnel VALUES
(101, 'librarian', '2022-05-01'),
(102, 'clerk', '2023-01-10'),
(103, 'archivist', '2021-11-20'),
(104, 'clerk', '2023-03-15'),
(105, 'librarian', '2020-06-12'),
(106, 'assistant', '2022-08-25'),
(107, 'librarian', '2021-02-03'),
(108, 'archivist', '2023-07-07'),
(109, 'clerk', '2022-09-18'),
(110, 'librarian', '2023-10-01');

INSERT INTO Loans VALUES
(1, 101, 3, '2024-01-01', '2024-01-15', '2024-01-10'),
(2, 102, 5, '2024-02-01', '2024-02-14', NULL),
(3, 103, 2, '2024-01-20', '2024-02-03', '2024-02-02'),
(4, 104, 4, '2024-01-15', '2024-01-29', '2024-01-30'),
(5, 105, 9, '2024-03-01', '2024-03-15', NULL),
(6, 106, 6, '2024-01-25', '2024-02-08', '2024-02-07'),
(7, 107, 1, '2024-02-10', '2024-02-24', '2024-02-22'),
(8, 108, 7, '2024-01-05', '2024-01-19', '2024-01-18'),
(9, 109, 8, '2024-03-10', '2024-03-24', NULL),
(10, 110, 10, '2024-02-15', '2024-02-28', '2024-02-27');

INSERT INTO Fines VALUES
(4, 5),
(5, 8),
(9, 12),
(2, 10),
(10, 6),
(3, 0),
(1, 0),
(6, 0),
(7, 0),
(8, 0);

INSERT INTO Rooms VALUES
(1, 'John A. MacDonald Theater', 1, 100),
(2, 'Conference Room 2', 2, 30),
(3, 'Main Hall', 1, 200),
(4, 'Reading Lounge', 3, 40),
(5, 'Kids Activity Room', 1, 25),
(6, 'Community Workshop Space', 2, 50),
(7, 'Local History Room', 3, 20),
(8, 'Media Center', 2, 15),
(9, 'Exhibit Gallery', 1, 75),
(10, 'Teen Zone', 3, 35);

INSERT INTO Events VALUES
(1, 1, 'Monthly Book Club', '2024-04-01', '18:00:00', 'book club', 'adults'),
(2, 5, 'Story Time', '2024-04-03', '10:00:00', 'reading', 'children'),
(3, 9, 'Art Exhibit Opening', '2024-04-05', '16:00:00', 'art show', 'general'),
(4, 2, 'Writing Workshop', '2024-04-08', '14:00:00', 'workshop', 'advanced readers'),
(5, 10, 'Teen Game Night', '2024-04-10', '18:30:00', 'games', 'teens'),
(6, 3, 'Local Author Signing', '2024-04-12', '13:00:00', 'writer signing', 'general'),
(7, 6, 'Crafting for Seniors', '2024-04-15', '11:00:00', 'craft', 'seniors'),
(8, 4, 'Quiet Reading Session', '2024-04-17', '15:00:00', 'reading', 'general'),
(9, 8, 'Tech Talk', '2024-04-20', '17:00:00', 'seminar', 'adults'),
(10, 7, 'History Night', '2024-04-22', '19:00:00', 'lecture', 'seniors');

INSERT INTO Donations VALUES
(1, 101, 'Classic novels collection', 'approved', 20),
(2, 102, 'Vintage music CDs', 'pending', 15),
(3, 103, 'Children''s books', 'approved', 25),
(4, 104, 'Rare magazines', 'denied', 5),
(5, 105, 'Reference textbooks', 'approved', 30),
(6, 106, 'Local history documents', 'approved', 10),
(7, 107, 'Craft supplies', 'pending', 12),
(8, 108, 'Board games', 'approved', 8),
(9, 109, 'Art supplies', 'denied', 18),
(10, 110, 'Science journals', 'pending', 7);

INSERT INTO HelpRequests VALUES
(1, 101, 110, 'Need help locating science books', TRUE),
(2, 102, NULL, 'Issue with digital media access', FALSE),
(3, 103, 105, 'Printing not working on 2nd floor', TRUE),
(4, 104, NULL, 'Can''t log into account', FALSE),
(5, 105, 107, 'Borrow limit clarification', TRUE),
(6, 106, 101, 'Assistance finding archived newspapers', TRUE),
(7, 107, NULL, 'E-book will not download', FALSE),
(8, 108, 109, 'Room reservation issues', TRUE),
(9, 109, NULL, 'Requesting a tour of library', FALSE),
(10, 110, 103, 'Donation inquiry', TRUE);

INSERT INTO Registers VALUES
(1, 101),
(2, 102),
(3, 103),
(4, 104),
(5, 105),
(6, 106),
(7, 107),
(8, 108),
(9, 109),
(10, 110);