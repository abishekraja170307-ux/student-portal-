import os
import sqlite3
import tempfile
import unittest

import database
from app import app


class AppCrudTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.original_cwd = os.getcwd()
        os.chdir(self.temp_dir.name)

    def tearDown(self):
        os.chdir(self.original_cwd)
        self.temp_dir.cleanup()

    def test_database_init_creates_required_tables(self):
        database.init_db()

        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")
        tables = {row[0] for row in cursor.fetchall()}
        conn.close()

        self.assertTrue({"users", "requests", "chats", "codes", "modules"}.issubset(tables))

    def test_module_crud_flow(self):
        client = app.test_client()

        with client.session_transaction() as session:
            session["user"] = "alice"

        resp = client.post("/add_module", data={"title": "Python", "description": "Basics"})
        self.assertEqual(resp.status_code, 302)

        resp = client.get("/dashboard")
        self.assertEqual(resp.status_code, 200)
        self.assertIn(b"Python", resp.data)

        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM modules WHERE user_name=? AND title=?", ("alice", "Python"))
        module_id = cursor.fetchone()[0]
        conn.close()

        resp = client.post(f"/delete_module/{module_id}")
        self.assertEqual(resp.status_code, 302)

        resp = client.get("/dashboard")
        self.assertEqual(resp.status_code, 200)
        self.assertNotIn(b"Python", resp.data)


if __name__ == "__main__":
    unittest.main()
