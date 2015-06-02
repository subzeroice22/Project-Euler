import praw
import string

def wait():
    print('Waiting...')
    trash = raw_input()

class myComment:
    author = "NULL"
    vote = 0
    flair = "NULL"
    age = 0
    replies = []
    

    def __init__(self, author, vote, flair, age):
        self.author = author
        self.flair = flair
        self.vote = vote
        self.age = age

    #def addReply(self, 

    def myPrint(self):
        print(str(self.author) + ' ' + str(self.flair) + ": Vote: " + str(self.vote) + ", Age: " + str(self.age))

userAgentString = "Comments & Flair stats by subzeroice23"
redditConnection = praw.Reddit(user_agent = userAgentString)

cfbSubreddit = redditConnection.get_subreddit('cfb')

hot5 = cfbSubreddit.get_new(limit=2)

myCommentList = []

for thread in hot5:

    thread.replace_more_comments(limit=None, threshold=0)

    comments = thread.comments
    flat_comments = praw.helpers.flatten_tree(comments)
    
    for comment in flat_comments:

        author = comment.author
        flair = comment.author_flair_text
        score = comment.score
        text = comment.body
        
        try:
            expanded_comment = redditConnection.get_submission(comment.permalink).comments[0]
            for item in expanded_comment:
                print("######## " + item.body)
        except:
            print(".")

        myCommentObject = myComment(str(author), score, str(flair), 1)
        myCommentObject.myPrint()
        myCommentList.append(myComment)
