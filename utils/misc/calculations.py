#this function calculate ELO for rating
from voteofart import Table

coef = 15
denom = 400

def calc_rating(winner, looser):
    expected_score_winner = 1 / (1 + (10 ** ((looser[Table.RATING.value] - winner[Table.RATING.value]) / denom)))
    expected_score_looser = 1 / (1 + (10 ** ((winner[Table.RATING.value] - looser[Table.RATING.value]) / denom)))
    print(expected_score_winner, expected_score_looser)
    new_rat_winner = round(winner[Table.RATING.value] + coef * (1 - expected_score_winner))
    new_rat_looser = round(looser[Table.RATING.value] + coef * (0 - expected_score_looser))

    return new_rat_winner, new_rat_looser