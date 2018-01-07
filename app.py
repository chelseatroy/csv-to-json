from flask import Flask
from flask import request
import csv
import json
import urllib2

app = Flask(__name__)

VOTER_AVERAGES_URL = 'https://projects.fivethirtyeight.com/congress-tracker-data/csv/averages.csv'
DATA_COLUMNS = {
    "chamber": 0,
    "bioguide": 1,
    "last_name": 2,
    "state": 3,
    "district": 4,
    "party": 5,
    "votes": 6,
    "agree_pct": 7,
    "predicted_agree": 8,
    "net_trump_vote": 9
}

@app.route('/')
def entry_point():
    representative_id = request.args.get('bioguide')

    # Make sure the client specified a representative
    if not representative_id:
        error_response = {"error": "Please include the bioguide of the representative as a query param."}
        return json.dumps(error_response), 422

    #Collect the voter averages data from an endpoint and shovel into a local file
    connection = urllib2.urlopen(url=VOTER_AVERAGES_URL)
    success_response = connection.read()
    filename = "voter_averages.csv"
    file_ = open(filename, 'w')
    file_.write(success_response)
    file_.close()

    with open(filename, 'rb') as csvfile:
        # Track the header row
        processed_header = False

        csv_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        averages = {}

        for row in csv_reader:
            if not processed_header:
                processed_header = True
                continue

            chamber = row[DATA_COLUMNS["chamber"]]
            bioguide = row[DATA_COLUMNS["bioguide"]]
            last_name = row[DATA_COLUMNS["last_name"]]
            state = row[DATA_COLUMNS["state"]]
            district = row[DATA_COLUMNS["district"]]
            party = row[DATA_COLUMNS["party"]]
            votes = row[DATA_COLUMNS["votes"]]
            percent_agree = row[DATA_COLUMNS["agree_pct"]]
            predicted_agreement = row[DATA_COLUMNS["predicted_agree"]]
            net_trump_vote = row[DATA_COLUMNS["net_trump_vote"]]

            averages[bioguide] = {
                "chamber": chamber,
                "last_name": last_name,
                "state": state,
                "district": district,
                "party": party,
                "votes": votes,
                "percent_agree": percent_agree,
                "predicted_agreement": predicted_agreement,
                "net_trump_vote": net_trump_vote,
            }

    if not averages[representative_id]:
        error_response = {"error": "That bioguide doesn't match any representative in our data."}
        return json.dumps(error_response), 422

    success_response = json.dumps(averages[representative_id])
    return success_response


if __name__ == '__main__':
    app.run(debug=True)
