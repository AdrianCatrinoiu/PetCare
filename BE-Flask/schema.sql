DROP TABLE IF EXISTS post;
DROP TABLE IF EXISTS temperature;
DROP TABLE IF EXISTS food;
DROP TABLE IF EXISTS water;



CREATE TABLE post (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  author_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  title TEXT NOT NULL,
  body TEXT NOT NULL,
  FOREIGN KEY (author_id) REFERENCES user (id)
);

CREATE TABLE temperature (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  level REAL NOT NULL
);

CREATE TABLE food (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  changed_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  level REAL NOT NULL
);

CREATE TABLE water (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  changed_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  level REAL NOT NULL
);