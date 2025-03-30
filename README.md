# ChatbotSI2
## Project Overview
This chatbot was developed as part of the first project of the [Intelligent Systems II Module](https://www.ua.pt/en/uc/15052) at the University of Aveiro during the 2024/2025 academic year.

## Prerequisites
* Python 3.10 
* Anaconda Prompt (Miniconda3) [Link to Install](https://docs.conda.io/projects/miniconda/en/latest/)
* Google Maps API Key [Watch this Video](https://www.youtube.com/watch?v=hsNlz7-abd0)
* TMDb API Key [Watch this Video](https://www.youtube.com/watch?v=Gf45f5cW6c4&list=LL&index=5)

## How to Run
Follow the steps below to set up and run the project.


### 1. Crete a .env file in the project directory
```bash
    # Write the following variables in the .env file to store yout API's keys
    GOOGLE_MAPS_API_KEY = "YOUR API KEY"
    TMDB_API_KEY = "YOUR API KEY"
```

### 2. Open 2 Anaconda Prompt in the project directory

### 3. Install Rasa and other dependecies
```bash
# In one Anaconda Prompt
conda create --name rasa-env python=3.10
conda activate rasa-env
pip install -r requirements.txt 
python -m spacy download en_core_web_lg
```

### 4. Train the chatbot model
```bash
# In the previous Anaconda Prompt
rasa train --domain .
```

### 5. Test the chatbot
```bash
# In previous Anaconda Prompt
rasa run actions

# In the other Anaconda Prompt 
activate rasa-env && rasa shell --endpoints endpoints.yml
```

**Note**: After completing the steps above for the first time, you can run all commands in a single line:
```bash
# In the Anaconda Prompt
activate rasa-env && rasa train --domain . && rasa shell --endpoints endpoints.yml

# On another Anaconda Prompt
rasa run actions
```

## Contributors
* **Daniel Emídio** - Master's student specializing in Informatics Engineering
* **David Palricas** - Master's student specializing in Digital Game Development
* **Márcio Tavares** - Master's student specializing in Digital Game Development
