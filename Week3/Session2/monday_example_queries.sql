USE wednesday_group_activity;
-- SET SQL_SAFE_UPDATES = 0;
-- INSERT INTO states(name, timezone) VALUES("Washington");
-- INSERT INTO states(name, timezone) VALUES("Oregon");
-- INSERT INTO states(name, timezone) VALUES("California");

-- UPDATE states SET name="Washington" WHERE id=1;
-- UPDATE states SET name="Oregon" WHERE id=2;
-- UPDATE states SET name="California" WHERE id=3;
INSERT INTO cities(name, state_id) VALUES("Seattle", 1);
INSERT INTO cities(name, state_id) VALUES("Portland", 2);
INSERT INTO cities(name, state_id) VALUES("Los Angeles", 3);

SELECT * FROM cities;