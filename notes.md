# Notes on the Data

VOTER_AVERAGES_URL: 'https://projects.fivethirtyeight.com/congress-tracker-data/csv/averages.csv'

## Voter Averages CSV
chamber - house or senate
bioguide - representative-specific ID
last_name - last name of representative
state - state of representative
party - R or D
district - area within state they represent (blank for senators)
votes - number of things they have voted on
agree_pct - * vote agreed with trump position/ * votes
predicted_agree - prediction for agree_pct
net_trump_vote - trump's percentage lead over Clinton in this district's presidential popular vote

INDIVIDUAL_VOTES_URL: 'https://projects.fivethirtyeight.com/congress-tracker-data/csv/vote_predictions.csv'

## INDIVIDUAL VOTE CSV
bill_id - Which bill they voted on
roll_id - A specific ID assigned for roll call votes
last_name - last name of representative
state - state of representative
chamber - house/senate
voted_at - date and time of voting
bioguide - representative-specific ID
vote - how they voted (yes/no)
trump_position - support/oppose
agree - whether or not the vote agreed with trump's position (1 yes, 0 no)
yesno - voting record, with 0 = no, 1 = yes, and -1 = not voting
predicted_probability - the likelihood of agreement with Trump's position