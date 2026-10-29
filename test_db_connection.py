from database.db_connection import get_connection

try:
    with get_connection() as conn:
        print("Connected to PostgreSQL!")

        result = conn.execute(
            "SELECT current_database();"
        ).fetchone()

        print("Database:", result[0])

        result = conn.execute(
            "SELECT COUNT(*) FROM public.games;"
        ).fetchone()

        print("Games in database:", result[0])

except Exception as error:
    print("Database test failed:", error)