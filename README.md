# Simple Reflex AI Agent for Fundus Disease Screening

This project implements a **Simple Reflex Agent** for automated screening of retinal fundus images to classify them into four categories:  
**Cataract**, **Diabetic Retinopathy**, **Glaucoma**, and **Normal** — and take corresponding actions such as _Refer_, _Monitor_, or _Ignore_.

Inspired by the **agent architectures** from _Artificial Intelligence: A Modern Approach (AIMA)_, this project goes beyond CNN model training and builds a structured **Perceive → Decide → Act** system.

---

## Project Goals

- Wrap a trained CNN model inside an autonomous decision-making loop.
- Simulate an environment to evaluate agent decisions.
- Design an educational, modular walkthrough for beginners to understand how to build AI agents (even reflex ones) from scratch.
- Prepare ground for building more intelligent, utility- or goal-based agents in future phases.

---

## Folder Structure

```
simple_reflex_ai_agent/
├── agent/                     ← All modular Python code
│   ├── sensor.py             ← CNN model + image perception
│   ├── decision.py           ← Decision logic based on class & confidence
│   ├── agent_loop.py         ← Agent controller (perceive → decide → act)
│   ├── environment.py        ← Simulated feedback environment
│   ├── reward.py             ← Evaluation logic
│   ├── logger.py             ← Log saving/loading
│   └── files.py              ← Image path loader
│
├── notebooks/                ← Exploratory notebooks
│   └── testing_implementation.ipynb
│
├── models/
│   └── full_model.keras      ← Pretrained MobileNetV2-based classifier
│
├── notes/
│   ├── notes.pdf
│   └── notes.docx            ← AIMA-based theory and architecture notes
│___simple_reflex_ai_agent.ipynb
├── README.md
├── requirements.txt
└── .gitignore
```
##  Dataset Source (Kaggle)
This project uses the validation portion of the following Kaggle dataset:
https://www.kaggle.com/datasets/drskprabhakar/cataract-dr-normal-glaucoma-fundus-images-dataset
You should place the downloaded Kaggle dataset at the same level as the project folder, like this:
```
YourWorkingDirectory/
├── simple_reflex_ai_agent/
│   └── ...                           ← All agent-related code and files
├── split(dataset)/
│   └── val/                          ← Validation set for testing agent perception
│       ├── cataract/
│       ├── diabetic_retinopathy/
│       ├── glaucoma/
│       └── normal/
```


Code Uses:
base_dir = Path(__file__).resolve().parent.parent.parent / "split" / "val"

This lets agent access validation images directly from the dataset without needing to split or reorganize anything.
---

## Tech Stack

- Python 3.8+
- TensorFlow / Keras
- NumPy, pandas, OpenCV
- Matplotlib, seaborn
- Jupyter Notebook

---

## Sample Output

Image: split/val/glaucoma/xyz.jpg
→ Predicted: Glaucoma
→ Confidence: 0.92
→ Action: Refer immediately
→ Reward: 1.0

