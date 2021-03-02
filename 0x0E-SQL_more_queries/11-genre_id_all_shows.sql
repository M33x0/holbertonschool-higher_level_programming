-- 11. Genre ID for all shows
-- List shows containing in db hbtn_od_tvshows
SELECT		tv_shows.title, tv_show_genres.genre_id
FROM		tv_shows
LEFT JOIN	tv_show_genres
ON			tv_show_genres.show_id = tv_shows.id
ORDER BY	tv_shows.title ASC,
			tv_show_genres.genre_id ASC;