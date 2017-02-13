-- 1
SELECT address.city_id, first_name, customer.last_name, customer.email, address.address
FROM customer
LEFT JOIN address
ON customer.address_id = address.address_id
WHERE address.city_id = 312;

-- 2
SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name AS genre
FROM film
LEFT JOIN film_category
ON film.film_id = film_category.film_id
LEFT JOIN category
ON film_category.category_id = category.category_id
WHERE category.name = "Comedy";

-- 3
SELECT actor.first_name, actor.last_name, film.title, film.release_year, film.description
FROM actor
LEFT JOIN film_actor
ON actor.actor_id = film_actor.actor_id
LEFT JOIN film
ON film_actor.film_id = film.film_id
WHERE actor.actor_id = 5;

-- 4
SELECT customer.first_name, customer.last_name, customer.email, address.address
FROM customer
LEFT JOIN address
ON customer.address_id = address.address_id
WHERE customer.store_id = 1
AND address.city_id IN (3, 42, 312, 459);

-- 5
SELECT actor.first_name, actor.last_name, film.title, film.description, film.release_year, film.rating, film.special_features
FROM actor
LEFT JOIN film_actor
ON actor.actor_id = film_actor.actor_id
LEFT JOIN film
ON film_actor.film_id = film.film_id
WHERE actor.actor_id = 15 
AND film.rating = "G" 
AND film.special_features LIKE "%behind the scenes%";

-- 6
SELECT film.film_id, film.title, actor.actor_id, actor.first_name, actor.last_name
FROM actor
LEFT JOIN film_actor
ON actor.actor_id = film_actor.actor_id
LEFT JOIN film
ON film_actor.film_id = film.film_id
WHERE film.film_id = 369;

-- 7
SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name AS genre, film.rental_rate
FROM film
LEFT JOIN film_category
ON film.film_id = film_category.film_id
LEFT JOIN category
ON film_category.category_id = category.category_id
WHERE film.rental_rate = 2.99
AND category.name = "Drama";

-- 8
SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name, actor.first_name, actor.last_name
FROM actor
LEFT JOIN film_actor
ON actor.actor_id = film_actor.actor_id
LEFT JOIN film
ON film_actor.film_id = film.film_id
LEFT JOIN film_category
ON film.film_id = film_category.film_id
LEFT JOIN category
ON film_category.category_id = category.category_id
WHERE actor.first_name = "SANDRA" AND actor.last_name = "KILMER"
AND category.name = "ACTION";
