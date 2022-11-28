############## imports ###############

from sklearn import datasets
import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
import string
import sklearn
import csv
from wordcloud import WordCloud
import pickle
from tkinter import *
from tkinter import messagebox ,Entry , Button ,Label
import tkinter as tk

####################################

### dataSet ###

data = pd.read_csv("C:/Users/persian computer/Desktop/website/I.A-Tutorial/spam.csv", encoding='latin-1')
# print(data.shape)
# print(data.info())

####################################


data = data.drop(["Unnamed: 2", "Unnamed: 3", "Unnamed: 4"], axis=1)
data = data.rename(columns={"v2": "text", "v1": "label"})

print(data.shape)
print(data.info())


###################################


# print(data["label"].value_counts())


###################################


nltk.download("punkt")


################## build ##########


# ham_words = ""
# spam_words = ""


# Creating a corpus of spam messages

# for val in data[data['label']== 'spam'].text:
#    text = val.lower()
#    tokens = nltk.word_tokenize(text)
#    for words in tokens:
#        spam_words = spam_words + words + " "

# Creating a corpus of ham messages

# for val in data[data['label']== 'ham'].text:
#    text = val.lower()
#    tokens = nltk.word_tokenize(text)
#    for words in tokens:
#        ham_words = ham_words + words + " "


######################################


# spam_wordcloud = WordCloud(width=500,height=300).generate(spam_words)
# ham_wordcloud = WordCloud(width=500,height=300).generate(ham_words)


# Spam word cloud

# plt.figure(figsize=(10,8), facecolor='w')
# plt.imshow(spam_wordcloud)
# plt.axis('off')
# plt.tight_layout(pad=0)
# plt.show()


# Ham word Cloud

# plt.figure(figsize=(10,8), facecolor='g')
# plt.imshow(ham_wordcloud)
# plt.axis('off')
# plt.tight_layout(pad=0)
# plt.show()


#######################################


nltk.download("stopwords")


def text_process(text):
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = [word for word in text.split() if word.lower() not in stopwords.words('english')]

    return " ".join(text)
    


data["text"] = data["text"].apply(text_process)

# print("#############")
# print(data.shape)
# print(data.info())


######################################


text = pd.DataFrame(data["text"])
label = pd.DataFrame(data["label"])

######################################


from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform(data["text"])
features = vectors

######################

df2 = pd.DataFrame(vectors.toarray(), columns=vectorizer.get_feature_names())
df3 = df2.transpose()
########################

x_train, x_test, y_train, y_test = train_test_split(features, data["label"], test_size=0.15, random_state=111)

########################

knn = KNeighborsClassifier(n_neighbors=49)
knn.fit(x_train,y_train)
score=knn.score(x_test,y_test)

########################
print("work")
############# TKinTer ################

#########################
def spam():
    
    #lst=[]
    #find=input("email contents? ")
    #lst.append(find)
    lst = enter.get()
    vec=vectorizer.transform(lst)
    result=knn.predict(vec)
    print(result)
    
    s = [str(i) for i in result]
    a = int("".join(s))

    # show out the final result
    if a == "spam":
        messagebox.showinfo("its spam")
        print("spam")
    else:
        messagebox.showerror("its not spam")
        print("not spam")
    
root = tk.Tk()
root.title('spam')
root.geometry('400x200')

head = Label(root, text='SPAM  Checker',font=('helvetica', 24 , 'bold'))
head.pack()
enter = Entry(root, width=400,borderwidth=5)
enter.pack()
b = Button(root, text = 'Check', font=('helvetica', 20 , 'bold'), fg = 'white', bg = 'blue', command = spam)
b.pack()
root.mainloop()