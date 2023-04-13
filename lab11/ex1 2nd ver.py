import psycopg2 as pgsql

connection=pgsql.connect(host="localhost", dbname="postgres", user="postgres", 
                         password="12345", port=5432)
cur=connection.cursor()

#PROCEDURES & functions
#1 searching by name
cur.execute("""CREATE OR REPLACE FUNCTION search_from_pb_byname(a character varying)
  RETURNS SETOF PhoneBook
AS
$$
SELECT * 
FROM PhoneBook 
WHERE name=a;
$$
language sql;
""")
#2 updating if exist inserting if not
cur.execute("""CREATE OR REPLACE PROCEDURE insert_to_pb(a character varying, b character varying, c integer)
LANGUAGE plpgsql
AS $$
DECLARE v_exists INTEGER;
BEGIN
    SELECT into v_exists (SELECT count(*) FROM public.PhoneBook WHERE name = b AND surname=a);
    IF v_exists=0 THEN
        INSERT INTO public.PhoneBook (surname, name, number) values(a, b, c);
    END IF;
	IF v_exists IS NOT NULL THEN
        UPDATE public.PhoneBook
		SET number = c
		WHERE surname = a AND name=b;
    END IF;
END;
$$;
""")
#3 inserting in loop

cur.execute("""CREATE OR REPLACE PROCEDURE insert_loop()
LANGUAGE plpgsql
AS $$
DECLARE
   m   text[];
   num int;
   arr text[] := '{{toqayev,qasym,12345},{nazarbayev,nursultan, 46465},{idont, know, 46451}}'; 
BEGIN
   FOREACH m SLICE 1 IN ARRAY arr
   LOOP
      SELECT INTO num CAST(m[3] AS INTEGER);
      INSERT INTO PhoneBook (surname, name, number) values(m[1],m[2],num);
   END LOOP;
END
$$;""")

#4pagination
cur.execute("""CREATE OR REPLACE FUNCTION paginating(a integer, b integer)
RETURNS SETOF PhoneBook
AS $$
    SELECT * FROM PhoneBook 
	ORDER BY surname
	LIMIT a OFFSET b;
$$
language sql;""")

#5deleting
cur.execute("""CREATE OR REPLACE PROCEDURE delete_from_pb(a character varying, b character varying)
LANGUAGE plpgsql
AS $$
DECLARE v_exists INTEGER;
BEGIN
    SELECT into v_exists (SELECT count(*) FROM public.PhoneBook WHERE name = b AND surname=a);
	IF v_exists IS NOT NULL THEN
        DELETE FROM PhoneBook
		WHERE surname=a AND name=b;
    END IF;
END;
$$;""")

#executing
cur.execute("""CALL insert_to_pb('fromp','tosql',465465654);
""")
cur.execute("""SELECT *
FROM search_from_pb_byname('lol');""")
print(cur.fetchall())
cur.execute("""CALL insert_to_pb('pip', 'pup', 66);""")
cur.execute("""SELECT *
FROM paginating(5, 2);""")
print(cur.fetchall())
cur.execute("""CALL delete_from_pb('fromp', 'tosql');""")
cur.execute("""CALL insert_loop();""")


connection.commit()
cur.close()
connection.close()