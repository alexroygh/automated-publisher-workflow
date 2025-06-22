from ai_agents.ai_writer import ai_writer
from unittest.mock import patch, MagicMock

def test_ai_writer_returns_written_text():
    fake_client = MagicMock()
    fake_response = MagicMock()
    fake_response.choices = [MagicMock(message=MagicMock(content="Written text."))]
    fake_client.chat.completions.create.return_value = fake_response
    with patch("ai_agents.ai_writer.openai.OpenAI", return_value=fake_client):
        result = ai_writer("Some chapter text.")
        assert result == "Written text."

def test_ai_writer_handles_exception():
    fake_client = MagicMock()
    fake_client.chat.completions.create.side_effect = Exception("API error")
    with patch("ai_agents.ai_writer.openai.OpenAI", return_value=fake_client):
        result = ai_writer("Some chapter text.")
        assert "Error generating AI writer output" in result 