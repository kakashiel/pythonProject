CREATE DATABASE doc_qa;
CREATE USER doc_qa WITH PASSWORD 'doc_qa_pwd';
ALTER ROLE doc_qa SET client_encoding TO 'utf8';
ALTER ROLE doc_qa SET default_transaction_isolation TO 'read committed';
ALTER ROLE doc_qa SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE doc_qa TO doc_qa;
\q;