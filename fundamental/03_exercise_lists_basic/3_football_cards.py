players_with_red_card = input()
flag = False
a_team_players = 11
b_team_players = 11
players_with_red_card_list = players_with_red_card.split(" ")
players_with_red_card_list = list(dict.fromkeys(players_with_red_card_list))
for player in players_with_red_card_list:
    if "A" in player:
        a_team_players -= 1
    elif "B" in player:
        b_team_players -= 1
    if a_team_players < 7 or b_team_players < 7:
        flag = True
        break

print(f"Team A - {a_team_players}; Team B - {b_team_players}")
if flag:
    print("Game was terminated")
