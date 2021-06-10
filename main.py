# This is a sample Python script.
import pprint

from dynamodb_json import json_util

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
THANK_YOUS_RECEIVED_KEY = 'thankYousReceived'
MONTH_KEY = '2021-05'


def load_json_file(path):

    with open(path, 'r') as fp:
        return json_util.loads("".join(fp.readlines()))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    data = load_json_file("/tmp/thankyou-data")

    league_user = []
    lottery_user = []
    none_user = []

    print("############### League Participants (number of thanks received) for month %s ##############" % MONTH_KEY)
    for item in data['Items']:
        if item['scheme'] == 'league':
            if THANK_YOUS_RECEIVED_KEY in item:
                if MONTH_KEY in item[THANK_YOUS_RECEIVED_KEY]:
                    thanks = item[THANK_YOUS_RECEIVED_KEY][MONTH_KEY]
                else:
                    thanks = []
            else:
                thanks = []
            print("%s: %s" % (item['displayName'], len(thanks)))

    print("\n\n############### Lottery Participants for month %s #########################################" % MONTH_KEY)
    for item in data['Items']:
        if item['scheme'] == 'lottery':
            if THANK_YOUS_RECEIVED_KEY in item:
                if MONTH_KEY in item[THANK_YOUS_RECEIVED_KEY]:
                    print("%s" % item['displayName'])
                    

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
