
def TS(POINT:int, FGA:int, FTA:int) -> float:
    return round(POINT/(2*(FGA+0.44*FTA)),2)
    
def EFG(POINT:int, FGA:int) -> float:
    return round(POINT/(2*FGA),2)

""" 
USG is calculated per game
both player stats and team stats per game requrie:
1. FGA  2.FTA  3.TO  4.mins
"""
def USG(player_stats:dict, team_stats:dict) -> float:
    player_aspect = (player_stats['FGA'] + 0.44 * player_stats['FTA'] + player_stats['TO']) / player_stats['mins']
    team_aspect = (team_stats['FGA'] + 0.44 * team_stats['FTA'] + team_stats['TO']) / (team_stats['mins']/5)
    return round(player_aspect / team_aspect, 2)

""" 
AST is calculated per game
both player stats and team stats per game requrie:
1. FGM  2.mins
additionally, player stats need 1.AST
"""
def AST(player_stats:dict, team_stats:dict) -> float:
    return round(player_stats['AST'] / ((player_stats['mins']/(team_stats['mins']/5)) * team_stats['FGM'] - player_stats['FGM']), 2)