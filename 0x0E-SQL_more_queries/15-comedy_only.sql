-- script that lists all Comedy shows in the database hbtn_0d_tvshows.
SELECT t.title
        FROM tv_genres AS g, tv_shows AS t, tv_show_genres AS tg
        WHERE t.id = tg.show_id AND g.id = tg.genre_id AND g.name 		="Comedy"
        ORDER BY t.title;
