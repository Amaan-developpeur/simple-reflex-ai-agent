import pandas as pd


def get_reward(true_label, predicted_class, action):
    
    if true_label == predicted_class:
        if true_label == 'Normal' and action == 'Ignore':
            return 1  # Correctly ignored
        elif true_label != 'Normal' and ('Refer' in action or 'Consult' in action):
            return 1  # Referred appropriately
        elif 'Monitor' in action:
            return 0.5  # Somewhat cautious, acceptable
    return 0  # Mismatch

def apply_rewards(df):
    
    df['reward'] = df.apply(lambda row: get_reward(row['true_label'], row['predicted_class'], row['action']), axis=1)
    return df
