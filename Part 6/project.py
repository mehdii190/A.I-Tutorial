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


#nltk.download("punkt")


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


#nltk.download("stopwords")


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

vectorizar = TfidfVectorizer()
vectors = vectorizar.fit_transform(data["text"])
features = vectors

######################

df2 = pd.DataFrame(vectors.toarray(), columns=vectorizar.get_feature_names())
df3 = df2.transpose()

########################
print("work")
############# TKinTer ################

root = tk.Tk()
#####
root.title("My Spam")
root.geometry("300x200")
root.configure(bg='yellow')
root.maxsize(300,200)
#####

########################
lb1 = Label(root,font=24 , text="text")
lb2 = Label(root,font=24 , text="search")


lb1.grid(row = 0, column = 1,pady=30)
lb2.grid(row = 1, column = 1,padx=50,pady=50)
#########################
def search():
    inp = inp1.get()
    
    if str(data[data['label']=='spam'].text) in inp:
        print("its spam")
        messagebox.showinfo("its spam")
    elif str(data[data['label']=='ham'].text) in inp:
        print("its not spam, ok!")
        messagebox.showinfo("its not spam , ok !")

bt1 = Button(root , font=24 , text="enter",command=search)

bt1.grid(row=1 , column=2)
#########################
inp1 = Entry(root , width=20)

inp1.grid(row=0,column=2)
#########################



root.mainloop()