-- Database initialization script for TimescaleDB
-- Run this after creating the database

-- Enable TimescaleDB extension
CREATE EXTENSION IF NOT EXISTS timescaledb;

-- Create hypertables for time-series data
SELECT create_hypertable('price_history', 'timestamp', if_not_exists => TRUE);
SELECT create_hypertable('onchain_metrics', 'timestamp', if_not_exists => TRUE);
SELECT create_hypertable('sentiment_data', 'timestamp', if_not_exists => TRUE);

-- Create indexes for better query performance
CREATE INDEX IF NOT EXISTS idx_price_history_coin_id ON price_history(coin_id);
CREATE INDEX IF NOT EXISTS idx_onchain_metrics_coin_id ON onchain_metrics(coin_id);
CREATE INDEX IF NOT EXISTS idx_sentiment_data_coin_id ON sentiment_data(coin_id);

-- Create materialized view for daily aggregates
CREATE MATERIALIZED VIEW IF NOT EXISTS daily_coin_stats AS
SELECT 
    coin_id,
    time_bucket('1 day', timestamp) AS day,
    first(close, timestamp) AS open,
    max(close) AS high,
    min(close) AS low,
    last(close, timestamp) AS close,
    sum(volume) AS volume
FROM price_history
GROUP BY coin_id, day;

-- Refresh policy for materialized view
SELECT add_continuous_aggregate_policy('daily_coin_stats',
    start_offset => INTERVAL '3 days',
    end_offset => INTERVAL '1 hour',
    schedule_interval => INTERVAL '1 hour',
    if_not_exists => TRUE
);

-- Create function to clean old data (retention policy)
CREATE OR REPLACE FUNCTION cleanup_old_data() RETURNS void AS $$
BEGIN
    -- Keep only 2 years of price history
    DELETE FROM price_history WHERE timestamp < NOW() - INTERVAL '2 years';
    
    -- Keep only 1 year of on-chain metrics
    DELETE FROM onchain_metrics WHERE timestamp < NOW() - INTERVAL '1 year';
    
    -- Keep only 6 months of sentiment data
    DELETE FROM sentiment_data WHERE timestamp < NOW() - INTERVAL '6 months';
    
    -- Keep only 3 months of system logs
    DELETE FROM system_logs WHERE timestamp < NOW() - INTERVAL '3 months';
END;
$$ LANGUAGE plpgsql;

-- Schedule cleanup to run weekly
-- Note: This requires pg_cron extension
-- CREATE EXTENSION IF NOT EXISTS pg_cron;
-- SELECT cron.schedule('cleanup-old-data', '0 3 * * 0', 'SELECT cleanup_old_data()');
