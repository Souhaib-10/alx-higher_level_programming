-- script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT g.name as genre, count(*) as number_of_shows 
	from tv_genres as g inner join tv_show_genres as tg
	on g.id = tg.genre_id 
	GROUP BY g.name 
	ORDER BY number_of_shows DESC;
