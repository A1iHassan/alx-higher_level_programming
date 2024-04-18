-- answer for task 9

-- creates a new table
CREATE TABLE IF NOT EXISTS second_table (
	id INT,
	'name' VARCHAR(256),
	score INT
);

-- starts perfoming operations on the table
USE second_table;

-- add data to the table
INSERT INTO second_table (id, name, score) VALUES
(1, 'Jhon', 10),
(2, 'Alex', 3),
(3, 'Bob', 14),
(4, 'George', 8);
