SELECT title, duration
  FROM track
 WHERE duration = (SELECT MAX(duration) FROM track);


SELECT title
  FROM track
  WHERE duration > 210;


SELECT title
  FROM music_collection
 WHERE year BETWEEN '2018-01-01' and '2020-12-31';

SELECT name
  FROM musican
 WHERE NOT name LIKE '% %';

SELECT title
  FROM track
 WHERE LOWER(title) LIKE '%my%' OR LOWER(title) LIKE '%мой%';

