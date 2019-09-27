import re

index = 0
def fix_translation(org_text, trans_text):
    """Receives original English text as well as text returned by translator.
       Parse trans_text restoring the original (English) code (wrapped inside
       code and pre tags) into it. Return the fixed translation str
    """
    pattern = re.compile(r'<pre>.*?<\/pre>|<code>.*?<\/code>', flags=re.DOTALL)
    matches = re.findall(pattern, org_text)

    def replace_from_list(obj):
        global index
        replacement = matches[index]
        index += 1
        return replacement

    trans = re.sub(pattern, replace_from_list, trans_text)
    global index
    index = 0
    return trans