import pandas as pd

def save_logs(logs):
    
    df = pd.DataFrame(logs)
    return df
    

def load_logs(filepath='agent_environment_logs.csv'):
    
    return pd.read_csv(filepath)
