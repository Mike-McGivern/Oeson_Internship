import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from preprocess import clean_text
from sklearn.feature_extraction.text import TfidfVectorizer

# Load the dataset
file = 'Sentences_AllAgree.txt'
sentences = []
labels = []

with open(file, 'r', encoding='ISO-8859-1') as file:
    for line in file:
        parts = line.rsplit('@', 1)
        if len(parts) == 2:
            sentences.append(parts[0].strip())
            labels.append(parts[1].strip())


# Convert labels into numeric
label_mapping = {'positive': 1, 'negative': -1, 'neutral': 0}
y = [label_mapping[label] for label in labels]

# Pre-process the sentences
sentences = [clean_text(sentence) for sentence in sentences]

# Split Data
X_train, X_test, y_train, y_test = train_test_split(sentences, y, test_size=0.2,
                                                    random_state=42)

from collections import Counter
print('Label Information: \n', Counter(y_train))

# Word Embeddings
from sentence_transformers import SentenceTransformer

embed_model = SentenceTransformer('all-MiniLM-L6-v2')
X_train_vec = embed_model.encode(X_train)
X_test_vec = embed_model.encode(X_test)

from imblearn.over_sampling import SMOTE
smote = SMOTE(random_state = 42)
X_train_bal, y_train_bal = smote.fit_resample(X_train_vec, y_train)

from collections import Counter
print('Label Information: \n', Counter(y_train_bal))

# Model
model_svc = SVC(kernel = 'linear')
model_svc.fit(X_train_bal, y_train_bal)

#Evaluation

y_pred_svc = model_svc.predict(X_test_vec)
accuracy_svc = accuracy_score(y_test, y_pred_svc)
print(f'SVC Model Accuracy: ', accuracy_svc)

#Save Model

with open('sentiment.pkl', 'wb') as file:
    pickle.dump(model_svc, file)

with open('transformer.pkl', 'wb') as file:
    pickle.dump(embed_model, file)



