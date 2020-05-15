import math,csv
can_doc_count=0
halifax_doc_count=0
university_doc_count=0
dal_uni_doc_count=0
can_edu_doc_count=0
total_doc_count=498
docs = []
with open("tfidf.csv",mode='a') as fp:
    writefile = csv.writer(fp, lineterminator='\n')
    writefile.writerow(
        ["Total Documents","500"])

    writefile.writerow(["Search Query", "Document containing term(df)", "Total Documents(N)/number of documents term appeared (df)", "Log10(N/df)"])
    fp.close()


def write(word,doc_count,div_val,loge):
    with open("tfidf.csv",mode='a') as fp:
        writefile = csv.writer(fp, lineterminator='\n')
        print(word,doc_count,div_val,loge)
        writefile.writerow([word,doc_count,div_val,loge])
        fp.close()



for i in range(497):
    filename="news" + str(i) +".txt"
    count_canada=0
    halifax_count=0
    university_count=0
    dalhousie_university_count=0
    canada_education_count=0

    with open(filename) as fp:
        content = fp.readline()
        content_words=content.split(" ")

        for j in range(len(content_words)):
            if content_words[j].lower() == 'canada':
                count_canada=count_canada+1
            if content_words[j].lower() == 'halifax':
                halifax_count=halifax_count+1
            if content_words[j].lower()=='university':
                university_count=university_count+1
            if content_words[j].lower()=='dalhousie' and content_words[j+1].lower() == 'university'and j<len(content_words):
                dalhousie_university_count=dalhousie_university_count+1
            if content_words[j].lower()=='canada' and content_words[j+1].lower() == 'education' and j<len(content_words):
                canada_education_count=canada_education_count+1
        if(count_canada>0):
            can_doc_count=can_doc_count+1
            canada_occur = str(len(content_words)) + "," + str(j) + "," + str(count_canada)
            docs.append(canada_occur)
        if(halifax_count>0):
            halifax_doc_count=halifax_doc_count+1
        if(university_count>0):
            university_doc_count=university_doc_count+1
        if(dalhousie_university_count>0):
            dal_uni_doc_count=dal_uni_doc_count+1
        if(canada_education_count>0):
            can_edu_doc_count=can_edu_doc_count+1

if can_doc_count != 0:
    #print(can_doc_count)
    can_exp=total_doc_count/can_doc_count
    #print(can_exp)
    can_exp_str=str(total_doc_count)+ "/" + str(can_doc_count)
    log_val=math.log10(can_exp)

    write("Canada",can_doc_count,can_exp_str,log_val)




if halifax_doc_count != 0:
    hal_exp=total_doc_count/halifax_doc_count
    hal_exp_str=str(total_doc_count)+ "/" + str(halifax_doc_count)
    log_val=math.log10(hal_exp)
    write("Halifax", halifax_doc_count, hal_exp_str, log_val)

if university_doc_count != 0:
    uni_exp=total_doc_count/university_doc_count
    uni_exp_str=str(total_doc_count) + "/" + str(university_doc_count)
    log_val=math.log10(uni_exp)
    write("University", university_doc_count, uni_exp_str, log_val)

if dal_uni_doc_count != 0:
    dal_uni_exp=total_doc_count/dal_uni_doc_count
    dal_uni_exp_str = str(total_doc_count) + "/" + str(dal_uni_doc_count)
    log_val=math.log10(dal_uni_exp)
    write("Dalhousie University", dal_uni_doc_count, dal_uni_exp_str, log_val)

if can_edu_doc_count != 0:
    can_edu_exp=total_doc_count/can_edu_doc_count
    can_edu_exp_str= str(total_doc_count) + "/" + str(can_edu_doc_count)
    log_val=math.log10(can_edu_exp)
    write("Canada Education",can_edu_doc_count,can_edu_exp_str,log_val)
doc_number=''
max_frequency=0


with open('tfidf2.csv',mode='w') as fp:
    writefile = csv.writer(fp, lineterminator='\n')
    writefile.writerow(
        ["Term", "Canada"])

    writefile.writerow(
        ["Canada appeared in" + str(can_doc_count) + 'documents', "Total words(m)", "Frequency(f)"])

    for i in range(can_doc_count):
        doc_info=docs[i].split(",")
        writefile.writerow(["Article# " + doc_info[1],doc_info[0],doc_info[2]])
        relativefreq=int(doc_info[2])/int(doc_info[0])

        if (relativefreq>max_frequency):
            max_frequency=relativefreq
            doc_number=doc_info[0]
doc_name="news" + str(doc_number)+".txt"
print(doc_name)
fp.close()

with open(doc_name,'r') as fp:
    doc_having_max_freq=fp.readline()
    print(doc_having_max_freq)











