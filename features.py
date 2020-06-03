import pandas as pd

def add_features(df: pd.DataFrame) -> pd.DataFrame:
    df['word_count'] = df['cleaned'].apply(lambda x: len(x.split()))
    df['sentence_count'] = df['readme_contents'].apply(lambda x: len(x.split('\n\n')))
    df['bracket_count'] = df['readme_contents'].apply(lambda x: x.count('['))
    df['angle_bracket_count'] = df['readme_contents'].apply(lambda x: x.count('<'))
    
    return df