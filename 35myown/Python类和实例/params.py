import psycopg2

def operate_task(query_str):
        conn = psycopg2.connect(
            database="my_local",
            user="postgres",
            password="1qaz2wsx",
            host="127.0.0.1",
            port="5432")
        cur = conn.cursor()
        cur.execute(query_str)
        conn.commit()
        rows = cur.fetchall()
        return rows
class Params(object):
    m1 = 0
    batch_size = 8
    map_height = 11
    map_width = 11
    closeness_sequence_length = 1
    period_sequence_length = 1
    trend_sequence_length = 1
    nb_flow = 1
    num_of_filters = 64
    num_of_residual_units = 4
    num_of_output = 1  # depth of predicted output map
    delta = 0.5
    epsilon = 1e-7
    beta1 = 0.8
    beta2 = 0.999
    lr = 0.001
    num_epochs = 4
    logdir = "data/logdir"
    model_path = "data/model/L12/m"

    

    def __init__(self, train_id):
        str1 = 'select user_name from task.train where train_id = \''+ str(train_id)+'\''
        x = operate_task(str1)
        self.m2 = x