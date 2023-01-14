import nfl_data_py as nfl
import time
import os
from tqdm import tqdm

def main():
    # Look into how nfl_data_py works   
    start_time = time.time()

    # Finding the players with the most passing, receiving, and rushing yards in the last decade
      
    '''
    The following code is used to create the csv files that are used in the code below
    
    decade = [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]

    decade_data = nfl.import_seasonal_data(decade)
    df = decade_data.reset_index()

    play = nfl.import_rosters(decade)
    dfp = play.reset_index()

    df.to_csv('season_decade_data.csv')
    dfp.to_csv('decade_players.csv')

    '''

    decade_seasons = open('season_decade_data.csv', 'r')
    header = decade_seasons.readline()
    decade_seasons_lines = decade_seasons.readlines()

    decade_data = open('decade_players.csv', 'r')
    header = decade_data.readline()
    decade_data_lines = decade_data.readlines()

    max_passing_yds = 0
    max_receiving_yds = 0
    max_rushing_yds = 0

    for i in tqdm(range(len(decade_seasons_lines))):

        dsl_list = decade_seasons_lines[i].split(',')
    
        if float(dsl_list[6]) > max_passing_yds:
            max_passing_yds = float(dsl_list[6])
            max_passer_id = dsl_list[1] 

        if float(dsl_list[30]) > max_receiving_yds:
            max_receiving_yds = float(dsl_list[30])
            max_receiver_id = dsl_list[1]

        if float(dsl_list[21]) > max_rushing_yds:
            max_rushing_yds = float(dsl_list[21])
            max_rusher_id = dsl_list[1]
        

    for i in tqdm(range(len(decade_data_lines))):

        ddl_list = decade_data_lines[i].split(',')

        if ddl_list[14] == max_passer_id:
            passer_player_name = ddl_list[7]
        
        if ddl_list[14] == max_receiver_id:
            receiver_player_name = ddl_list[7]

        if ddl_list[14] == max_rusher_id:
            rusher_player_name = ddl_list[7]
        

    print(max_passer_id, passer_player_name, max_passing_yds)
    print(max_receiver_id, receiver_player_name, max_receiving_yds)
    print(max_rusher_id, rusher_player_name, max_rushing_yds)


    print("--- %s seconds ---" % (time.time() - start_time))

    return 0

if __name__ == '__main__':
    main()
