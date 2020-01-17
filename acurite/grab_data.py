import argparse
from datetime import date, timedelta


def grab_data(dataDate):
    print(f'Retrieving data from {dataDate}')


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Download daily data from acurite.')
    parser.add_argument('-d', '--date',
                        default=str(date.today() - timedelta(days = 1)),
                        help='Date to download - defaults to yesterday\n  format -> YYYY-MM-DD',
                        type=date.fromisoformat)
    parser.add_argument('-n', '--days', default=1, type=int,
                        help='Number of days to download')
    parser.add_argument('-r', '--rev', action='store_true',
                        help='Count backwards from given date')
    args = parser.parse_args()

    current_date = args.date
    direction = -1 if args.rev else 1
    interval = timedelta(days=direction)
    for _ in range(args.days):
        grab_data(current_date)
        current_date = current_date + interval
