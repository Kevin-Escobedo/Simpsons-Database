#Author: Kevin C. Escobedo
#Email: escobedo001@gmail.com

def combine_files() -> None:
    '''Combines all title files into one'''
    file = open("episode_titles.txt", "w")
    num = 1
    while True:
        try:
            season_file = open("season_{}_titles.txt".format(num), "r")
            info = season_file.readlines()
            for title in info:
                file.write("{}".format(title))
            season_file.close()
            num += 1
        except FileNotFoundError:
            file.close()
            break

if __name__ == "__main__":
    combine_files()
