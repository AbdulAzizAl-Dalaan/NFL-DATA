import nfl_data_py as nfl
import time
import os
from tqdm import tqdm

def main():
    # Look into how nfl_data_py works   
    start_time = time.time()

    # Finding the players with the most passing yards in the last decade
    
    decade = [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
  
    decade_data = nfl.import_seasonal_data(decade)
    df = decade_data.reset_index()

    play = nfl.import_rosters(decade)
    dfp = play.reset_index()
    
    os.system('cls' if os.name == 'nt' else 'clear')

    df_dict = df.to_dict('records')
    dfp_dict = dfp.to_dict('records')
    
    id_passing_yards = []
    passing_yards = []
    player_name = ''

    for i in tqdm(range(len(df_dict))):
        id_passing_yards.append([df_dict[i]['player_id'], df_dict[i]['passing_yards']])
        passing_yards.append(df_dict[i]['passing_yards'])

    maxyds = max(passing_yards)
    maxid = id_passing_yards[passing_yards.index(maxyds)][0]

    for i in tqdm(range(len(dfp_dict))):
        if dfp_dict[i]['player_id'] == maxid:
            player_name = dfp_dict[i]['player_name']
            break

    print(player_name, maxyds)

    print("--- %s seconds ---" % (time.time() - start_time))

    return 0

if __name__ == '__main__':
    main()
