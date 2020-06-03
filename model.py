import prepare_r
import features
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import BernoulliNB
from scipy import stats

def make_the_model():
    # Read the data in from the file named 'data.json'
    df = pd.read_json('data.json')

    # Drop any rows that have null values in them, then reset the index
    df = df.dropna(axis=0)\
            .reset_index(drop = True)

    # Filter out languages
    df = df.groupby('language').filter(lambda x : len(x)>5)

    # Replace the languages that show up < 4 times in our data with 'Other'
    # This consolidates the languages to one classification
    df.language = df.language.apply(prepare_r.other)

    # Drop the column with the name of the repo, since that won't impact the model
    df = df.drop(columns = ['repo'])

    # Apply some cleaning to the data
    df = prepare_r.prep_contents(df).drop(columns = ['original', 'stemmed', 'normalized', 'lemmatized'])
    df = df.reset_index()



    # Create, fit and transform our TF-IDF Vectorizor on our model dataset
    from sklearn.feature_extraction.text import TfidfVectorizer
    tfidf = TfidfVectorizer()
    X = tfidf.fit_transform(df.cleaned).todense()
    y = df.language

    # Split the data into train and test, along the x and y variables
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=.2, random_state = 123)

    # Create a Classifier for the Naive Bayes 
    clf = BernoulliNB(alpha=1)
    clf.fit(X_train, y_train)
    
    # Return the NLP classifier, as well as the Naive Bayes classifier
    # These classifiers have been fit to the sample dataset we provided
    # They can be used to transform new datasets and provide predictions on them
    return tfidf, clf


def predict_single_readme(readme_text):
    # Getting our classifiers we modeled
    tfidf, clf = make_the_model()
    X = tfidf.transform([readme_text]).todense()
    
    return clf.predict(X)[0]


def predict_all_readmes(df, col: pd.DataFrame) -> pd.DataFrame:
    tfidf, clf = make_the_model()
    
    data = []
    for row in df[col]:
        x = tfidf.transform([row]).todense()
        data.append(clf.predict(x)[0])
    df['predicted'] = data
    
    return df

def split_data(X,y):
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=.2, random_state = 123)
    return X_train, X_test, y_train, y_test


def tfid_vectorize(df):
    #Create, fit and transform our TF-IDF Vectorizor on our model dataset
    from sklearn.feature_extraction.text import TfidfVectorizer
    tfidf = TfidfVectorizer()
    X = tfidf.fit_transform(df.cleaned).todense()
    y = df.language
    return X, y

def logistic_reg(df, set):
    X, y = tfid_vectorize(df)
    X_train, X_test, y_train, y_test = split_data(X,y)
    train = pd.DataFrame(dict(actual=y_train))
    test = pd.DataFrame(dict(actual=y_test))
    logit = LogisticRegression(solver = 'liblinear', C = 10).fit(X_train, y_train)
    train['predicted'] = logit.predict(X_train)
    test['predicted'] = logit.predict(X_test)

    if set == 'train':
        print('Accuracy: {:.2%}'.format(accuracy_score(train.actual, train.predicted)))
        print('---')
        print('Confusion Matrix')
        print(pd.crosstab(train.predicted, train.actual))
        print('---')
        print(classification_report(train.actual, train.predicted))


    if set == 'test':
        print('Accuracy: {:.2%}'.format(accuracy_score(test.actual, test.predicted)))
        print('---')
        print('Confusion Matrix')
        print(pd.crosstab(test.predicted, test.actual))
        print('---')
        print(classification_report(test.actual, test.predicted))
    
def DecisionTree_clf(df, set):
    X, y = tfid_vectorize(df)
    X_train, X_test, y_train, y_test = split_data(X,y)
    train = pd.DataFrame(dict(actual=y_train))
    test = pd.DataFrame(dict(actual=y_test))
    clf = DecisionTreeClassifier(criterion='entropy', max_depth=3, random_state=123)
    clf.fit(X_train, y_train)
    train['predicted'] = clf.predict(X_train)
    test['predicted'] = clf.predict(X_test)

    if set == 'train':
        print('Accuracy: {:.2%}'.format(accuracy_score(train.actual, train.predicted)))
        print('---')
        print('Confusion Matrix')
        print(pd.crosstab(train.predicted, train.actual))
        print('---')
        print(classification_report(train.actual, train.predicted))


    if set == 'test':
        print('Accuracy: {:.2%}'.format(accuracy_score(test.actual, test.predicted)))
        print('---')
        print('Confusion Matrix')
        print(pd.crosstab(test.predicted, test.actual))
        print('---')
        print(classification_report(test.actual, test.predicted))


def RF_clf(df, set):
    """ Random Forest Classifier"""
    X, y = tfid_vectorize(df)
    X_train, X_test, y_train, y_test = split_data(X,y)
    train = pd.DataFrame(dict(actual=y_train))
    test = pd.DataFrame(dict(actual=y_test))
    clf = RandomForestClassifier(bootstrap=True, 
                            class_weight=None, 
                            criterion='gini',
                            min_samples_leaf=3,
                            n_estimators=1000,
                            max_depth=5, 
                            random_state=42)
    clf = DecisionTreeClassifier(criterion='entropy', max_depth=3, random_state=123)
    clf.fit(X_train, y_train)
    train['predicted'] = clf.predict(X_train)
    test['predicted'] = clf.predict(X_test)

    if set == 'train':
        print('Accuracy: {:.2%}'.format(accuracy_score(train.actual, train.predicted)))
        print('---')
        print('Confusion Matrix')
        print(pd.crosstab(train.predicted, train.actual))
        print('---')
        print(classification_report(train.actual, train.predicted))


    if set == 'test':
        print('Accuracy: {:.2%}'.format(accuracy_score(test.actual, test.predicted)))
        print('---')
        print('Confusion Matrix')
        print(pd.crosstab(test.predicted, test.actual))
        print('---')
        print(classification_report(test.actual, test.predicted))


def NB_Multinomial(df, set):
    X, y = tfid_vectorize(df)
    X_train, X_test, y_train, y_test = split_data(X,y)
    train = pd.DataFrame(dict(actual=y_train))
    test = pd.DataFrame(dict(actual=y_test))
    clf = MultinomialNB(alpha = 0.01)
    clf.fit(X_train, y_train)

    if set == 'train':
        y_pred = clf.predict(X_train)
        print('Accuracy of Naive Bayes classifier on training set: {:.2f}'.format(clf.score(X_train, y_train)))
        print(classification_report(y_train, y_pred))


    if set == 'test':
        y_pred = clf.predict(X_test)
        print('Accuracy of Naive Bayes classifier on test set: {:.2f}'.format(clf.score(X_test, y_test)))
        print(classification_report(y_test, y_pred))