import nfl_data_py as nfl
import time
import os

def main():
    # Look into how nfl_data_py works   
    start_time = time.time()

    # Finding the players with the most passing yards and rushing yards in the last decade
    
    decade = [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
  
    decade_data = nfl.import_seasonal_data(decade)
    df = decade_data.reset_index()

    os.system('cls' if os.name == 'nt' else 'clear')

    max_passing_yards = 0
    max_passer_id = ''
    max_rushing_yards = 0
    max_rusher_id = ''

    for index, row in df.iterrows():
        if row['passing_yards'] > max_passing_yards:
            max_passing_yards = row['passing_yards']
            max_passer_id = row['player_id']
        if row['rushing_yards'] > max_rushing_yards:
            max_rushing_yards = row['rushing_yards']
            max_rusher_id = row['player_id']

    play = nfl.import_rosters(decade)
    dfp = play.reset_index()
    f1 = 0
    f2 = 0
    for index, row in dfp.iterrows():
        if row['player_id'] == max_passer_id and f1 == 0:
            print(row['player_name'], row['team'],  f'{max_passing_yards} passing yards')
            f1 += 1
        if row['player_id'] == max_rusher_id and f2 == 0:
            print(row['player_name'], row['team'], f'{max_rushing_yards} rushing yards')
            f2 += 1
        
    print("--- %s seconds ---" % (time.time() - start_time))


    return 0

if __name__ == '__main__':
    main()
