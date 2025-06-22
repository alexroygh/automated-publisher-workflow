from ai_agents.ai_editor import ai_editor
from unittest.mock import patch, MagicMock

def test_ai_editor_returns_polished_text():
    fake_client = MagicMock()
    fake_response = MagicMock()
    fake_response.choices = [MagicMock(message=MagicMock(content="Polished text."))]
    fake_client.chat.completions.create.return_value = fake_response
    with patch("ai_agents.ai_editor.openai.OpenAI", return_value=fake_client):
        result = ai_editor("Some raw text.")
        assert result == "Polished text."

def test_ai_editor_handles_exception():
    fake_client = MagicMock()
    fake_client.chat.completions.create.side_effect = Exception("API error")
    with patch("ai_agents.ai_editor.openai.OpenAI", return_value=fake_client):
        result = ai_editor("Some raw text.")
        assert "Error generating AI editor output" in result 