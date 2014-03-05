
-- Table: word
CREATE TABLE word ( 
    id            INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
    type          TEXT,
    word          TEXT UNIQUE,
    origin        TEXT,
    origin_code   TEXT,
    original_word TEXT,
    description   TEXT 
);


-- Table: relation
CREATE TABLE relation ( 
    id              INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
    source_word_id  INTEGER REFERENCES word ( id ),
    target_word_id  INTEGER REFERENCES word ( id ),
    connection_type INTEGER 
);


-- Index: idx_word
CREATE INDEX idx_word ON word ( 
    word 
);

