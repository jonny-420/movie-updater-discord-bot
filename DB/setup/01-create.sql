CREATE TABLE member(
    id SERIAL PRIMARY KEY,
    username varchar(500)
);

CREATE TABLE genres(
    id SERIAL PRIMARY KEY,
    genre_id BIGINT,
    genre varchar(250)
);

CREATE TABLE subscription(
    id SERIAL PRIMARY KEY,
    genre_id BIGINT REFERENCES genres(id),
    user_id SERIAL REFERENCES member(id)
);