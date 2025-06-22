from human_feedback.feedback_loop import human_feedback_loop
from unittest.mock import patch

def test_human_feedback_loop_keeps_content():
    # Simulate user pressing END immediately
    with patch("builtins.input", side_effect=["END"]):
        result = human_feedback_loop("original content")
        assert result == "original content"

def test_human_feedback_loop_returns_user_input():
    # Simulate user entering a line, then END to break
    with patch("builtins.input", side_effect=["user edit", "END"]):
        result = human_feedback_loop("original content")
        assert result == "user edit" 