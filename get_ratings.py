#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import requests
import sys

OMDB_API_URL = 'http://www.omdbapi.com/'


def get_rating(title, api_key):

    params = {'t': title, 'apikey': api_key, 'r': 'json'}
    r = requests.get(OMDB_API_URL, params=params)

    r.raise_for_status()

    response = r.json()
    if response['Response'] == 'False':
        msg = 'ERROR: %s' % response['Error']
        raise ValueError(msg)

    ratings = {rate['Source']: rate['Value'] for rate in response['Ratings']}
    try:
        rating = ratings['Rotten Tomatoes']
    except KeyError:
        msg = 'ERROR: Rotten Tomatoes rating not availble for "%s"' % response['Title']
        raise ValueError(msg)

    return response['Title'], rating


def main():
    """Fetch Rotten Tomatoes rating from www.omdbapi.com."""

    parser = argparse.ArgumentParser(
        description='Fetch Rotten Tomatoes rating from www.omdbapi.com')

    parser.add_argument('title', help='title of the movie')

    args = parser.parse_args()

    try:
        import config
    except ImportError:
        print('ERROR: cannot import config.py')
        sys.exit(-1)

    if not config.API_KEY:
        print('ERROR: API key is missing, check config.py')
        sys.exit(-1)

    try:
        found_title, rating = get_rating(args.title, config.API_KEY)
    except (requests.exceptions.HTTPError, ValueError) as e:
        print(e)
        sys.exit(-1)
    else:
        print('Rotten Tomatoes rating for "%s" = %s' % (found_title, rating))


if __name__ == "__main__":
    main()
