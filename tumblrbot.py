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

special_days = {
    "Thu20": "thursday the 20th",        
    "Oct19": "none pizza with left beef",
    "Nov5":  "november 5th",              
    "Apr13": "neil banging out the tunes",
    "Mar15": "ides of march",
    "Apr24": "josh fight",
    "Jul17": "hershey",
    "Jul12": "dashcon"
    }

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
#while(True):
if(True):

    # check if its a new day yet
    possiblePosts = {}
    day = time.asctime(time.localtime())
    #day = "Thu Mar 15 131231231"
    file = open("lastPost.txt","r+")
    if(day[0:3] != file.read()[0:3]):
    #if(True):
        #if(True):

        try:

            # look up if it's a special non-weekly holiday
            for i in special_days:
                if(i[0:3] in day[0:10] and i[4:5] in day[0:10]):
                   possiblePosts = client.posts("weekdayholidaybot", tag = special_days[i])["posts"]
                   print("SPECIAL DAY! - " + special_days[i].upper())

            # search through posts tagged with the current weekday
            if(len(possiblePosts) == 0):
                possiblePosts = client.posts("weekdayholidaybot", tag = day_names[day[0:3]])["posts"]
            #print(possiblePosts)
            
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

    time.sleep(3)
        
    # wait eight hours
    # time.sleep(28800)
        
    
