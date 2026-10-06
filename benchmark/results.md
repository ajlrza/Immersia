# BENCHMARK RESULTS

Immersia's Token Compaction Prompt:
**->compressworldusing->worldtheme:list,generalkwords:list,charactersname[list]->worldconnect[]**

The Token Compaction Prompt is appended alongside the user's very first prompt payload 
that is used to build the world setting that acts as the logical and semantic anchor 
for each API calls to LLMs.

WORLD SETTING:
world theme: anime,romance, enticing
general kwords: aot-like,naruto
characters name:aj

WORLD EVENTS:
#N1: char alive:0.2 | char dead:0.8
#N2: still here:0.9 | i left:0.1
#N3: tolerated:0.5 | no more:0.5
#E: N1->N2 | N2->N3

## BENCHMARK USED
                    ┌─── Lexical Metrics (ROUGE / BLEU) ───► Measures Word-level Retention
                     ├─── Semantic Alignment (BERTScore) ───► Measures Contextual Vector Drift
Compressed Output ───┼─── Factual Entailment (SummaC) ──────► Measures Hallucination / Contradiction
                     └─── Information Recovery (QAFactEval) ─► Measures downstream Task Reconstruction

    