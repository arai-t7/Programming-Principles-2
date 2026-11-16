
CREATE OR REPLACE PROCEDURE add_phone(
    p_contact_name VARCHAR,
    p_phone VARCHAR,
    p_type VARCHAR
)
LANGUAGE plpgsql
AS $$
DECLARE
    v_contact_id INTEGER;
BEGIN
    SELECT id
    INTO v_contact_id
    FROM contacts
    WHERE LOWER(CONCAT_WS(' ', first_name, last_name))
          = LOWER(p_contact_name)
    LIMIT 1;

    IF v_contact_id IS NULL THEN
        RAISE EXCEPTION 'Contact % not found', p_contact_name;
    END IF;

    INSERT INTO phones (contact_id, phone, type)
    VALUES (v_contact_id, p_phone, p_type);

    RAISE NOTICE 'Phone added successfully';
END;
$$;



CREATE OR REPLACE PROCEDURE move_to_group(
    p_contact_name VARCHAR,
    p_group_name VARCHAR
)
LANGUAGE plpgsql
AS $$
DECLARE
    v_contact_id INTEGER;
    v_group_id INTEGER;
BEGIN
    SELECT id
    INTO v_contact_id
    FROM contacts
    WHERE LOWER(CONCAT_WS(' ', first_name, last_name))
          = LOWER(p_contact_name)
    LIMIT 1;

    IF v_contact_id IS NULL THEN
        RAISE EXCEPTION 'Contact % not found', p_contact_name;
    END IF;

    INSERT INTO groups (name)
    VALUES (p_group_name)
    ON CONFLICT (name) DO NOTHING;

    SELECT id
    INTO v_group_id
    FROM groups
    WHERE name = p_group_name;

    UPDATE contacts
    SET group_id = v_group_id
    WHERE id = v_contact_id;

    RAISE NOTICE 'Contact moved successfully';
END;
$$;

CREATE OR REPLACE FUNCTION search_contacts(
    p_query TEXT
)
RETURNS TABLE (
    contact_id INTEGER,
    first_name VARCHAR,
    last_name VARCHAR,
    email VARCHAR,
    phone VARCHAR,
    group_name VARCHAR
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT DISTINCT
        c.id,
        c.first_name,
        c.last_name,
        c.email,
        p.phone,
        g.name
    FROM contacts c
    LEFT JOIN phones p ON c.id = p.contact_id
    LEFT JOIN groups g ON c.group_id = g.id
    WHERE
        c.first_name ILIKE '%' || p_query || '%'
        OR c.last_name ILIKE '%' || p_query || '%'
        OR c.email ILIKE '%' || p_query || '%'
        OR p.phone ILIKE '%' || p_query || '%'
    ORDER BY c.id;
END;
$$;