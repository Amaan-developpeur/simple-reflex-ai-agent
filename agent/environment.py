import os
from pathlib import Path
import pandas as pd
from agent.model_loader import loading_model
from agent.sensor import sense  
from agent.decision import decision
from agent.agent_loop import agent_loop

def prepare_image_paths(base_dir: Path, limit_per_class=None):
    """
    Collects image paths from subfolders in base_dir.
    If limit_per_class is set, limits the number of images per class folder.
    """
    image_paths = []
    for class_name in os.listdir(base_dir):
        class_path = base_dir / class_name
        if not class_path.is_dir():
            continue
        files = list(class_path.iterdir())
        if limit_per_class:
            files = files[:limit_per_class]
        for file in files:
            image_paths.append(str(file))
    return image_paths

def add_true_label_column(df: pd.DataFrame):
    """
    Extracts true label from image_path assuming folder structure includes true label.
    """
    df['true_label'] = df['image_path'].apply(lambda x: Path(x).parts[-2].capitalize())
    return df

def main():
    BASE_DIR = Path('split/val')
    
    # Step 1: Prepare environment data (image paths)
    image_paths = prepare_image_paths(BASE_DIR, limit_per_class=50)  # or None for all

    # Step 2: Load the trained model
    model = loading_model('full_model.keras')

    # Step 3: Run the agent loop
    logs = agent_loop(image_paths, model)

    # Step 4: Create DataFrame with logs and true labels
    df = pd.DataFrame(logs)
    df = add_true_label_column(df)

    # Step 5: Save logs for further analysis
    df.to_csv('agent_environment_logs.csv', index=False)

    print(f"Processed {len(df)} images. Logs saved to 'agent_environment_logs.csv'.")

if __name__ == "__main__":
    main()
