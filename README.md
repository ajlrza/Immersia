# IMMERSIA

Immersia is a local web application that brings together your ideas into a simulated, playable worlds with persistency and context management
to enrich the experience

<img width="1358" height="567" alt="tikz-export" src="https://github.com/user-attachments/assets/9dcc3b7d-1a5f-46f6-822a-092af64e2b18" />


# About

Inspired by the [paper](https://arxiv.org/abs/2512.23676) on web world models, a website processes initial and real-time data via a mechanism that structures both logical and narrative data into TypeScript structs which are both combined to deliver outputs to the user. It works by using
Large Language Models to generate narrative and contexts while it follows the logical struct constraints provided by the developer. While it allows users to interact
with world models via a websites, for an application persistency matters. Hence Immersia integrates videogame software logic on web world models.

# How To Install

```shell
git clone https://github.com/ajlrza/Immersia.git
cd Immersia
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
npm install
cp .env.example .env             # then add API key
python src/main.py               # run locally
```
