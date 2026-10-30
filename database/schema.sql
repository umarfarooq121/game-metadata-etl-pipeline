CREATE TABLE IF NOT EXISTS public.games (
    id INTEGER GENERATED ALWAYS AS IDENTITY,
    source_id VARCHAR(100) NOT NULL,
    platform VARCHAR(50) NOT NULL,
    title TEXT NOT NULL,
    genre TEXT NOT NULL,
    developer TEXT,
    publisher TEXT,
    release_date DATE,
    price NUMERIC(10, 2),
    currency VARCHAR(3),
    user_rating NUMERIC(3, 2),
    age_rating VARCHAR(30),
    image_url TEXT,
    resolved_image_url TEXT,
    local_image_path TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT games_pkey PRIMARY KEY (id),
    CONSTRAINT unique_platform_game UNIQUE (platform, source_id),
    CONSTRAINT valid_price CHECK (price >= 0),
    CONSTRAINT valid_rating CHECK (user_rating BETWEEN 0 AND 5)
);