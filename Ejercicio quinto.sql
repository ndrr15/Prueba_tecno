

--1. CONSULTA:

SELECT
    CONCAT(usr.first_name,' ',usr.lASt_name) AS Usuario,
    pl.name AS Playlist,
    sg.name AS Canciones,
    sg.gender AS Genero,
    art.name AS Artista
FROM
    users AS usr,
    playlists AS pl,
    songs AS sg,
    artists AS Art
WHERE
    pl.user_id = usr.id AND 
    pl.song_id = sg.id AND
    art.id=sg.artist_id


--2. CONSULTA:

SELECT
	Art.name AS Artista,
	abm.name AS Albumes,
	abm.releASe_date AS "Fecha de Lanzamiento",
	abm.gender AS Genero
FROM
	artists AS Art,
	albums AS abm
WHERE
	abm.artist_id=Art.id


--3. CONSULTA:

SELECT
	Art.name AS Artista,
	pdc.id AS PodcASts,
	pdc.duration AS Duración,
	pdc.gender AS Genero
FROM
	artists AS Art,
	podcASts AS pdc

WHERE
	pdc.artist_id = Art.id


--4. CONSULTA:

SELECT
	art.name AS Artista,
	alb.name AS Albumes,
	alb.releASe_date AS "Fecha de Lanzamiento",
	alb.gender AS Genero
FROM
	artists AS art,
	albums AS alb
WHERE
	alb.bitactivo = 0 AND
	alb.artist_id = art.id