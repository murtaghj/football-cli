import argparse
import re
import requests
import pandas as pd
from .enums import Leagues
from .defines import interesting_league_table_columns, table_base_url, fixtures_base_url, interesting_fixture_columns
from bs4 import BeautifulSoup


def get_league_table(league: Leagues):
    """
    Get and print specified league
    :param league: The league that you want to see table or tables for.
    :return: str
    """
    if not isinstance(league, Leagues):
        raise ValueError(f'Expected a league to be supplied got {type(league)}')
    # Fetch data from source
    tables = pd.read_html(table_base_url(league_value=league.value))

    if not tables:
        # If we see this message it is likely the source has changed something
        raise Exception('No data! Check the source')

    # Some leagues like the champions league or the europa league can have
    # multiple tables we need to account for this.

    for index, table in enumerate(tables):
        # We extract only what we need from the dataframe
        table = table[interesting_league_table_columns]

        # Print the group if more than one table detected
        if len(tables) > 1:
            letter = chr(ord('A') + index)
            print(f'Group {letter}')
        print(table.to_string(index=False))
        # Take some line breaks so it looks formatted correctly
        print('\n\n')


def _get_fixture_dates(url: str):
    """
    Private function used to fetch the fixture dates
    :param url:
    :return: list
    """
    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, "html.parser")
    return [date.text for date in soup.find_all(class_="date-divider")]


def get_fixtures(league: Leagues):
    """
    Get the fixtures for the specified league
    :param league: The league that you want to see fixtures for.
    :return: str
    """
    if not isinstance(league, Leagues):
        raise ValueError(f'Expected a league to be supplied got {type(league)}')

    url = fixtures_base_url(league_value=league.value)
    # Fetch data from source
    tables = pd.read_html(url)

    if not tables:
        raise Exception('No data! Check the source')

    # Fetch the dates for fixtures
    dates = _get_fixture_dates(url)
    # For each date and table print them out
    for date, table in zip(dates, tables):
        table = table[interesting_fixture_columns].copy()

        # Renaming a single column
        table.rename(columns={'Unnamed: 2': 'Teams'}, inplace=True)

        # Add " vs " between team names not sure why this is missing from source...
        table['Teams'] = table['Teams'].apply(lambda x: ' vs '.join(re.split(r' {2}', x)))

        print('\n')
        print(f'Fixture Date: {date}')
        print(table.to_string(index=False))
        print('\n')


def entrypoint():
    """
    Main entrypoint for the command line tool
    """
    parser = argparse.ArgumentParser(description="Get league table or fixtures")
    parser.add_argument('league', type=str, choices=[league.name for league in Leagues],
                        help='The league for which you want to get the table or fixtures')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--table', action='store_true', help='Fetch league table')
    group.add_argument('--fixtures', action='store_true', help='Fetch fixtures')
    args = parser.parse_args()

    league_enum = Leagues[args.league]  # Convert string to corresponding Enum value

    if args.table:
        get_league_table(league_enum)
    elif args.fixtures:
        get_fixtures(league_enum)


if __name__ == "__main__":
    entrypoint()
