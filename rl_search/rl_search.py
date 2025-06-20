import os
import numpy as np
import openai

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def rank_with_rl(query, candidates):
    """
    Uses LLM-based reward model to simulate RL-based reranking.
    """
    scores = []
    for doc in candidates:
        try:
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant trained to rank content based on how well it answers a query."},
                    {"role": "user", "content": f"Query: {query}\nContent: {doc}\nScore this from 1 to 10 based on relevance."}
                ],
                temperature=0.3,
                max_tokens=100
            )
            score = int(''.join(filter(str.isdigit, response.choices[0].message.content)))
            scores.append(score)
        except Exception as e:
            scores.append(0)
    best_idx = np.argmax(scores)
    return candidates[best_idx] if candidates else "No candidates found."

def rl_search(query, search_fn):
    """
    Performs RL-style reranking over ChromaDB search results.
    """
    result = search_fn(query, n_results=5)
    if result and "documents" in result:
        documents = [doc[0] for doc in result["documents"]]
        return rank_with_rl(query, documents)
    return "No match found."
