DROP TABLE IF EXISTS posts;
DROP TABLE IF EXISTS user_accounts;

CREATE TABLE user_accounts (
    id SERIAL PRIMARY KEY,
    username text,
    email_address text
);

INSERT INTO user_accounts (username, email_address) VALUES ('John Lennon', 'john@beatles.net');
INSERT INTO user_accounts (username, email_address) VALUES ('Paul McCartney', 'paul@beatles.net');


CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    post_title text,
    post_contents text,
    post_views int,
    user_account_id int,
    constraint fk_user_account foreign key(user_account_id)
        references user_accounts(id)
        on delete cascade
);

INSERT INTO posts (post_title, post_contents, post_views, user_account_id) VALUES ('Paul is a traitor', 'He left the band', 20, 1);
INSERT INTO posts (post_title, post_contents, post_views, user_account_id) VALUES ('John is full of it', 'I left because of him', 50, 2);
