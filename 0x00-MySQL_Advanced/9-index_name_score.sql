-- script that create an index idx_name_first_score on
--table names and first letter of name and the score
DROP INDEX IF EXISTS idx_name_first_score ON names;
CREATE INDEX idx_name_first_score ON names (SUBSTRING(name, 1, 1) score );
