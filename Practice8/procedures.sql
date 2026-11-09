CREATE OR REPLACE PROCEDURE upsert_contact(
    p_name VARCHAR,
    p_phone VARCHAR
)
LANGUAGE plpgsql
AS $$
BEGIN

    IF EXISTS (
        SELECT 1
        FROM contacts
        WHERE first_name = p_name
    )
    THEN

        UPDATE contacts
        SET phone = p_phone
        WHERE first_name = p_name;

    ELSE

        INSERT INTO contacts(first_name, phone)
        VALUES(p_name, p_phone);

    END IF;

END;
$$;
CREATE OR REPLACE PROCEDURE insert_many_contacts(
    p_names TEXT[],
    p_phones TEXT[],
    INOUT p_invalid_data TEXT
)
LANGUAGE plpgsql
AS $$
DECLARE
    i INTEGER;
    total INTEGER;
BEGIN

    p_invalid_data := '';

    IF COALESCE(array_length(p_names, 1), 0)
       <> COALESCE(array_length(p_phones, 1), 0) THEN
        RAISE EXCEPTION 'Names and phones must have equal length';
    END IF;

    total := COALESCE(array_length(p_names, 1), 0);

    FOR i IN 1..total LOOP

        IF p_names[i] IS NULL
           OR p_phones[i] IS NULL
           OR p_names[i] = ''
           OR p_phones[i] !~ '^\+?[0-9]{7,15}$'
        THEN

            p_invalid_data := p_invalid_data ||
                'Invalid data: ' ||
                COALESCE(p_names[i], 'NULL') || ' - ' ||
                COALESCE(p_phones[i], 'NULL') || E'\n';

        ELSIF EXISTS (
            SELECT 1
            FROM contacts
            WHERE phone = p_phones[i]
              AND first_name <> p_names[i]
        )
        THEN

            p_invalid_data := p_invalid_data ||
                'Duplicate phone: ' ||
                p_names[i] || ' - ' ||
                p_phones[i] || E'\n';

        ELSIF EXISTS (
            SELECT 1
            FROM contacts
            WHERE first_name = p_names[i]
        )
        THEN

            UPDATE contacts
            SET phone = p_phones[i]
            WHERE first_name = p_names[i];

        ELSE

            INSERT INTO contacts(first_name, phone)
            VALUES(p_names[i], p_phones[i]);

        END IF;

    END LOOP;

END;
$$;
CREATE OR REPLACE PROCEDURE delete_contact(
    p_username VARCHAR DEFAULT NULL,
    p_phone VARCHAR DEFAULT NULL
)
LANGUAGE plpgsql
AS $$
BEGIN

    IF p_username IS NOT NULL AND p_phone IS NOT NULL THEN

        RAISE EXCEPTION 'Provide username OR phone, not both';

    ELSIF p_username IS NOT NULL THEN

        DELETE FROM contacts
        WHERE first_name = p_username;

    ELSIF p_phone IS NOT NULL THEN

        DELETE FROM contacts
        WHERE phone = p_phone;

    ELSE

        RAISE EXCEPTION 'Username or phone is required';

    END IF;

END;
$$;