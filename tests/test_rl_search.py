from rl_search.rl_search import rl_search, rank_with_rl
from unittest.mock import patch, MagicMock

def test_rank_with_rl_returns_best_candidate():
    candidates = ["doc1", "doc2", "doc3"]
    fake_client = MagicMock()
    # doc1: 5, doc2: 8, doc3: 3
    def fake_create(*args, **kwargs):
        content_map = {"doc1": "5", "doc2": "8", "doc3": "3"}
        doc = kwargs["messages"][1]["content"].split("Content: ")[1].split("\n")[0]
        resp = MagicMock()
        resp.message = MagicMock(content=content_map[doc])
        return MagicMock(choices=[resp])
    fake_client.chat.completions.create.side_effect = fake_create
    with patch("rl_search.rl_search.openai.OpenAI", return_value=fake_client), \
         patch("rl_search.rl_search.np.argmax", return_value=1):
        best = rank_with_rl("query", candidates)
        assert best == "doc2"

def test_rank_with_rl_handles_exception():
    candidates = ["doc1"]
    fake_client = MagicMock()
    fake_client.chat.completions.create.side_effect = Exception("API error")
    with patch("rl_search.rl_search.openai.OpenAI", return_value=fake_client), \
         patch("rl_search.rl_search.np.argmax", return_value=0):
        best = rank_with_rl("query", candidates)
        assert best == "doc1"

def test_rl_search_returns_ranked_result():
    def fake_search_fn(query, n_results):
        return {"documents": [["docA"], ["docB"]]}
    with patch("rl_search.rl_search.rank_with_rl", return_value="docA"):
        result = rl_search("query", fake_search_fn)
        assert result == "docA"

def test_rl_search_no_documents():
    def fake_search_fn(query, n_results):
        return {"no_documents": []}
    result = rl_search("query", fake_search_fn)
    assert result == "No match found." 