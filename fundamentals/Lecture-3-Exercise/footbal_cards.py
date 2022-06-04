info = input().split(" ")
team_a_players = 11
team_b_players = 11
player_loses = []
condition = False

for card in info:
    if card not in player_loses:
        player_loses.append(card)
        if 'A' in card:
            team_a_players -= 1
        else:
            team_b_players -= 1

        if team_a_players < 7 or team_b_players < 7:
            condition = True
            break

print(f"Team A - {team_a_players}; Team B - {team_b_players}")

if condition:
    print("Game was terminated")