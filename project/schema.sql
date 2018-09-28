drop table if exists user;
drop table if exists topic;
drop table if exists subscription;
drop table if exists post;
drop table if exists type;
drop table if exists vote;
drop table if exists votertype;
drop table if exists notification;
drop table if exists groups;
drop table if exists membership;


CREATE TABLE user(
id              INT     PRIMARY KEY, 
username        TEXT    NOT NULL, 
password        TEXT    NOT NULL, 
fname           TEXT    NOT NULL, 
lname           TEXT    NOT NULL
);

CREATE TABLE topic (
id              INT    PRIMARY KEY,
name            TEXT    NOT NULL,
time_created    DATE    NOT NULL,
created_by      TEXT    NOT NULL, 
FOREIGN KEY(created_by) REFERENCES user(username)
);

CREATE TABLE subscription (
subscription_id         INT         PRIMARY KEY,
user_id                 INT         NOT NULL, 
topic_id                INT         NOT NULL,
FOREIGN KEY(user_id) REFERENCES user(id),
FOREIGN KEY(topic_id) REFERENCES topic(id)
);

CREATE TABLE post (
id              INT         PRIMARY KEY,
topic_id        INT         NOT NULL,
posted_by       TEXT        NOT NULL,
title           TEXT        NOT NULL, 
main_body       TEXT        NOT NULL,
time_posted     DATE        NOT NULL, 
edited          BOOLEAN, 
time_edited     DATE,

FOREIGN KEY(posted_by) REFERENCES user(id),
FOREIGN KEY(topic_id) REFERENCES topic(id)

);

CREATE TABLE type (
id              INT     PRIMARY KEY,
type_name       TEXT    NOT NULL
);

CREATE TABLE vote (
id              INT     PRIMARY KEY,
type_id         INT     NOT NULL,
upvote          INT     NOT NULL,
downvote        INT     NOT NULL,

FOREIGN KEY(type_id)  REFERENCES type(id)
);

CREATE TABLE votertype (
id              INT     PRIMARY KEY,
vote_id         INT     NOT NULL,
user_id         INT     NOT NULL,
type            TEXT    NOT NULL,

FOREIGN KEY(vote_id)  REFERENCES vote(id),
FOREIGN KEY(user_id)  REFERENCES user(id)
);

CREATE TABLE notification (
id              INT     PRIMARY KEY,
title           TEXT    NOT NULL,
user_id         INT     NOT NULL,
body            TEXT    NOT NULL,
target          TEXT    NOT NULL,
target_id       INT     NOT NULL,

FOREIGN KEY(target_id)  REFERENCES type(id),
FOREIGN KEY(user_id)  REFERENCES user(id)
);

CREATE TABLE groups (
id              INT     PRIMARY KEY,
name            TEXT    NOT NULL,
created_by      INT     NOT NULL,

FOREIGN KEY(created_by) REFERENCES user(id)
);

CREATE TABLE membership (
membership_id   INT     PRIMARY KEY,
group_id        INT     NOT NULL,
user_id         INT     NOT NULL,

FOREIGN KEY(group_id)  REFERENCES groups(id),
FOREIGN KEY(user_id)   REFERENCES user(id)
);