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
        self.oprint("{remove_albums} No albums marked to remove")
        return
    sql = """DELETE FROM albums 
            WHERE delete = TRUE
    """
    cur.execute(sql)
    conn.commit()
    len_rec = len(records)
    users = []
    albums = []
    for i in range(len_rec):
        users.append(records[i][0])
        albums.append(records[i][1])
    for i in range(len_rec):
        self.oprint("{remove_albums} Remove album from Database | User_ID: "+str(users[i])+" | Album_ID: "+str(albums[i]))
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
            self.oprint("{remove_albums} (Empty album) | (User_ID: "+user_id+" | Album_ID "+album_id+") doesn't contain images to remove")
            continue
        self.oprint("{remove_albums} All images from (User_ID: "+user_id+" | Album_ID: "+album_id+") removed from Database")
        for k in range(len(rec_images)):
            name = rec_images[k][0]
            for path_dir in ['i','p','s']:
                image_path = config.site_location+path_dir+'/'+user_id+'/'+name+'.jpg'
                os.remove(image_path)
            self.oprint("{remove_albums} (User_ID: "+user_id+" | Album_ID: "+album_id+" ) Removed image from HDD: " + name)
    self.oprint("{remove_albums} It took %s to remove Albums" % self.time_spent())
    cur.close()
