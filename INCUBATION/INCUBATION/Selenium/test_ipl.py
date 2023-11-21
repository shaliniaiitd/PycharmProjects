# Goto – IPL website-> Tables menu-> find which team won most matches.Consider Last 5 matches results and find max consecutive wins.

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.get('https://www.iplt20.com/')


# Given every team has scores for 5 matches, select the team(s) that has maximum number of consecutive wins

score = ["team1", 1,1,0,1,1]
wins = 0
win_count = {}
for i in range(len(score)-1):
    if score[i] == 1 and score[i+1] == 1:
        wins += 1
    else:
        if wins !=0:
            wins =0
    win_count.update["team1": wins]

