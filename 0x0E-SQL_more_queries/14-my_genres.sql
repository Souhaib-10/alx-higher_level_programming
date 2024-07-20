-- script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
SELECT g.name
	FROM tv_genres AS g, tv_shows AS t, tv_show_genres AS tg 
	WHERE t.id = tg.show_id AND g.id = tg.genre_id AND title = 		"Dexter";
