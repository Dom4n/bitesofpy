import re


def has_timestamp(text):
    """Return True if text has a timestamp of this format:
       2014-07-03T23:30:37"""
    match = re.search(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}', text)
    return True if match else False


def is_integer(number):
    """Return True if number is an integer"""
    return True if isinstance(number, int) else False


def has_word_with_dashes(text):
    """Returns True if text has one or more words with dashes"""
    return True if re.search(r'\S-\S', text) else False


def remove_all_parenthesis_words(text):
    """Return text but without any words or phrases in parenthesis:
       'Good morning (afternoon)' -> 'Good morning' (so don't forget
       leading spaces)"""
    return re.sub(r'\s+\(.*?\)', '', text)


def split_string_on_punctuation(text):
    """Split on ?!.,; - e.g. "hi, how are you doing? blabla" ->
       ['hi', 'how are you doing', 'blabla']
       (make sure you strip trailing spaces)"""
    return [x for x in re.split(r'[?!.,;]\W?', text) if len(x) > 0]


def remove_duplicate_spacing(text):
    """Replace multiple spaces by one space"""
    return re.sub(r'\W+', ' ', text)


def has_three_consecutive_vowels(word):
    """Returns True if word has at least 3 consecutive vowels"""
    return True if re.search(r'[aeiou]{3}', word) else False


def convert_emea_date_to_amer_date(date):
    """Convert dd/mm/yyyy (EMEA date format) to mm/dd/yyyy
       (AMER date format)"""
    date_match = re.search(r'(?P<day>\d{2})/(?P<month>\d{2})/(?P<year>\d{4})', date)
    if not date_match:
        return 'none'
    return f'{date_match.group("month")}/{date_match.group("day")}/{date_match.group("year")}'

