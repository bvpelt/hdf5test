CREATE TABLE dataset_metadata (
    id SERIAL PRIMARY KEY,
    iso_dataset TEXT,
    product TEXT,
    projection TEXT
);


CREATE TABLE grid_cells (
    id SERIAL PRIMARY KEY,
    time TIMESTAMP NOT NULL,
    y INT NOT NULL,
    x INT NOT NULL,

    station INT,
    station_value REAL,
    prediction REAL,

    UNIQUE (time, y, x)
);
