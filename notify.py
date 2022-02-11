import sqlite3
import time
import datetime
from plyer import notification
import sqlite3

while(1):
    dt = datetime.datetime.now()
    conn=sqlite3.connect("Data.db")
    c=conn.cursor()

    d=c.execute("SELECT Task FROM School WHERE Date=? and Month=? and Year=? and Hour= ? and Min=?",(dt.day,dt.month,dt.year,dt.hour,dt.minute))
    for r in d:
        notification.notify(title = "SCHEDULE NOTIFIER", message = r[0], timeout=20)
    
    e=c.execute("SELECT Task FROM Office WHERE Date=? and Month=? and Year=? and Hour= ? and Min=?",(dt.day,dt.month,dt.year,dt.hour,dt.minute))
    for r in e:
        notification.notify(title = "SCHEDULE NOTIFIER", message = r[0], timeout=20)
    
    f=c.execute("SELECT Task FROM Gathering WHERE Date=? and Month=? and Year=? and Hour= ? and Min=?",(dt.day,dt.month,dt.year,dt.hour,dt.minute))
    for r in f:
        notification.notify(title = "SCHEDULE NOTIFIER", message = r[0], timeout=20)
    
    g=c.execute("SELECT Task FROM Chores WHERE Date=? and Month=? and Year=? and Hour= ? and Min=?",(dt.day,dt.month,dt.year,dt.hour,dt.minute))
    for r in g:
        notification.notify(title = "SCHEDULE NOTIFIER", message = r[0], timeout=20)
    
    h=c.execute("SELECT Task FROM Medical WHERE Date=? and Month=? and Year=? and Hour= ? and Min=?",(dt.day,dt.month,dt.year,dt.hour,dt.minute))
    for r in h:
        notification.notify(title = "SCHEDULE NOTIFIER", message = r[0], timeout=20)
    
    i=c.execute("SELECT Task FROM Submission WHERE Date=? and Month=? and Year=? and Hour= ? and Min=?",(dt.day,dt.month,dt.year,dt.hour,dt.minute))
    for r in i:
        notification.notify(title = "SCHEDULE NOTIFIER", message = r[0], timeout=20)
    
    j=c.execute("SELECT Task FROM Others WHERE Date=? and Month=? and Year=? and Hour= ? and Min=?",(dt.day,dt.month,dt.year,dt.hour,dt.minute))
    for r in j:
        notification.notify(title = "SCHEDULE NOTIFIER", message = r[0], timeout=20)
    #if d!=None or e!=None or f!=None or g!=None or h!=None or i!=None  or j!=None:
    time.sleep(40)
    