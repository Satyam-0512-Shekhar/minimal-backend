CREATE TABLE IF NOT EXISTS patients (

    id SERIAL PRIMARY KEY,

    name TEXT NOT NULL,

    age INT,

    disease TEXT
);