DROP TABLE IF EXISTS users CASCADE;
DROP TABLE IF EXISTS posts CASCADE;
DROP TABLE IF EXISTS community CASCADE;
DROP TABLE IF EXISTS user_comments CASCADE;


CREATE TABLE users (
    user_id SERIAL UNIQUE,
    user_name VARCHAR(255),
    user_email VARCHAR(255) UNIQUE,
    user_password VARCHAR(255),
    PRIMARY KEY (user_id)
);

INSERT INTO users(user_name, user_email, user_password)
VALUES('test', 'test@test.test', 'test');

CREATE TABLE community(
    com_id SERIAL UNIQUE,
    com_name VARCHAR(50),
    user_id INTEGER,
    com_total_users INTEGER,
	PRIMARY KEY (com_id)
);

CREATE TABLE posts(
    post_id  SERIAL,
    post_title VARCHAR(50),
    post_link  VARCHAR(255),
    post_text VARCHAR(255),
    post_rating INTEGER,
    com_id INTEGER,
    user_id INTEGER,
	PRIMARY KEY(post_id),
    FOREIGN KEY(com_id) REFERENCES community(com_id),
	FOREIGN KEY(user_id) REFERENCES users(user_id)
);

CREATE TABLE user_comments(
    comment_id SERIAL,
    user_id INTEGER UNIQUE,
    post_id SERIAL,
    reply_id INTEGER,
    flagged_comment BOOLEAN NULL,
    comment_text VARCHAR(40000),
    comment_rating INTEGER,
    PRIMARY KEY(comment_id),
    FOREIGN KEY(post_id) REFERENCES posts(post_id),
    FOREIGN KEY(user_id) REFERENCES users(user_id),
    FOREIGN KEY(flagged_comment) REFERENCES flag_comments(flagged_comment)
);

-- Joint table below.
CREATE TABLE flag_comments(
    flagged_comment BOOLEAN NULL,
    comment_id SERIAL,
    PRIMARY KEY(flagged_comment),
    FOREIGN KEY(comment_id) REFERENCES comments(comment_id)
);

INSERT INTO community (com_name, user_id, com_total_users)
VALUES('Test Sub 1', 1, 1);
INSERT INTO community (com_name, user_id, com_total_users)
VALUES('Test Sub 2', 1, 1);
INSERT INTO community (com_name, user_id, com_total_users)
VALUES('Test Sub 3', 1, 1);
INSERT INTO community (com_name, user_id, com_total_users)
VALUES('Test Sub 4', 1, 1);

INSERT INTO posts (post_title, post_link, post_text, post_rating, com_id, user_id)
VALUES('Test Post 1', 'test_link_1', 'Test text for post 1', 1, 1, 1);
INSERT INTO posts (post_title, post_link, post_text, post_rating, com_id, user_id)
VALUES('Test Post 2', 'test_link_2', 'Test text for post 2', 2, 2, 1);
INSERT INTO posts (post_title, post_link, post_text, post_rating, com_id, user_id)
VALUES('Test Post 3', 'test_link_3', 'Test text for post 3', 3, 3, 1);
INSERT INTO posts (post_title, post_link, post_text, post_rating, com_id, user_id)
VALUES('Test Post 4', 'test_link_4', 'Test text for post 4', 4, 4, 1);

INSERT INTO comments (comment_text, flagged_comment, comment_rating, reply_id)
VALUES ('Comment Post 1', true, 3, 2);