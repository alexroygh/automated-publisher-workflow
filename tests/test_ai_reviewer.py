from ai_agents.ai_reviewer import ai_reviewer
from unittest.mock import patch, MagicMock

def test_ai_reviewer_returns_reviewed_text():
    fake_client = MagicMock()
    fake_response = MagicMock()
    fake_response.choices = [MagicMock(message=MagicMock(content="Reviewed text."))]
    fake_client.chat.completions.create.return_value = fake_response
    with patch("ai_agents.ai_reviewer.openai.OpenAI", return_value=fake_client):
        result = ai_reviewer("Some draft text.")
        assert result == "Reviewed text."

def test_ai_reviewer_handles_exception():
    fake_client = MagicMock()
    fake_client.chat.completions.create.side_effect = Exception("API error")
    with patch("ai_agents.ai_reviewer.openai.OpenAI", return_value=fake_client):
        result = ai_reviewer("Some draft text.")
        assert "Error generating AI reviewer output" in result 