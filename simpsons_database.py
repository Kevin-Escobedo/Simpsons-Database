import sqlite3

class SimpsonsDatabase:
    def __init__(self):
        self.db = sqlite3.connect("simpsons_episodes.db")
        self.cursor = self.db.cursor()

    def create_table(self, table_name:str) -> None:
        '''Creates a new table in the database'''
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS {}(episode INTEGER PRIMARY KEY, title TEXT)'''.format(table_name))

        self.db.commit()

    def insert_episode(self, table_name:str, episode:int, title:str) -> None:
        '''Inserts a new episode into the database'''
        try:
            self.cursor.execute('''INSERT INTO {}(episode, title) VALUES(?, ?)'''.format(table_name), (episode, title))
        except sqlite3.IntegrityError:
            pass

    def close_connection(self):
        '''Closes the connection to the database'''
        self.db.commit()
        self.db.close()


if __name__ == "__main__":
    sd = SimpsonsDatabase()
    sd.create_table("simpsons_season_1")

    with open("season_1_titles.txt", "r") as info:
        for i, title in enumerate(info.readlines()):
            sd.insert_episode("simpsons_season_1", i+1, title)

    sd.close_connection()
