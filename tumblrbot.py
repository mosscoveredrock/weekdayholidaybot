import pytumblr
import time
import random

# OAuth is stored in a seperate file because thats not something you post publicly on github
oauth = open("oauth.txt","r+")
oauth = oauth.read()

# Authenticate via OAuth
# OAuth comes in four parts
client = pytumblr.TumblrRestClient(
  oauth[1:51],
  oauth[55:105],
  oauth[109:159],
  oauth[163:213]
)

special_days = {
    "Thu20": "thursday the 20th",        
    "Oct19": "none pizza with left beef",
    "Nov05":  "november 5th",              
    "Apr13": "neil banging out the tunes",
    "Mar15": "ides of march",
    "Apr24": "josh fight",
    "Jul17": "hershey",
    "Jul12": "dashcon",
    "Oct03": "october 3rd"
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
if(True):
    
    # check if its a new day yet
    possiblePosts = {}
    day = time.asctime(time.localtime())  
    file = open("lastPost.txt","r+")
    
    if(day[0:3] != file.read()[0:3]):
        try:

            # look up if it's a special non-weekly holiday
            for i in special_days:
                if(i[0:2] in day[0:10] and i[3:4] in day[0:10]):
                   possiblePosts = client.posts("weekdayholidaybot", tag = special_days[i])["posts"]
                   print("SPECIAL DAY! - " + special_days[i].upper())

            # otherwise search through posts tagged with the current weekday
            if(len(possiblePosts) == 0):
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
        
        except:
            print("OOPSIE WOOPSIE!!! WE DID A FUCKIE WUCKIE!!!!")
               
    else:
        file.seek(0)
        print("not yet. - " + file.read())
        
    file.close()
    time.sleep(3)
        
    # wait eight hours
    # time.sleep(28800)
        
    
