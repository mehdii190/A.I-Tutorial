import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
import tkinter as tk

##################
def search():
    label2.configure(text="")
    data = pd.read_csv("/Users/mehdimirawa/Desktop/video IA/spam.csv", encoding="latin-1")
    data = data.drop(["Unnamed: 2", "Unnamed: 3", "Unnamed: 4"], axis=1)
    data = data.rename(columns={"v2": "text", "v1": "label"})
    #####################
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(data['text'])
    features = vectors
    X_train, X_test, y_train, y_test = train_test_split(features, data['label'], test_size=0.15, random_state=111)
    knn = KNeighborsClassifier(n_neighbors=49)
    knn.fit(X_train, y_train)
    lst = []
    find = text.get()
    lst.append(find)
    vec = vectorizer.transform(lst)
    result = knn.predict(vec)
    for results in result:
        if results == "ham":
            label2.configure(text="its ham", fg="green")
            print("ham")
            return
        else:
            label2.configure(text="its not ham , spam!!!", fg="red")
            print("spam")
##################
root = tk.Tk()
root.title("check")
root.geometry("500x320")
root.maxsize(550, 350)
root.minsize(450, 250)
root.configure(bg='white')

#####################
label1 = tk.Label(root, text="ham or spam?", font=('Times', 20), fg="RED", background="black")
label1.pack(pady=10)

#####################
text = tk.Entry(root, width=40, borderwidth=10, bg="yellow", fg="black", font=('Arial', 20))
text.pack(pady=5)

#####################
button1 = tk.Button(root, text="enter", background="White", width=16, height=2, font=('Bold italic', 15), command=search)
button1.pack(pady=7)
#####################
label2 = tk.Label(root, font=('Arial', 20), background="black")
label2.pack()
#####################
root.mainloop()