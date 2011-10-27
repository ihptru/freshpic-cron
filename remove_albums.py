import psycopg2
import config
import os

def start(self):
    conn = psycopg2.connect( ("host=%s port=%s dbname=%s user=%s password=%s") % (config.dbhost, config.dbport, config.dbname, config.dbuser, config.dbpassword) )
    cur = conn.cursor()

    sql = """SELECT user_id,album_id FROM albums
            WHERE delete = TRUE
    """
    cur.execute(sql)
    records = cur.fetchall()
    conn.commit()
    if ( len(records) == 0 ):
        print("No albums to remove")
        return
    sql = """DELETE FROM albums 
            WHERE delete = TRUE
    """
    cur.execute(sql)
    conn.commit()
    for i in range(len(records)):
        user_id = str(records[i][0])
        album_id = str(records[i][1])
        sql = """SELECT name FROM images
                WHERE user_id = """+user_id+""" AND album_id = """+album_id+"""
        """
        cur.execute(sql)
        rec_images = cur.fetchall()
        conn.commit()
        sql = """DELETE FROM images
                WHERE user_id = """+user_id+""" AND album_id = """+album_id+"""
        """
        cur.execute(sql)
        conn.commit()
        if ( len(rec_images) == 0 ):
            print("This album is empty")
            continue
        for k in range(len(rec_images)):
            name = rec_images[k][0]
            for path_dir in ['i','p','s']:
                image_path = config.site_location+path_dir+'/'+user_id+'/'+name+'.jpg'
                os.remove(image_path)
                print("Removed image: " + user_id+'/'+name)
    cur.close()
