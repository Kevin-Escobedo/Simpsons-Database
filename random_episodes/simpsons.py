#Author: Kevin C. Escobedo
#Email: escobedo001@gmail.com
from random import randrange
import pickle

class RandomEpisode:
    def __init__(self):
        self.num_of_episodes = {1:13, 2:22, 3:24, 4:22, 5:22, 6:25,
                       7:25, 8:25, 9:25, 10:23, 11:22, 12:21,
                       13:22, 14:22, 15:22, 16:21, 17:22, 18:22,
                       19:20, 20:21, 21:23, 22:22, 23:22, 24:22,
                       25:22, 26:22, 27:22, 28:22, 29:21, 30:23}

        self.watch_history = self.get_watch_history()

    def get_watch_history(self) -> set:
        '''Keeps track of the episodes already watched'''
        try:
            file = open("watch_history.sim", "rb")
            watch_history = pickle.load(file)
            file.close()
            return watch_history
        except FileNotFoundError:
            return set()

    def update_watch_history(self, episode: (int, int)) -> None:
        '''Updates the watch history'''
        self.watch_history.add(episode)
        file = open("watch_history.sim", "wb")
        pickle.dump(self.watch_history, file)
        file.close()
        
    def generate_random_episode(self) -> (int, int):
        '''Randomly picks a Simpsons episode'''
        season = randrange(1, len(self.num_of_episodes)+1)
        if season == 3:
            episode = randrange(2, self.num_of_episodes[season] + 1)
        else:
            episode = randrange(1, self.num_of_episodes[season] + 1)
        return (season, episode)

    def seen_episode(self, episode: (int, int)) -> bool:
        '''Checks if the episode has been seen'''
        return episode in self.watch_history

    def pick_episode(self) -> (int, int):
        '''Returns episode not in watch history'''
        episode = self.generate_random_episode()
        seen = self.seen_episode(episode)
        while seen:
            episode = self.generate_random_episode()
            seen = self.seen_episode(episode)
        self.update_watch_history(episode)
        return episode


if __name__ == "__main__":
    r = RandomEpisode()
    episode = r.pick_episode()
    print("Season: {}\nEpisode: {}".format(episode[0], episode[1]))
