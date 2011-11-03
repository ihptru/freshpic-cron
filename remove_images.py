import psycopg2
import config
import os

def start(self):
    conn = psycopg2.connect( ("host=%s port=%s dbname=%s user=%s password=%s") % (config.dbhost, config.dbport, config.dbname, config.dbuser, config.dbpassword) )
    cur = conn.cursor()
    sql = """SELECT name,user_id FROM images
            WHERE delete = TRUE
    """
    cur.execute(sql)
    records = cur.fetchall()
    conn.commit()
    if ( len(records) == 0 ):
        self.oprint("{remove_images} No images marked to remove")
        return
    for i in range(len(records)):
        name = records[i][0]
        user_id = str(records[i][1])
        sql = """DELETE FROM images
                WHERE name = '"""+name+"""' AND user_id = """+user_id+"""
        """
        cur.execute(sql)
        conn.commit()
        self.oprint("{remove_images} (User_ID: "+user_id+") Removed image from Database: "+name)
        for path_dir in ['i','p','s']:
            image_path = config.site_location+path_dir+'/'+user_id+'/'+name+'.jpg'
            os.remove(image_path)
        self.oprint("{remove_images} (User_ID: "+user_id+") Removed image: " + name)
    self.oprint("{remove_images} It took %s to remove Images" % self.time_spent())
    cur.close()
        
    
