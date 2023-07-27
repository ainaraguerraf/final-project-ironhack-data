
# CREATE THE SCHEMA TO USE IT
CREATE schema schema_final_project;

# SELECT THE DATABASE
use schema_final_project;

# SHOW DATA
SELECT *
FROM data_for_tableau_and_sql;

# COUNT UNIQUE VALUES
SELECT count(*)
FROM data_for_tableau_and_sql;

# COUNT VALUES INSIDE EACH AREA
SELECT area, COUNT(name) AS total_per_area
FROM data_for_tableau_and_sql
GROUP BY area;

# COUNT VALUES INSIDE EACH CATEGORY
SELECT cat_sites_reduced_more, COUNT(name) AS total_per_category
FROM data_for_tableau_and_sql
GROUP BY cat_sites_reduced_more;

# COUNT VALUES INSIDE EACH category and AREA
SELECT area, cat_sites_reduced_more, COUNT(*) AS total_category_per_area
FROM data_for_tableau_and_sql
GROUP BY area, cat_sites_reduced_more;

# COUNT VALUES INSIDE EACH AGE
SELECT average_age, COUNT(name) AS total_per_age_category
FROM data_for_tableau_and_sql
GROUP BY average_age;

# COUNT VALUES INSIDE EACH WAY OF TRAVEL
SELECT way_travel_encoded, COUNT(name) AS total_per_way_of_travel
FROM data_for_tableau_and_sql
GROUP BY way_travel_encoded;

# LIST BEST RANKED SITES
SELECT name, cat_sites_reduced_more, rating
FROM data_for_tableau_and_sql
ORDER BY rating DESC;

# LIST WORST RANKED SITES
SELECT name, cat_sites_reduced_more, rating
FROM data_for_tableau_and_sql
ORDER BY rating ASC;


