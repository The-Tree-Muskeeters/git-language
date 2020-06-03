import pandas as pd
import re

def add_features(df: pd.DataFrame) -> pd.DataFrame:
    df['word_count'] = df['cleaned'].apply(lambda x: len(x.split()))
    df['sentence_count'] = df['readme_contents'].apply(lambda x: len(x.split('\n\n')))
    df['bracket_count'] = df['readme_contents'].apply(lambda x: x.count('['))
    df['angle_bracket_count'] = df['readme_contents'].apply(lambda x: x.count('<'))
    df['headings1'] = df.readme_contents.apply(lambda x: len(re.findall(r'[^#]#[^#]', x)))
    df['headings2'] = df.readme_contents.apply(lambda x: len(re.findall(r'[^#]##[^#]', x)))
    df['headings3'] = df.readme_contents.apply(lambda x: len(re.findall(r'[^#]###[^#]', x)))
    df['headings4'] = df.readme_contents.apply(lambda x: len(re.findall(r'[^#]####[^#]', x)))
    df['link'] = df.readme_contents.apply(lambda x: len((re.findall(r'http', x ))))
    df['digits'] = df.readme_contents.apply(lambda x: len(re.findall(r'[0-9]', x))) 
    df['headings'] =  df['headings1'] +  df['headings2']  +  df['headings3']  +  df['headings4'] 
    df['total'] = df['word_count'] + df['headings']  + df['link']
        
    return df
