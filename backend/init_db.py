#!/usr/bin/env python3
"""
AlgoForge Database Initializer
Creates required tables (users, registration_logs, submission_logs)
and migrates any existing registered_users.json records into the database.
"""
import os
import json
import sys

# Ensure backend package can be imported
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from backend.database import init_db, db_create_user, db_get_all_users, db_log_registration, engine

def main():
    print("[1/3] Initializing AlgoForge database tables on target database...")
    init_db()

    # Migrate any existing local registered_users.json into database if present
    users_file = os.path.join(os.path.dirname(__file__), "registered_users.json")
    migrated = 0
    if os.path.exists(users_file):
        try:
            with open(users_file, "r", encoding="utf-8") as f:
                data = json.load(f)
            for email, u in data.items():
                db_create_user(
                    email=email,
                    username=u.get("username", email.split("@")[0]),
                    password=u.get("password", "TestPass123!"),
                    avatar=u.get("avatar"),
                    theme=u.get("theme", "orange")
                )
                db_log_registration(
                    email=email,
                    username=u.get("username", email.split("@")[0]),
                    status="MIGRATED_FROM_FILE"
                )
                migrated += 1
            print(f"[2/3] Migrated {migrated} registered user(s) into database.")
        except Exception as e:
            print(f"[2/3] Warning during migration: {e}")
    else:
        print("[2/3] No legacy registered_users.json found to migrate.")

    users = db_get_all_users()
    print(f"[3/3] Database initialization complete! {len(users)} user(s) currently stored in database:")
    for u in users:
        print(f"  - {u['username']} ({u['email']}): Score={u['score']}, Status={u['status']}")

if __name__ == "__main__":
    main()
