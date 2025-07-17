CREATE TABLE IF NOT EXISTS raw_telegram_messages (
    id SERIAL PRIMARY KEY,
    channel_name TEXT NOT NULL,
    message_date DATE NOT NULL,
    message_json JSONB NOT NULL
); 