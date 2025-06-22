import pytest
from ai_agents.agent_api import split_text, get_multiline_input, agentic_flow
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

def test_get_multiline_input_keeps_content():
    # Simulate user entering two lines and then END
    with patch("builtins.input", side_effect=["line1", "line2", "END"]):
        result = get_multiline_input()
        assert result == "line1\nline2"

def test_agentic_flow_all_accepts():
    chapter = "First sentence. Second sentence."
    with patch("ai_agents.agent_api.split_text", return_value=["chunk1", "chunk2"]), \
         patch("ai_agents.agent_api.ai_writer", side_effect=["writer1", "writer2"]), \
         patch("ai_agents.agent_api.ai_reviewer", side_effect=["reviewer1", "reviewer2"]), \
         patch("ai_agents.agent_api.ai_editor", side_effect=["editor1", "editor2"]):
        # Always accept ("y" for draft, review, and "n" for edit loop)
        def always_accept(prompt=None):
            if prompt and "revise" in prompt:
                return "n"
            return "y"
        with patch("builtins.input", side_effect=always_accept):
            result = agentic_flow(chapter)
            assert "editor1" in result and "editor2" in result

def test_agentic_flow_with_user_edits():
    chapter = "Only one chunk."
    with patch("ai_agents.agent_api.split_text", return_value=["chunk1"]), \
         patch("ai_agents.agent_api.ai_writer", return_value="writer1"), \
         patch("ai_agents.agent_api.ai_reviewer", return_value="reviewer1"), \
         patch("ai_agents.agent_api.ai_editor", return_value="editor1"):
        # Always reject ("n") to trigger get_multiline_input, and always "y" once for edit, then "n"
        def always_n(*args, **kwargs):
            return "n"
        def always_edit(*args, **kwargs):
            return "user edit"
        with patch("builtins.input", side_effect=["n", "n", "y", "n"]), \
             patch("ai_agents.agent_api.get_multiline_input", side_effect=["user draft", "user review", "user edit"]):
            result = agentic_flow(chapter)
            assert "user draft" in result or "user review" in result or "user edit" in result 