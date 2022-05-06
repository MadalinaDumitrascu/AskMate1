from datetime import datetime
import time


def get_current_time():
    return datetime.utcfromtimestamp(int(time.time())).strftime("%Y-%m-%d %H:%M:%S")


def generate_id_number(ids):
    ids = sorted(ids)
    new_id = ids[-1]
    print(type(new_id))
    return new_id
