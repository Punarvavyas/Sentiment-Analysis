import csv

file="tweet_text.txt"
tweet_list=[]
with open(file) as file:
    content = [x.strip() for x in file.readlines()]
    tweet_list.append(content)

print(tweet_list)

nwords=[]

with open("negative-words.txt") as fp:
    nwords=[n.strip() for n in fp.readlines()]
print(nwords)
with open("positive-words.txt") as fp:
    pwords=[n.strip() for n in fp.readlines()]

with open("polarity.csv",'w') as fp:
    writefile=csv.writer(fp,lineterminator='\n')
    writefile.writerow(["Tweet","message","match","Polarity"])
    tweetnumber=1;
    for tweets in tweet_list:
        print(tweets)
        for tweet in tweets:

            tweet_words=tweet.split(" ")
            count=0;
            dic_bag = {}
            positive_count=0
            negative_count=0
            neutral=0
            polarity="none"
            positive_matchlist=[]
            negative_matchlist=[]
            matchlist=[]
            print(tweet_words)
            for twords in tweet_words:
                if twords in dic_bag.keys():
                    count=dic_bag[twords]+1
                    dic_bag[twords]=count

                else:
                    dic_bag[twords]=1
                if twords in pwords:
                    positive_count=positive_count+1;
                    positive_matchlist.append(twords)
                elif twords in nwords:
                    negative_count=negative_count+1;
                    negative_matchlist.append(twords)
                else:
                    neutral=neutral+1
            if(positive_count>negative_count):
                polarity="Positive"
                matchlist=positive_matchlist
            elif(negative_count>positive_count):
                polarity="Negative"
                matchlist=negative_matchlist
            else:
                polarity="Neutral"
                matchlist=["None"]
            strw=" ".join(matchlist)
            writefile.writerow([tweetnumber,tweet,strw,polarity])
            tweetnumber=tweetnumber+1

















