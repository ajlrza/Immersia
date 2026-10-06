import json
import tiktoken
import numpy as np
from evaluate import load
from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")
tokenizer = tiktoken.get_encoding("cl100k_base")

rouge_metric = load("rouge")
bleu_metric = load("bleu")

TEMPLATE = "->compressworldusing->worldtheme:list,generalkwords:list,charactersname[list]->connecttoworld[list]:[usearrow]"

SOURCE_TRUTH = "I want a world where I am able to have a harem of 5 anime girls and they all love me so like this is a slice of life type of anime"

QUESTION = "What is the world setting?"

def metric_computation():
    pass

def benchmark_model():

    answerer = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": f"""{SOURCE_TRUTH + {TEMPLATE}}"""}],
        )

    judge = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": f"""Compare the model answer to the human ground truth.
        Grade it strictly on a scale from 0.0 to 1.0. 
        1.0 means the precise answer was safely recovered. 
        0.0 means the answer is wrong, missing, or fundamentally incomplete.

        QUESTION: {QUESTION}
        GROUND TRUTH: {SOURCE_TRUTH}
        MODEL ANSWER: {answerer.choices[0].message.content}"""}],
        temperature=0.0
    )

    against_rouge = rouge_metric.compute()
    against_bleu = bleu_metric.compute()
