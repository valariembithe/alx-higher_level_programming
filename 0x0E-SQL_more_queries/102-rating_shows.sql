--  lists all shows from hbtn_0d_tvshows_rate by their rating.
SELECT title, SUM(rating) AS rating
FROM tv_shows
JOIN tv_shows_ratings
ON tv_shows.id = tv_shows_ratings.show_id
GROUP BY title
ORDER BY rating DESC;
