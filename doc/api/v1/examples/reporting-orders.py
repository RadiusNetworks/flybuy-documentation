#  USAGE: python export_orders.py \
#   --project=<project_id> \
#   --start=<start_time> \
#   --end=<end_time> \
#   --token=<api_token> \
#   --prefix=<file_prefix>

import json, requests, sys, csv, getopt

ENDPOINT = 'https://flybuy.radiusnetworks.com/api/v1/archived_orders/'

def get_orders(project_id, start, end, token):
    orders = []
    headers = { 'Authorization' : 'Token token='+token }
    next_url = ''
    while True:
        sys.stdout.write(' . ')
        sys.stdout.flush()
        if next_url == '':
            params = {
                'project_id': project_id,
                'start_time': start,
                'end_time': end
            }
            response = requests.get(ENDPOINT, params=params, headers=headers)
        else:
            response = requests.get(next_url, headers=headers)
        json = response.json()
        orders += json['data']
        if 'next' in json['pages']:
            next_url = json['pages']['next']
        else:
            break
    sys.stdout.write("\nExported {0} orders\n".format(len(orders)))
    return orders

def to_csv(data, filename, keys = []):
    if keys == []:
        keys = data[0].keys()
    with open(filename, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, keys)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

def from_csv(filename):
    orders = []
    with open(filename, mode='r') as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            orders.append(row)
    return orders

def main():
    prefix = ''
    opts,args = getopt.gnu_getopt(sys.argv[1:], '', ['project=', 'start=', 'end=', 'token=', 'prefix='])
    for option, arg in opts:
        if (option == '--project'):
            project_id = arg
        if (option == '--start'):
            start = arg
        if (option == '--end'):
            end = arg
        if (option == '--token'):
            token = arg
        if (option == '--prefix'):
            prefix = arg+'-'

    to_csv(get_orders(project_id, start, end, token), filename=prefix+'orders.csv')

if __name__ == '__main__' :
    main()
