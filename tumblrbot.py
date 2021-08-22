import pytumblr
import time
import random

# Authenticate via OAuth
client = pytumblr.TumblrRestClient(
  'LC4d8YNlCyxNqbTwcXW3vi1nK2Dr4N65k99ULJl3AQrvoVAnCj',
  'KhFvn2iYzmJJV5GhY98vWyBv3QjEMQhMx1FM12pSMc9gPtinF8',
  'p5W1JfRLrt1NxMT8hWYwwm4qSJPiakoeXATykBIWqUSFGIFKas',
  'Ti31RBWd0F0O1YWeO1D1S48WdmyQiPKMl2Z4TPVJ4JVdM91Gi6'
)

day_names ={
    "Mon":"monday",
    "Tue":"tuesday",
    "Wed":"wednesday",
    "Thu":"thursday",
    "Fri":"friday",
    "Sat":"saturday",
    "Sun":"sunday",
    }

random.seed()
while(True):

    # check if its a new day yet
    day = time.asctime(time.localtime())
    file = open("lastPost.txt","r+")
    if(day[0:3] != file.read()[0:3]):
    #if(True):
        

        try:
            # search through posts tagged with the current day
            possiblePosts = client.posts("weekdayholidaybot", tag = day_names[day[0:3]])["posts"]

            # randomly pick one
            post = random.sample(possiblePosts, 1)[0]

            # reblog picked post
            print(post["id"])
            print(post["summary"])
            client.reblog('weekdayholidaybot.tumblr.com',id = post["id"], reblog_key = post["reblog_key"])
            print("Post reblogged!")

            # remember day of last post
            file.truncate(0)
            file.seek(0)
            file.write(day)
            file.close()
        
        except:
            print("OOPSIE WOOPSIE!!! WE DID A FUCKIE WUCKIE!!!!")
               
        
    else:
        print("not yet. - " + time.asctime(time.localtime()))
        
    # wait eight hours
    time.sleep(28800)
        
    
