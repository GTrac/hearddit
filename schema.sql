DROP TABLE IF EXISTS users CASCADE;
DROP TABLE IF EXISTS posts CASCADE;
DROP TABLE IF EXISTS community CASCADE;


CREATE TABLE users (
    user_id SERIAL UNIQUE,
    user_name VARCHAR(255),
    user_email VARCHAR(255) UNIQUE,
    user_password VARCHAR(255),
    PRIMARY KEY (user_id)
);

INSERT INTO users (user_name, user_email, user_password) VALUES ('doejohn23', 'testUser001@test.com', 'password123');
INSERT INTO users (user_name, user_email, user_password) VALUES ('smithjane84', 'testUser002@test.com', 'ilovecats');
INSERT INTO users (user_name, user_email, user_password) VALUES ('rjohnson96', 'testUser003@test.com', 'qwertyuiop');
INSERT INTO users (user_name, user_email, user_password) VALUES ('emilyw87', 'testUser004@test.com', 'letmein');
INSERT INTO users (user_name, user_email, user_password) VALUES ('mbrown29', 'testUser005@test.com', 'abc123');

CREATE TABLE community(
    com_id SERIAL UNIQUE,
    com_name VARCHAR(50),
    user_id INTEGER,
    com_total_users INTEGER,
	PRIMARY KEY (com_id)
);

CREATE TABLE posts(
    post_id  SERIAL,
    post_title VARCHAR(75),
    post_link  VARCHAR(255),
    post_text VARCHAR(3000),
    post_rating INTEGER,
    com_id INTEGER,
    user_id INTEGER,
    track_id VARCHAR(255),
	PRIMARY KEY(post_id),
    FOREIGN KEY(com_id) REFERENCES community(com_id),
	FOREIGN KEY(user_id) REFERENCES users(user_id)
);


INSERT INTO community (com_name, user_id, com_total_users)
VALUES('TheBeatles', 1, 1);
INSERT INTO community (com_name, user_id, com_total_users)
VALUES('BillWithers', 2, 1);
INSERT INTO community (com_name, user_id, com_total_users)
VALUES('LedZepplin', 3, 1);
INSERT INTO community (com_name, user_id, com_total_users)
VALUES('DavidBowie', 4, 1);
INSERT INTO community (com_name, user_id, com_total_users)
VALUES('Supertramp', 5, 1);
INSERT INTO community (com_name, user_id, com_total_users)
VALUES('FrankSinatra', 1, 1);
INSERT INTO community (com_name, user_id, com_total_users)
VALUES('OtisRedding', 1, 1);

INSERT INTO posts (post_title, post_link, post_text, post_rating, com_id, user_id, track_id)

VALUES('What''s the deal with ''Yer Blues'' by the Beatles?', 'test_link_1', 
        'I recently listened to the White Album for the first time and was blown away by the song ''Yer Blues.'' It''s such a raw, intense track, and it''s so different from anything else the Beatles had released up to that point. I''m curious to know what other people think of the song. What do you love about it? What do you think it''s about? And how does it fit in with the rest of the White Album?For me, I think the song is about feeling isolated and disconnected, even when surrounded by other people. The lyrics are so bleak and desperate, and I think they perfectly capture the feeling of being stuck in the ''blues.''',
        1, 1, 1, '2AsGApoUuN8pTM17Lq9eUd');
INSERT INTO posts (post_title, post_link, post_text, post_rating, com_id, user_id, track_id)
VALUES('What''s the story behind ''Get Back'' by the Beatles?', 
        'test_link_1', 
        'I recently heard the Beatles'' song ''Get Back'' for the first time and I was really struck by it. It''s such a catchy, upbeat track, but the lyrics are kind of biting and sarcastic. I''m curious to know more about the story behind the song. What inspired the Beatles to write it? Who is it directed at? And how does it fit in with the rest of their discography?',
        1, 2, 1, '47qD4mGcc6cS4PbkvoIcy9');
INSERT INTO posts (post_title, post_link, post_text, post_rating, com_id, user_id, track_id)
VALUES('I can''t get enough of ''When the Levee Breaks'' by Led Zeppelin', 
        'test_link_1', 
        'I recently rediscovered ''When the Levee Breaks'' by Led Zeppelin and I am absolutely loving it. It''s such a powerful and intense track, and I can''t get enough of it.',
        1, 3, 1, '05f8Hg3RSfiPSCBQOtxl3i');
INSERT INTO posts (post_title, post_link, post_text, post_rating, com_id, user_id, track_id)
VALUES('Did you know... about ''Sittin'' on the Dock of the Bay'' by Otis Redding?', 
        'test_link_1', 
        'I recently learned something really cool about Otis Redding''s classic song ''Sittin'' on the Dock of the Bay.'' Did you know that the song was actually unfinished when Redding passed away? According to the story, Redding was in the studio working on the song when he had to leave to go on tour. He never got the chance to finish recording it, and he tragically passed away in a plane crash a few days later. The song was eventually finished by Redding''s producer, who added the famous whistling intro and outro. It''s amazing to think that such a timeless classic was never actually completed by its creator.',
        1, 4, 1, '3zBhihYUHBmGd2bcQIobrF');

