const { test, expect } = require('@playwright/test');
const fs = require('fs');
const { execSync } = require('child_process');

test('smoke', async ({ page }) => {
  execSync('python scripts/generate_blueprint.py');
  await page.goto('http://localhost:3000');
  await page.waitForSelector('canvas');
  // pretend there is an export button
  await page.click('button#export');
  const svg = fs.readFileSync('blueprint/blueprint.svg');
  expect(svg.length).toBeGreaterThan(0);
});
