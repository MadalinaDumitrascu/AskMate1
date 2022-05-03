import connection
import util



def get_data_base():
    content = connection.read_data_base()
    return content

def get_one_question():
    question = get_data_base()


