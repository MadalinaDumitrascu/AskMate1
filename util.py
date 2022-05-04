from datetime import datetime

def get_current_time():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print("date and time =", dt_string)
    return dt_string


def converter(elem):
    date = datetime.fromtimestamp(float(elem) / 1000.0,)
    date = date.strftime('%d/%m/%Y  %H:%M')
    return date


def generate_id_number(ids):
    ids = sorted(ids)
    new_id = ids[-1]
    print(type(new_id))
    return new_id

