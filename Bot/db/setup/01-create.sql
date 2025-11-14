CREATE TABLE member(
    id varchar(500) PRIMARY KEY,
    username varchar(500)
);

CREATE TABLE genres(
    genre_id BIGINT PRIMARY KEY,
    genre varchar(250)
);

CREATE TABLE company(
    company_id BIGINT PRIMARY KEY,
    company VARCHAR(500)
);

CREATE TABLE genre_subscription(
    id SERIAL PRIMARY KEY,
    genre_id BIGINT REFERENCES genres(genre_id),
    member_id varchar(500) REFERENCES member(id) ON DELETE CASCADE
);


CREATE TABLE company_subscription(
    id SERIAL PRIMARY KEY,
    company_id BIGINT REFERENCES company(company_id),
    member_id varchar(500) REFERENCES member(id) ON DELETE CASCADE
);