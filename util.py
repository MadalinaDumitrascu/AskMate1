from datetime import datetime


def converter(elem):
    date = datetime.fromtimestamp(float(elem) / 1000.0,)
    date = date.strftime('%d/%m/%Y  %H:%M')
    return date


def generate_id_number(ids):
    ids = [int(id) for id in ids]
    print(ids)

    return

