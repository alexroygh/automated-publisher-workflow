from human_feedback.feedback_loop import human_feedback_loop
from unittest.mock import patch

def test_human_feedback_loop_keeps_content():
    with patch("builtins.input", return_value=""):
        result = human_feedback_loop("original content")
        assert result == "original content"

def test_human_feedback_loop_returns_user_input():
    with patch("builtins.input", return_value="user edit"):
        result = human_feedback_loop("original content")
        assert result == "user edit" 