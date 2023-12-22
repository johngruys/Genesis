import pandas as pd
import numpy as np
from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.endpoints import commonplayerinfo
import helpers

career = playercareerstats.PlayerCareerStats(player_id='203999')
lebron = commonplayerinfo.CommonPlayerInfo(player_id=2544)

# Pandas data frame
# career.get_data_frames()[0]

# Dictionary
# career.get_dict()
# print(career.get_dict())

# Data Frame example
# lebron_df = lebron.get_data_frames()
# print(lebron_df[0])

# id = helpers.get_id('lebron')
# print(players.find_players_by_full_name('lebron james')[0]["id"])
# print(id)
print(helpers.get_id("larry bird"))
