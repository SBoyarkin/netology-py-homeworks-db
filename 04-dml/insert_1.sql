INSERT INTO musican(name)
VALUES ('Linkin Park'),
       ('Prodigy'),
       ('Riana'),
       ('Nirvana'),
       ('Lorde'),
       ('Katy Perry');

INSERT INTO genre(genre)
VALUES ('Rock'),
       ('RNB'),
       ('Electro house'),
       ('Jazz house'),
       ('Electropunk');

INSERT INTO album(title, yaer)
VALUES ('Hybrid Theory','2000-10-01'),
       ('Meteora','2003-03-01'),
       ('Experience','1992-09-28'),
       ('Music for the Jilted Generation','1994-07-04'),
       ('No Tourists','2018-11-2'),
       ('Good Girl Gone Bad','2007-06-05'),
       ('Rated R','2009-11-23'),
       ('Loud','2010-11-23'),
       ('Smile','2020-08-28'),
       ('Bleach','1989-06-15'),
       ('Killection','2020-01-31');


INSERT INTO track(title, duration, album_id)
VALUES ('Papercut','187','2'),
       ('Faint','166','2'),
       ('A Place For My Head','184','1'),
       ('Poison','422','4'),
       ('Intro','45','4'),
       ('Mad House','94','7'),
       ('Hard','250','7'),
       ('In the end', '422', '2'),
       ('Мой герой','90','7'),
       ('«Radio SCG 10»','83','11'),
       ('«Shake the Baby Silent»','83','11'),
       ('«Apollyon»','206','11');

INSERT INTO musicant_genre(genre_id, musicant_id)
VALUES ('5','4'),
       ('1','1'),
       ('1','4'),
       ('2','3'),
       ('2','6'),
       ('3','4');




INSERT INTO album_musicant (album_id, musican_id)
VALUES ('1','1'),
       ('2','1'),
       ('3','2'),
       ('4','3'),
       ('5','3'),
       ('6','4'),
       ('9','5'),
       ('7','5'),
       ('10','6');


INSERT INTO music_collection(title, year)
VALUES ('Музыка для тренировки','2024-01-01'),
       ('Самые прослушиваемые за 2023 год','2023-12-31'),
       ('Легены музыки','2023-06-11'),
       ('Linkin park and Prodjy','2020-12-31');


INSERT INTO track_music_collection(track_id, music_collection_id)
VALUES ('1','4'),
       ('2','4'),
       ('3','4'),
       ('4','4'),
       ('1','3'),
       ('2','3'),
       ('3','3'),
       ('4','3'),
       ('5','3'),
       ('6','3'),
       ('7','3'),
       ('8','3'),
       ('1','2'),
       ('3','2'),
       ('5','2'),
       ('7','2'),
       ('2','2'),
       ('8','1'),
       ('5','1'),
       ('1','1');
