import pandas as pd
import nltk
from nltk.corpus import stopwords

def basic_clean(df, col):
    '''
    This function takes in a df and a string for a column and
    returns the df with a new column named 'basic_clean' with the
    passed column text normalized.
    '''
    df['basic_clean'] = df[col].str.lower()\
                    .replace(r'[^\w\s]', '', regex=True)\
                    .str.normalize('NFKC')\
                    .str.encode('ascii', 'ignore')\
                    .str.decode('utf-8', 'ignore')
    return df


def lemmatize(df, col):
    '''
    This function takes in a df and a string for column name and
    returns the original df with a new column called 'lemmatized'.
    '''
    # Create the lemmatizer
    wnl = nltk.stem.WordNetLemmatizer()
    
    # Lemmatize each token from our clean_tokes Series of lists
    lemmas = df[col].apply(lambda row: [wnl.lemmatize(word) for word in row])
    
    # Join the cleaned and lemmatized tokens back into sentences
    df['lemmatized'] = lemmas.str.join(' ')
    return df


def remove_stopwords(df, col):
    '''
    This function takes in a df and a string for column name and 
    returns the df with a new column named 'clean' with stopwords removed.
    '''
    # Create stopword_list
    stopword_list = stopwords.words('english')
    
    # Split words in column
    words = df[col].str.split()
    
    # Check each word in each row of the column against stopword_list and return only those that are not in list
    filtered_words = words.apply(lambda row: [word for word in row if word not in stopword_list])
    
    # Create new column of words that have stopwords removed
    df['dropped_stop_' + col] = filtered_words.str.join(' ')
    
    return df

def tokenize(df, col):
    '''
    This function takes in a df and a string for a column and
    returns a df with a new column named 'clean_tokes' with the
    passed column text tokenized and in a list.
    '''
    tokenizer = nltk.tokenize.ToktokTokenizer()
    df['clean_tokes'] = df[col].apply(tokenizer.tokenize)
    return df
    

def prep_docs(df, col):
    '''
    This function takes in a dataframe and returns the same dataframe with a bunch of new columns of the transformed data.
    This will add the following columns:
        - basic_clean (text is normalized)
        - lemmatized
        - dropped_stop_basic_clean (combination of remove stop words and basic clean)
    '''
    
    df = basic_clean(df, col)
    df = lemmatize(df, col)
    df = remove_stopwords(df, 'basic_clean')
    
    return df