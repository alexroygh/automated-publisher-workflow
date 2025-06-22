import pytest
from ai_agents.agent_api import split_text
from unittest.mock import patch, MagicMock

def test_split_text_basic():
    text = "Sentence one. Sentence two! Sentence three?"
    # Patch tiktoken to count tokens as words for simplicity
    with patch("ai_agents.agent_api.tiktoken.encoding_for_model") as mock_enc:
        mock_encoder = MagicMock()
        mock_encoder.encode.side_effect = lambda s: s.split()
        mock_enc.return_value = mock_encoder
        chunks = split_text(text, max_tokens=3)
        assert len(chunks) == 3
        assert all(chunk for chunk in chunks)

def test_split_text_long_sentence():
    text = "This is a very long sentence that should be split if it exceeds the token limit."
    with patch("ai_agents.agent_api.tiktoken.encoding_for_model") as mock_enc:
        mock_encoder = MagicMock()
        mock_encoder.encode.side_effect = lambda s: s.split()
        mock_enc.return_value = mock_encoder
        chunks = split_text(text, max_tokens=2)
        assert len(chunks) >= 1
        assert any("long sentence" in chunk for chunk in chunks) 