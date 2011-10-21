import psycopg2
import config

def start(self):
    conn = psycopg2.connect( ("dbname=%s user=%s password=%s") % (config.dbname, config.dbuser, config.dbpassword) )
    cur = conn.cursor()

    sql = """SELECT delete_flag FROM images
    """
    cur.execute(sql)
    
    conn.commit()
    cur.close()
