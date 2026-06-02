const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.launch();
  const context = await browser.newContext({
      viewport: { width: 375, height: 812 }, // iPhone X
      userAgent: 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1'
  });
  const page = await context.newPage();
  
  page.on('console', msg => console.log('Browser log:', msg.text()));
  page.on('pageerror', err => console.log('Browser error:', err.message));
  
  await page.goto('https://london-family-trip-2026.surge.sh/');
  console.log('Loaded page');
  
  const vidsTab = await page.$('button:has-text("行前神遊")');
  if (vidsTab) {
      console.log('Clicking videos tab...');
      await vidsTab.click();
      await page.waitForTimeout(1000);
      const isVisible = await page.evaluate(() => {
          const el = document.querySelector('[x-show="activeTab === \\'videos\\'"]');
          return el ? window.getComputedStyle(el).display !== 'none' : false;
      });
      console.log('Videos tab visible after click?', isVisible);
  } else {
      console.log('Could not find videos tab button');
  }
  
  await browser.close();
})();
