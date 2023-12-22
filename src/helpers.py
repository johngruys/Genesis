from nba_api.stats.static import players


### Returns the NBA_API ID of a player given a name, -1 if player not found or more than one player found
def get_id(player_name):
    # Get list of players through api search
    matching_players = players.find_players_by_full_name(player_name)
    
    player_id = 0
    if (len(matching_players) == 1):
        player_id = matching_players[0]["id"]
        return player_id
    else:
        return -1
    
    