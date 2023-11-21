points_tally = [{"team": "GT", "tally": [1,1,0,1,1], "cons_wins": 0},
{"team": "A", "tally": [1,1,0,1,1], "cons_wins": 0},
{"team": "C", "tally": [1,0,1,1,1], "cons_wins": 0},
{"team": "D", "tally": [1,1,1,1,1], "cons_wins": 0},
{"team": "E", "tally": [1,1,1,1,0], "cons_wins": 0},
{"team": "F", "tally": [1,1,1,0,1], "cons_wins": 0}]

max_count = 0

for team_list in points_tally:
    cons_count = 0
    pt_list = team_list["tally"]
    count= 0
    for point in pt_list:
        if point == 1:
            count += 1
        else:
            count = 0
        cons_count = max(count, cons_count)
    team_list["cons_wins"] = cons_count
    if team_list["cons_wins"] > max_count:
        max_count = team_list["cons_wins"]
        team_name = team_list["team"]

print(points_tally)
print(max_count, team_name)
