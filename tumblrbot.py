import pytumblr
import time
import random

# OAuth is stored in a seperate file because thats not something you post publicly on github
oauth = open("oauth.txt", "r+")
oauth = oauth.read()

# Authenticate via OAuth
# OAuth comes in four parts
client = pytumblr.TumblrRestClient(
    oauth[1:51],
    oauth[55:105],
    oauth[109:159],
    oauth[163:213]
)

# constants
special_days = {
    "Thu20": "thursday the 20th",
    "Oct19": "none pizza with left beef",
    "Nov 5": "november 5th",
    "Apr13": "neil banging out the tunes",
    "Mar15": "ides of march",
    "Apr24": "josh fight",
    "Jul17": "hershey",
    "Jul12": "dashcon",
    "Oct03": "october 3rd"
}

day_names = {
    "Mon": "monday",
    "Tue": "tuesday",
    "Wed": "wednesday",
    "Thu": "thursday",
    "Fri": "friday",
    "Sat": "saturday",
    "Sun": "sunday",
}

# set variables
random.seed()
possiblePosts = {}
day = time.asctime(time.localtime())
#day = "Tue Apr 13 10:20:24 2022"
file = open("lastPost.txt", "r+")

#if(True):

# check if its a new day yet
if(day[0:3] != file.read()[0:3]):

    # look up if it's a special non-weekly holiday
    for i in special_days:
        if(i[0:3] in day[0:10] and i[3:5] in day[0:10]):
            possiblePosts = client.posts("weekdayholidaybot", tag = special_days[i])["posts"]
            print("SPECIAL DAY! - " + special_days[i].upper())

    # otherwise search through posts tagged with the current weekday
    if(len(possiblePosts) == 0):
        possiblePosts = client.posts("weekdayholidaybot", tag = day_names[day[0:3]])["posts"]

    # print possible posts in terminal for visualization (optional)
    n = 0
    for i in possiblePosts:
        n += 1
        # "summary" is what tumblr calls the main string associated with the original post
        print(str(n) + " " + i["summary"])

        # "trail" is a list of all reblogs
        for j in i["trail"]:
            try:
                # "content" is the content of any reblogs, with html formatting
                content = j["content"]
                if len(content) < 100 and content[0] != " ":
                    
                    # theres probably a much better way to do this lmao
                    content = content.replace("&nbsp", "")
                    content = content.replace("&rsquo;", "'")
                    content = content.replace("&uuml;", "ü")
                    content = content.replace("<b>", "")
                    content = content.replace("</b>", "")
                    content = content.replace("<i>", "")
                    content = content.replace("</i>", "")
                    content = content.replace("<br />", "")
                    content = content.replace("<h2>", "")
                    content = content.replace("</h2>", "")
                    print(" " * (len(str(n)) + 1) + content[3:-4])
            except KeyError:
                pass
        print("")

    # randomly pick one
    post = random.sample(possiblePosts, 1)[0]

    # print the chosen post
    print(post["id"])
    print(post["summary"])

    # this line is what actually reblogs the post
    client.reblog('weekdayholidaybot.tumblr.com', id = post["id"], reblog_key = post["reblog_key"], tags = [" "])
    print("Post reblogged!")

    # remember day of last post (so the bot doesn't reblog two posts in one day)
    file.truncate(0)
    file.seek(0)
    file.write(day)
    time.sleep(1)

# if it's not a new day yet shut it all down
else:
    file.seek(0)
    print("not yet. - " + file.read())

file.close()
