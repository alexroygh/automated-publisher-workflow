from scraping.fetch_chapter import fetch_chapter_and_screenshot
from unittest.mock import patch, MagicMock

def test_fetch_chapter_and_screenshot_mocks_playwright():
    with patch("scraping.fetch_chapter.sync_playwright") as mock_playwright, \
         patch("os.makedirs") as mock_makedirs, \
         patch("builtins.open") as mock_open:
        mock_browser = MagicMock()
        mock_page = MagicMock()
        mock_page.content.return_value = "<html>content</html>"
        mock_browser.new_page.return_value = mock_page
        mock_context = MagicMock()
        mock_context.chromium.launch.return_value = mock_browser
        mock_playwright.return_value.__enter__.return_value = mock_context
        result = fetch_chapter_and_screenshot("http://example.com", output_dir="test_output")
        assert result == "<html>content</html>"
        mock_makedirs.assert_called_once_with("test_output", exist_ok=True)
        mock_page.screenshot.assert_called_once()
        mock_open.assert_called() 