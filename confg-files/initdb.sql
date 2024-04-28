create extension pg_trgm;

CREATE TABLE IF NOT EXISTS person (
    id UUID NOT NULL, 
    nickname VARCHAR(32) NOT NULL, 
    name VARCHAR(100) NOT NULL, 
    birth_date TIMESTAMP WITHOUT TIME ZONE NOT NULL, 
    stack VARCHAR(32)[], 
    search VARCHAR GENERATED ALWAYS AS (nickname || ' ' || name || ' ' || coalesce(stack)) STORED NOT NULL, 
    
    CONSTRAINT person_pkey PRIMARY KEY (id),
    CONSTRAINT person_nickname_key UNIQUE (nickname)
);

CREATE UNIQUE INDEX IF NOT EXISTS idx_person_id ON person (id);

CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_person_busca_gist ON person USING GIST (search gist_trgm_ops);