import os
from collections import defaultdict

textdict = {'a01':'Der Lappen liegt auf dem Eisschrank',
'a02':'Das will sie am Mittwoch abgeben',
'a04':'Heute abend konnte ich es ihm sagen',
'a05':'Das schwarze Stuck Papier befindet sich da oben neben dem Holzstuck',
'a07':'In sieben Stunden wird es soweit sein',
'b01':'Was sind denn das fur Tuten, die da unter dem Tisch stehen',
'b02':'Sie haben es gerade hochgetragen und jetzt gehen sie wieder runter',
'b03':'An den Wochenenden bin ich jetzt immer nach Hause gefahren und habe Agnes besucht',
'b09':'Ich will das eben wegbringen und dann mit Karl was trinken gehen',
'b10':'Die wird auf dem Platz sein, wo wir sie immer hinlegen'}
emotiondict = {'W':1,'L':2,'E':3,'A':4,'F':5,'T':6,'N':7}
files = os.listdir('/Users/jennyyang/Desktop/test')
data = []
speaker = []
sentence = []
emotion = []
index = 0
for file in files:
    filename = file.split('.')[0]
    speaker.append(filename[:2])
    print(filename)
    sentence.append(textdict[filename[2:5]])
    emotion.append(emotiondict[filename[5]])
    data.append(index)
    os.rename(r'/Users/jennyyang/Desktop/test/'+filename+'.wav',r'/Users/jennyyang/Desktop/test/'+str(index) +'.wav')
    index = index + 1
    if index == 400:
        break
        break
print(data)

# https://stackoverflow.com/questions/5419204/index-of-duplicates-items-in-a-python-list
def list_duplicates(seq):
    tally = defaultdict(list)
    for i,item in enumerate(seq):
        tally[item].append(data[i])
    return ((key,locs) for key,locs in tally.items() 
                            if len(locs)>1)

f = open("spk2utt", "w")
for dup in sorted(list_duplicates(speaker)):
    f.write(str(dup[0]) + " ")
    for item in dup[1]:
    	f.write(str(item) + " ")
    f.write("\n")
f.close()


f = open("textraw", "w")
for index in range(len(sentence)):
    f.write(str(sentence[index]) + "\n")
f.close()

f = open("text", "w")
for index in range(len(sentence)):
    f.write(str(data[index]) + " " + str(sentence[index]) + "\n")
f.close()

f = open("utt2spk", "w")
#for dup in sorted(list_duplicates(emotion)):
#    for item in dup[1]:
#        for num in item:
#            f.write(item + " ")
#            f.write(str(dup[0]) + " ")
#            f.write("\n")
#f.close()
for index in range(len(sentence)):
    f.write(str(data[index]) + " " + str(speaker[index]) + "\n")
f.close()

f = open("utt2emo", "w")
#for dup in sorted(list_duplicates(emotion)):
#    for item in dup[1]:
#        for num in item:
#            f.write(item + " ")
#            f.write(str(dup[0]) + " ")
#            f.write("\n")
#f.close()
for index in range(len(sentence)):
    f.write(str(data[index]) + " " + str(emotion[index]) + "\n")
f.close()



