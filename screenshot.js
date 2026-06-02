const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('file:///Users/nelly/Documents/Antigravity/Europe%20Trip%202026/London_Trip_Map.html');
  await page.waitForTimeout(3000);
  await page.screenshot({ path: 'screenshot.png' });
  await browser.close();
})();
