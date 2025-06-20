from playwright.sync_api import sync_playwright
import os

def fetch_chapter_and_screenshot(url, output_dir="output"):
    os.makedirs(output_dir, exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        content = page.content()
        page.screenshot(path=f"{output_dir}/screenshot.png", full_page=True)
        with open(f"{output_dir}/chapter.html", "w", encoding="utf-8") as f:
            f.write(content)
        browser.close()
    return content
