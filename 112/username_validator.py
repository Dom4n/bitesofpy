# nice snippet: https://gist.github.com/tonybruess/9405134
from collections import namedtuple
import re

social_platforms = """Twitter
  Min: 1
  Max: 15
  Can contain: a-z A-Z 0-9 _

Facebook
  Min: 5
  Max: 50
  Can contain: a-z A-Z 0-9 .

Reddit
  Min: 3
  Max: 20
  Can contain: a-z A-Z 0-9 _ -
"""

# note range is of type range and regex is a re.compile object
Validator = namedtuple('Validator', 'range regex')


def parse_social_platforms_string():
    """Convert the social_platforms string above into a dict where
       keys = social platformsname and values = validator namedtuples"""
    platforms = social_platforms.split('\n\n')
    validators = {}
    for platform in platforms:
        name = re.search(r'^\w+', platform).group(0)

        _range_min = re.search(r'Min: (\d+)', platform).group(1)
        _range_max = re.search(r'Max: (\d+)', platform).group(1)

        can_contain = re.search(r'Can contain: (.*)', platform).group(1).replace(' ', '')
        _range = range(int(_range_min), int(_range_max) + 1)

        validators.update({
            name: Validator(range=_range, regex=re.compile(f'[{can_contain}]*'))
        })
    return validators


def validate_username(platform, username):
    """Receives platforms(Twitter, Facebook or Reddit) and username string,
       raise a ValueError if the wrong platform is passed in,
       return True/False if username is valid for entered platform"""
    all_validators = parse_social_platforms_string()

    if platform not in all_validators.keys():
        raise ValueError

    validator = all_validators[platform]

    if len(username) not in validator.range:
        return False

    if not re.fullmatch(validator.regex, username):
        return False

    return True
