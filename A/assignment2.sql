CREATE TABLE Points (
    point_id INT PRIMARY KEY AUTO_INCREMENT,
    x INT,
    y INT
);

CREATE TABLE Shapes (
    shape_id INT PRIMARY KEY,
    shape_name VARCHAR(50),
    position_id INT,
    FOREIGN KEY (position_id) REFERENCES Points (point_id)
);

INSERT INTO Points (x, y) VALUES (10, 20);
INSERT INTO Points (x, y) VALUES (30, 40);
INSERT INTO Points (x, y) VALUES (50, 60);

INSERT INTO Shapes (shape_id, shape_name, position_id) VALUES (1, 'Circle', 1); 
INSERT INTO Shapes (shape_id, shape_name, position_id) VALUES (2, 'Square', 2); 
INSERT INTO Shapes (shape_id, shape_name, position_id) VALUES (3, 'Triangle', 3); 
