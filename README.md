# ChatbotSI2
## Project Overview
This chatbot was developed as part of the first project of the [Intelligent Systems II Module](https://www.ua.pt/en/uc/15052) at the University of Aveiro during the 2024/2025 academic year.

## Prerequisites
* Python 3.10 
* Anaconda Prompt (Miniconda3) [Link to Install](https://docs.conda.io/projects/miniconda/en/latest/)

## How to Run
Follow the steps below to set up and run the project.

### 1. Open the Anaconda Prompt in the project directory

### 2. Install Rasa
```bash
conda create --name rasa-env python=3.10
conda activate rasa-env
pip install rasa
```

### 3. Train the chatbot model
```bash
# In the Anaconda Prompt
rasa train
```

### 4. Test the chatbot
```bash
# In the Anaconda Prompt
rasa shell
```

**Note**: After completing the steps above for the first time, you can run all commands in a single line:
```bash
# In the Anaconda Prompt
activate rasa-env && rasa train && rasa shell
```

## Contributors
* **Daniel Emídio** - Master's student specializing in Informatics Engineering
* **David Palricas** - Master's student specializing in Digital Game Development
* **Márcio Tavares** - Master's student specializing in Digital Game Development
