from modules import *
from transferer import *

xlsx_file = "test_scheduel.xlsx"

Event.create_event(Event.extractor(xlsx_file))