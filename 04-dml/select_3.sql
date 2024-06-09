SELECT COUNT(musicant_id) AS count, genre.genre
  FROM musicant_genre
  JOIN genre 
    ON musicant_genre.genre_id = genre.id
 GROUP BY genre.genre;


SELECT count(track.title)
  FROM track
  JOIN album
    ON album_id=album.id
 WHERE yaer BETWEEN '2019-01-01' and '2020-12-31'


SELECT ROUND(AVG(duration),2), album.title
  FROM track
  JOIN album
    ON album_id=album.id
 GROUP BY album.title


SELECT DISTINCT(musican.name)
  FROM album_musicant
  JOIN musican
    ON musican_id = musican.id
  JOIN album
    ON album_id = album.id
 WHERE musican.name <> (SELECT DISTINCT(musican.name)
  FROM album_musicant
  JOIN musican
    ON musican_id = musican.id
  JOIN album
    ON album_id = album.id
 WHERE album.yaer BETWEEN '2020-01-01' AND  '2020-12-31');

SELECT music_collection.title
  FROM track_music_collection
  JOIN musican 
    ON track_id  = musican.id
  JOIN music_collection
    ON music_collection_id = music_collection.id
 WHERE musican.name LIKE 'Linkin Park'
