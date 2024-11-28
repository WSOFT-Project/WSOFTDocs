import re
import unicodedata

def slugify(value, separator):
    """Slugify a string, making it URL friendly."""
    normalized = unicodedata.normalize('NFKC', value)
    # Remove leading/trailing whitespace, including Japanese whitespace
    normalized = re.sub(r'^[ 　]+|[ 　]+$', '', normalized)
    # Replace whitespace with the separator
    normalized = re.sub(r'\s+', separator, normalized)
    # Replace special English grammar characters except dot (・)
    normalized = re.sub(r'[^\w\s.・-]', '', normalized)
    # Convert to lowercase
    normalized = normalized.lower()
    return normalized
