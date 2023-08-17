--  script that lists all cities contained in the database hbtn_0d_usa.
SELECT cities.id, cities.name, states.id
FROM cities
INNER JOIN states on cities.states_id=states.id
ORDER BY cities.id ASC;
