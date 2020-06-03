import prepare_r
import features
import pandas as pd

def make_the_model():
    # Read the data in from the file named 'data.json'
    df = pd.read_json('data.json')

    # Drop any rows that have null values in them, then reset the index
    df = df.dropna(axis=0)\
            .reset_index(drop = True)

    # Replace the languages that show up < 4 times in our data with 'Other'
    # This consolidates the languages to one classification
    df['language'] = df.language.replace([
                'PHP','Shell','Kotlin','Vue','ApacheConf','Jupyter Notebook','R','Groovy',\
                'Kotlin','Scala','Rust', 'Swift','C#','Dart','Ruby','Objective-C','PowerShell','TeX',\
                'C', 'CSS', 'TypeScript', 'Go'], 
                'Other')

    # Drop the column with the name of the repo, since that won't impact the model
    df = df.drop(columns = ['repo'])

    # Apply some cleaning to the data
    df = (prepare_r.prep_contents(df)
              .drop(columns = ['original', 'stemmed', 'normalized', 'lemmatized'])
         )

    df = features.add_features(df)

    from sklearn.feature_extraction.text import TfidfVectorizer
    tfidf = TfidfVectorizer()
    X = tfidf.fit_transform(df.cleaned).todense()
    y = df.language

    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=.2, random_state = 123)

    from sklearn.neural_network import MLPClassifier
    clf = MLPClassifier(solver='lbfgs', alpha=1,
                         hidden_layer_sizes=(70,), random_state=123)

    clf.fit(X_train, y_train)
    
    return tfidf, clf


def predict_single_readme(readme_text):
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