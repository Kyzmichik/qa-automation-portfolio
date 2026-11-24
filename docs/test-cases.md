# Manual test cases — SauceDemo checkout

Application: https://www.saucedemo.com  
Each case is also covered by an automated test (column **Automated**).

| ID | Title | Preconditions | Steps | Expected result | Priority | Automated |
|----|-------|---------------|-------|-----------------|----------|-----------|
| TC-01 | Login with valid credentials | Login page is open | 1. Enter `standard_user` 2. Enter `secret_sauce` 3. Click **Login** | Products page opens, URL contains `/inventory.html` | High | `test_login_with_valid_credentials` |
| TC-02 | Login with empty username | Login page is open | 1. Leave username empty 2. Enter password 3. Click **Login** | Error "Username is required" | Medium | `test_login_negative[empty-username]` |
| TC-03 | Login as locked-out user | Login page is open | 1. Enter `locked_out_user` 2. Enter `secret_sauce` 3. Click **Login** | Error "Sorry, this user has been locked out" | High | `test_login_negative[locked-out-user]` |
| TC-04 | Direct access without login | User is logged out | 1. Open `/inventory.html` directly | Login page with an access error is shown | High | `test_inventory_is_protected_without_login` |
| TC-05 | Add item to cart | User is logged in | 1. Click **Add to cart** on "Sauce Labs Backpack" | Cart badge shows **1** | High | `test_add_item_updates_cart_badge` |
| TC-06 | Remove item from cart | 1 item in cart | 1. Click **Remove** on the item | Cart badge disappears | Medium | `test_remove_item_clears_cart_badge` |
| TC-07 | Sort by price low → high | User is logged in | 1. Select "Price (low to high)" | Prices are in ascending order | Low | `test_sort_by_price` |
| TC-08 | Checkout without first name | Item in cart, checkout form open | 1. Leave First Name empty 2. Fill other fields 3. Click **Continue** | Error "First Name is required" | Medium | `test_checkout_form_validation[no-first-name]` |
| TC-09 | Order total calculation | Item in cart, checkout overview open | 1. Compare Item total, Tax and Total | Total = Item total + Tax | High | `test_order_total_equals_subtotal_plus_tax` |
| TC-10 | Complete purchase (E2E) | User is logged in | 1. Add item 2. Open cart 3. Checkout 4. Fill form 5. Finish | "Thank you for your order!" is shown | High | `test_complete_purchase_end_to_end` |
