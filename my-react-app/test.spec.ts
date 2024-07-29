import { test, expect } from '@playwright/test';

test('login page should load and allow login', async ({ page }) => {
  await page.goto('http://localhost:3000/login');
  await page.fill('input[name="username"]', 'testuser');
  await page.fill('input[name="password"]', 'testpass');
  await page.click('button[type="submit"]');
  await expect(page).toHaveURL('http://localhost:3000/home');
  await expect(page.locator('text=Welcome, testuser')).toBeVisible();
});

test('user management should list users', async ({ page }) => {
  await page.goto('http://localhost:3000/user-management');
  await expect(page.locator('text=Username')).toBeVisible();
  await expect(page.locator('text=Email')).toBeVisible();
});
