from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto('file:///Users/nelly/Documents/Antigravity/Europe%20Trip%202026/London_Trip_Map.html')
    
    # Wait for Alpine to initialize
    page.wait_for_timeout(1000)
    
    # Check if videos tab is visible initially
    print("Videos tab visible initially:", page.locator("text=行前神遊影片").is_visible())
    
    # Click on the videos tab button
    print("Clicking Videos button...")
    page.locator("button:has-text('行前神遊')").click(force=True)
    
    page.wait_for_timeout(500)
    
    # Check if videos tab is visible now
    print("Videos tab visible after click:", page.locator("text=行前神遊影片").is_visible())
    
    # Get console logs
    browser.close()
