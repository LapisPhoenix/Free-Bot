import sqlite3
from settings import database_name, Leveling
from tools import Xp
import random

name = (
    database_name.replace(' ', '_') if database_name.endswith(".db") else database_name.replace(' ', '_') + ".db"
)  # Sets the name of the database, makes sure it ends with .db
debug = False  # Debug mode, useless


def create_database():
    #  Creates the database for users.

    db = sqlite3.connect(name)
    curs = db.cursor()

    curs.execute(
        f"CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, warns INTEGER, mutes INTEGER, kicks INTEGER, bans INTEGER, xp INTEGER, level INTEGER)"
    )  # Creates the table with ID, username, warns, mutes, kicks, bans, and currency

    if debug:
        print("Database created successfully.")

    db.commit()
    curs.close()
    db.close()


def add_user(id: int, username: str, warns: int, mutes: int, kicks: int, bans: int, xp: int, level: int):
    """Attempts to add a user to the database."""

    db = sqlite3.connect(name)
    curs = db.cursor()

    curs.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (id, username, warns, mutes, kicks, bans, xp, level))

    if debug:
        print("User added successfully.")

    db.commit()
    curs.close()
    db.close()


def remove_user(id: int):
    """Attempts to remove a user from the database."""

    db = sqlite3.connect(name)
    curs = db.cursor()

    curs.execute(f"DELETE FROM users WHERE id = {id}")

    if debug:
        print("User removed successfully.")

    db.commit()
    curs.close()
    db.close()


def add_warn(id: int):
    """Attempts to add a warn to a user."""

    db = sqlite3.connect(name)
    curs = db.cursor()

    curs.execute(f"SELECT warns FROM users WHERE id = {id}")
    current_warns = curs.fetchone()
    new_warns = current_warns[0] + 1

    curs.execute(f"UPDATE users SET warns = {new_warns} WHERE id = {id}")

    if debug:
        print("Warn added successfully.")

    db.commit()
    curs.close()
    db.close()


def remove_warn(id: int):
    """Attempts to remove a warn from a user."""

    db = sqlite3.connect(name)
    curs = db.cursor()

    curs.execute(f"SELECT warns FROM users WHERE id = {id}")

    current_warns = curs.fetchone()
    new_warns = current_warns[0] - 1

    curs.execute(f"UPDATE users SET warns = {new_warns} WHERE id = {id}")

    if debug:
        print("Warn removed successfully.")

    db.commit()
    curs.close()
    db.close()


def add_mute(id: int):
    """Attempts to add a mute to a user."""

    db = sqlite3.connect(name)
    curs = db.cursor()

    curs.execute(f"SELECT mutes FROM users WHERE id = {id}")
    current_mutes = curs.fetchone()
    new_mutes = current_mutes[0] + 1

    curs.execute(f"UPDATE users SET mutes = {new_mutes} WHERE id = {id}")

    db.commit()
    curs.close()
    db.close()


def add_kick(id: int):
    """Attempts to add a kick to a user."""

    db = sqlite3.connect(name)
    curs = db.cursor()

    curs.execute(f"SELECT kicks FROM users WHERE id = {id}")
    current_kicks = curs.fetchone()
    new_kicks = current_kicks[0] + 1

    curs.execute(f"UPDATE users SET kicks = {new_kicks} WHERE id = {id}")

    db.commit()
    curs.close()
    db.close()


def add_bans(id: int):
    """Attempts to add a ban to a user."""

    db = sqlite3.connect(name)
    curs = db.cursor()

    curs.execute(f"SELECT bans FROM users WHERE id = {id}")
    current_bans = curs.fetchone()
    new_bans = current_bans[0] + 1

    curs.execute(f"UPDATE users SET bans = {new_bans} WHERE id = {id}")

    db.commit()
    curs.close()
    db.close()


def get_warns(id: int):
    """Attempts to get the warns of a user."""

    db = sqlite3.connect(name)
    curs = db.cursor()

    curs.execute(f"SELECT warns FROM users WHERE id = {id}")
    warns = curs.fetchone()

    db.commit()
    curs.close()
    db.close()

    return warns[0]


def get_mutes(id: int):
    """Attempts to get the mutes of a user."""

    db = sqlite3.connect(name)
    curs = db.cursor()

    curs.execute(f"SELECT mutes FROM users WHERE id = {id}")
    mutes = curs.fetchone()

    db.commit()
    curs.close()
    db.close()

    return mutes[0]


def get_kicks(id: int):
    """Attempts to get the kicks of a user."""

    db = sqlite3.connect(name)
    curs = db.cursor()

    curs.execute(f"SELECT kicks FROM users WHERE id = {id}")
    kicks = curs.fetchone()

    db.commit()
    curs.close()
    db.close()

    return kicks[0]


def get_bans(id: int):
    """Attempts to get the bans of a user."""

    db = sqlite3.connect(name)
    curs = db.cursor()

    curs.execute(f"SELECT bans FROM users WHERE id = {id}")
    bans = curs.fetchone()

    db.commit()
    curs.close()
    db.close()

    return bans[0]


def isindatabase(id: int):
    """Checks if a user is in the database."""

    db = sqlite3.connect(name)
    curs = db.cursor()

    curs.execute(f"SELECT id FROM users WHERE id = {id}")
    result = curs.fetchone()

    curs.close()
    db.close()

    if result is None:
        return False
    else:
        return True


def add_level(id: int):
    """Level up a user"""

    db = sqlite3.connect(name)
    curs = db.cursor()

    curs.execute(f"SELECT level FROM users WHERE id = {id}")

    level = curs.fetchone()
    level = level[0] + 1

    curs.execute(f"UPDATE users SET level = {level} WHERE id = {id}")

    curs.execute(f"UPDATE users SET xp = 0 WHERE id = {id}")

    db.commit()
    curs.close()
    db.close()


def add_xp(id: int, xp: int = random.randint(Leveling.min_xp, Leveling.max_xp)):
    """Adds xp to a user."""

    db = sqlite3.connect(name)
    curs = db.cursor()

    curs.execute(f"SELECT xp FROM users WHERE id = {id}")

    current_xp = curs.fetchone()

    curs.execute(f"SELECT level FROM users WHERE id = {id}")
    level = curs.fetchone()

    if current_xp[0] >= Xp.calc_xp(level[0]):
        add_level(id)
    else:
        new_xp = current_xp[0] + xp

        curs.execute(f"UPDATE users SET xp = {new_xp} WHERE id = {id}")

    db.commit()
    curs.close()
    db.close()


def get_level(id: int):
    """Gets the level of a user."""

    db = sqlite3.connect(name)
    curs = db.cursor()

    curs.execute(f"SELECT level FROM users WHERE id = {id}")
    level = curs.fetchone()

    db.commit()
    curs.close()
    db.close()

    return level[0]


def get_xp(id: int):
    """Gets the xp of a user."""

    db = sqlite3.connect(name)
    curs = db.cursor()

    curs.execute(f"SELECT xp FROM users WHERE id = {id}")
    xp = curs.fetchone()

    db.commit()
    curs.close()
    db.close()

    return xp[0]


def leaderboard():
    """Gets top 10 users in the server."""

    db = sqlite3.connect(name)
    curs = db.cursor()

    curs.execute("SELECT id, username, level, xp FROM users ORDER BY level DESC")
    data = curs.fetchmany(10)

    db.commit()
    curs.close()
    db.close()

    return data
