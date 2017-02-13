SELECT users.first_name, users.last_name, users2.first_name as friend_first_name, users2.last_name as friend_last_name
FROM users
LEFT JOIN friendships
ON users.id = friendships.user_id
LEFT JOIN users as users2
ON friendships.friend_id = users2.id

-- INSERT INTO friendships
-- VALUES (1, 1, 5), (2,2,4),(3,3,2),(4,4,3),(5,5,1);
