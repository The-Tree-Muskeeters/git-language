import pandas as pd
import re

def add_features(df: pd.DataFrame) -> pd.DataFrame:
    # Number of words in the repo
    df['word_count'] = df['cleaned'].apply(lambda x: len(x.split()))
    
    # Number of sentences in the repo
    df['sentence_count'] = df['readme_contents'].apply(lambda x: len(x.split('\n\n')))
    
    # Number of brackets ('[') in the repo
    df['bracket_count'] = df['readme_contents'].apply(lambda x: x.count('['))
    
    # Number of angle brackets ('<') in the repo
    df['angle_bracket_count'] = df['readme_contents'].apply(lambda x: x.count('<'))
    
    # Number of headings in the repo
    # Each one is a seperate feature
    df['headings1'] = df.readme_contents.apply(lambda x: len(re.findall(r'[^#]#[^#]', x)))
    df['headings2'] = df.readme_contents.apply(lambda x: len(re.findall(r'[^#]##[^#]', x)))
    df['headings3'] = df.readme_contents.apply(lambda x: len(re.findall(r'[^#]###[^#]', x)))
    df['headings4'] = df.readme_contents.apply(lambda x: len(re.findall(r'[^#]####[^#]', x)))
    
    # Count of all the headings
    df['headings'] =  df['headings1'] +  df['headings2']  +  df['headings3']  +  df['headings4'] 
    
    # Number of links in the repo
    df['link'] = df.readme_contents.apply(lambda x: len((re.findall(r'http', x ))))
    
    # Number of digits in the repo
    df['digits'] = df.readme_contents.apply(lambda x: len(re.findall(r'[0-9]', x))) 
    
    # Sum of word count, headings and links
    df['total'] = df['word_count'] + df['headings']  + df['link']
        
    return df
