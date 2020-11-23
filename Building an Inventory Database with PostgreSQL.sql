-- alter "code" column in the "parts" table as unique and not empty
ALTER TABLE parts 
ALTER COLUMN code SET NOT NULL;

ALTER TABLE parts 
ADD UNIQUE (code);

-- Alter the table so that all rows have a value for "description":
UPDATE parts
SET description = 'None Available'
WHERE description IS NULL;

-- ensure that all values in description non-empty:
ALTER TABLE parts
ALTER COLUMN description
SET NOT NULL;

-- update "parts":
CREATE TABLE parts_temp (
    id int PRIMARY KEY, 
    code VARCHAR,
    manufacturer_id INT 
);

INSERT INTO parts_temp
VALUES (54, 'V1-009', 9);

UPDATE parts
SET id = parts_temp.id
from parts_temp
where parts_temp.id = parts.id
and parts.id IS NULL;

-- ensures that price_usd and quantity are both NOT NULL in "reorder_options":
ALTER TABLE reorder_options
ALTER COLUMN price_usd 
SET NOT NULL;

ALTER TABLE reorder_options
ALTER COLUMN quantity 
SET NOT NULL;

--ensure that price_usd and quantity are both positive: 
ALTER TABLE reorder_options
ADD CHECK (price_usd > 0 AND quantity > 0);

-- ensure that price per unit between 0.02 USD and 25.00 USD: 
ALTER TABLE reorder_options
ADD CHECK (price_usd/quantity > 0.02 AND price_usd/quantity < 25.00);

-- Form a relationship between parts and reorder_options:
ALTER TABLE parts
ADD PRIMARY KEY (id);

ALTER TABLE reorder_options
ADD FOREIGN KEY (part_id) REFERENCES parts (id);

-- ensure that each value in qty is greater than 0 in "locations" table:
ALTER TABLE locations
ADD CHECK (qty >0);

-- ensure that locations records only one row for each combination of location and part.
ALTER TABLE locations
ADD UNIQUE (part_id, location);

 -- ensure that for a part to be stored in locations, it must already be registered in parts.
ALTER TABLE locations
ADD FOREIGN KEY (part_id) REFERENCES parts (id);

-- ensure that all parts in parts have a valid manufacturer.
ALTER TABLE parts
ADD FOREIGN KEY (manufacturer_id) 
REFERENCES manufacturer (id);
-- Assume that 'Pip Industrial' and 'NNC Manufacturing' merge and become 'Pip-NNC Industrial'. Create a new manufacturer in manufacturers with an id=11:
INSERT INTO manufacturers VALUES (11, 'Pip-NNC Industrial');





   
