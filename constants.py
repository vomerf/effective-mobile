from pathlib import Path

from addition import add_records
from edit import edit_records
from read import read_records
from search import search_records

BASE = Path(__file__).parent


MODE_TO_FUNCTION = {
    'read_phone_book': read_records,
    'add_in_phone_book': add_records,
    'edit_in_phone_book': edit_records,
    'search_in_phone_book': search_records
}