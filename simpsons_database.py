#Author: Kevin C. Escobedo
#Email: escobedo001@gmail.com
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

    def get_episode_number(self, title:str) -> int:
        '''Finds the total episode number based on the input title'''
        self.cursor.execute('''SELECT * FROM simpsons_episodes WHERE title=?''', (title,))
        data = self.cursor.fetchall()
        try:
            return data[0][0]
        except IndexError:
            return -1

    def get_episode_title(self, total_num:int) -> str:
        '''Finds the episode title based on input number'''
        self.cursor.execute('''SELECT * FROM simpsons_episodes WHERE episode=?''', (total_num,))
        data = self.cursor.fetchall()
        try:
            return data[0][1]
        except IndexError:
            return "No Episode Found"

    def close_connection(self):
        '''Closes the connection to the database'''
        self.db.commit()
        self.db.close()


def add_episodes(sd: SimpsonsDatabase) -> None:
    '''Adds episodes to the Database'''
    season_num = 1
    while True:
        try:
            file = open("titles/season_{}_titles.txt".format(season_num, "r"))
            sd.create_table("simpsons_season_{}".format(season_num))
            info = file.readlines()
            file.close()
            for i, title in enumerate(info):
                sd.insert_episode("simpsons_season_{}".format(season_num), i+1, title.strip())
            season_num += 1
        except FileNotFoundError:
            break

def add_total(sd: SimpsonsDatabase) -> None:
    '''Adds every episode'''
    file = open("titles/episode_titles.txt", "r")
    sd.create_table("simpsons_episodes")
    info = file.readlines()
    file.close()
    for i,title in enumerate(info):
        sd.insert_episode("simpsons_episodes", i+1, title.strip())

if __name__ == "__main__":
    sd = SimpsonsDatabase()
    sd.close_connection()
