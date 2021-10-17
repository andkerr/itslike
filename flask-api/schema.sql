DROP TABLE IF EXISTS companies;
DROP TABLE IF EXISTS objects;
DROP TABLE IF EXISTS prev_indices;

CREATE TABLE companies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company TEXT NOT NULL
);

CREATE TABLE objects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    obj TEXT NOT NULL
);

CREATE TABLE prev_indices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    prev_company INTEGER,
    prev_obj INTEGER
);

INSERT INTO companies (
    company
)
VALUES
    (
        "Dropbox"
    ),
    (
        "McDonalds"
    ),
    (
        "Spotify"
    ),
    (
        "Instagram"
    ),
    (
        "Airbnb"
    );

INSERT INTO objects (
    obj
)
VALUES
    (
        "Kittens"
    ),
    (
        "Blockchain"
    ),
    (
        "Machine Learning"
    ),
    (
        "Disruptive Innovation"
    ),
    (
        "Oreo Cookies"
    ),
    (
        "Parking Spots"
    );