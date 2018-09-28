#!/usr/bin/python3

import sqlite3

class Database():
    def __init__(self):
        self._conn = sqlite3.connect('projecttest.db')

    def _close(self):
        self._conn.commit()
        self._conn.close()    

    def create_tables(self):
        self._conn.executescript("""
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
            drop table if exists grouptopics;


            CREATE TABLE user(
            id              INTEGER     PRIMARY KEY     AUTOINCREMENT, 
            username        TEXT    NOT NULL, 
            password        TEXT    NOT NULL, 
            fname           TEXT    NOT NULL, 
            lname           TEXT    NOT NULL
            );

            CREATE TABLE topic (
            id              INTEGER    PRIMARY KEY      AUTOINCREMENT,
            name            TEXT    NOT NULL,
            time_created    DATE    NOT NULL,
            created_by      TEXT    NOT NULL, 
            FOREIGN KEY(created_by) REFERENCES user(username)
            );

            CREATE TABLE subscription (
            subscription_id         INTEGER     PRIMARY KEY     AUTOINCREMENT,
            user_id                 INT         NOT NULL, 
            topic_id                INT         NOT NULL,
            FOREIGN KEY(user_id) REFERENCES user(id),
            FOREIGN KEY(topic_id) REFERENCES topic(id)
            );

            CREATE TABLE post (
            id              INTEGER     PRIMARY KEY     AUTOINCREMENT,
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
            id              INTEGER PRIMARY KEY     AUTOINCREMENT,
            type_name       TEXT    NOT NULL
            );

            CREATE TABLE vote (
            id              INTEGER PRIMARY KEY     AUTOINCREMENT,
            type            INT     NOT NULL,   
            upvote          INT     NOT NULL,
            downvote        INT     NOT NULL,
            type_id         INT     NOT NULL, 

            FOREIGN KEY(type)  REFERENCES type(id)
            );

            CREATE TABLE votertype (
            id              INTEGER PRIMARY KEY     AUTOINCREMENT,
            vote_id         INT     NOT NULL,
            user_id         INT     NOT NULL,
            type            TEXT    NOT NULL,

            FOREIGN KEY(vote_id)  REFERENCES vote(id),
            FOREIGN KEY(user_id)  REFERENCES user(id)
            );

            CREATE TABLE notification (
            id              INTEGER PRIMARY KEY     AUTOINCREMENT,
            title           TEXT    NOT NULL,
            user_id         INT     NOT NULL,
            body            TEXT    NOT NULL,
            target          TEXT    NOT NULL,
            target_id       INT     NOT NULL,

            FOREIGN KEY(target_id)  REFERENCES type(id),
            FOREIGN KEY(user_id)  REFERENCES user(id)
            );

            CREATE TABLE groups (
            id              INTEGER PRIMARY KEY     AUTOINCREMENT,
            name            TEXT    NOT NULL,
            created_by      INT     NOT NULL,

            FOREIGN KEY(created_by) REFERENCES user(id)
            );

            CREATE TABLE membership (
            membership_id   INTEGER PRIMARY KEY     AUTOINCREMENT,
            group_id        INT     NOT NULL,
            user_id         INT     NOT NULL,

            FOREIGN KEY(group_id)  REFERENCES groups(id),
            FOREIGN KEY(user_id)   REFERENCES user(id)
            );
            
            CREATE TABLE grouptopics(
            id              INTEGER     PRIMARY KEY     AUTOINCREMENT,
            group_id        INT     NOT NULL,
            topic_id        INT     NOT NULL,
            
            FOREIGN KEY(group_id) REFERENCES groups(id),
            FOREIGN KEY(topic_id) REFERENCES topic(id)
            );
        """)

if __name__ == "__main__":
    database = Database()
    database.create_tables()