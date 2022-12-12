DROP TABLE IF EXISTS posts;
DROP TABLE IF EXISTS subhearddits;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
    user_id SERIAL UNIQUE,
    user_name VARCHAR(255),
    user_email VARCHAR(255) UNIQUE,
    user_password VARCHAR(255),
    PRIMARY KEY (user_id)
);


CREATE TABLE subhearddits(
    sub_id SERIAL,
    sub_name VARCHAR(50),
    user_id INTEGER UNIQUE,
    sub_total_users INTEGER,
	PRIMARY KEY (sub_id), 
    FOREIGN KEY(user_id) REFERENCES users(user_id)
);

CREATE TABLE posts(
    post_id  SERIAL,
    post_title VARCHAR(50),
    post_link  VARCHAR(255),
    post_text VARCHAR(255),
    post_rating INTEGER,
    sub_id INTEGER UNIQUE,
    user_id INTEGER UNIQUE,
	PRIMARY KEY(post_id),
    FOREIGN KEY(sub_id) REFERENCES subhearddits(sub_id)
    FOREIGN KEY(user_id) REFERENCES users(user_id)
);


INSERT INTO subhearddits (sub_name, user_id, sub_total_users)
VALUES('Test Sub 1', null, 1)
VALUES('Test Sub 2', null, 2)
VALUES('Test Sub 3', null, 3)
VALUES('Test Sub 4', null, 4);

INSERT INTO posts (post_title, post_link, post_text, post_rating, sub_id)
VALUES('Test Post 1', 'test_link_1', 'Test text for post 1', 1, 1)
VALUES('Test Post 2', 'test_link_2', 'Test text for post 2', 2, 2)
VALUES('Test Post 3', 'test_link_3', 'Test text for post 3', 3, 3)
VALUES('Test Post 4', 'test_link_4', 'Test text for post 4', 4, 4);