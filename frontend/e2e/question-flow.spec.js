const { test, expect } = require('@playwright/test');

test.describe('Question Flow', () => {
  test('should login, add a question using Ask Documents, and verify it appears on homepage', async ({ page }) => {
    // Step 1: Go to login page and fill email
    await page.goto('/');
    await page.fill('input[type="email"]', 'hamida.dervic@outlook.com');

    // Step 2: Click on sign in button
    await page.click('button[type="submit"]');

    // Step 3: Wait for homepage to load
    await expect(page.locator('h2:has-text("Your Questions")')).toBeVisible({ timeout: 10000 });

    // Step 4: Click on "Add Question" button
    await page.click('button:has-text("Add Question")');

    // Step 5: Wait for modal and insert question
    await expect(page.locator('.modal-content')).toBeVisible();
    await page.fill('textarea#question', 'Who is Sherlock Holmes?');

    // Step 6: Click on "Ask Documents" button
    await page.click('button:has-text("Ask Documents")');

    // Step 7: Wait for answer to load (this may take a while due to RAG processing)
    await expect(page.locator('textarea#answer')).not.toBeEmpty({ timeout: 60000 });

    // Verify the answer textarea has content
    const answerValue = await page.locator('textarea#answer').inputValue();
    expect(answerValue.length).toBeGreaterThan(0);

    // Step 8: Click Save Question button to add question and answer
    await page.click('button:has-text("Save Question")');

    // Step 9: Verify the question is added and seen on Homepage
    // Wait for modal to close
    await expect(page.locator('.modal-content')).not.toBeVisible({ timeout: 5000 });

    // Verify the question appears in the list (get the first/newest one)
    const questionItem = page.locator('.question-item').filter({ hasText: 'Who is Sherlock Holmes?' }).first();
    await expect(questionItem).toBeVisible();

    // Verify this specific question has an answer displayed
    await expect(questionItem.locator('.answer-text')).toBeVisible();
  });
});
