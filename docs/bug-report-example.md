# Bug report example

**ID:** BUG-001  
**Title:** `POST /auth` returns HTTP 200 instead of 401 for invalid credentials  
**Application:** Restful-Booker API — https://restful-booker.herokuapp.com  
**Severity:** Minor · **Priority:** Low  
**Environment:** Public demo API, requests 2.x, Python 3.12

## Steps to reproduce
1. Send `POST /auth` with body:
   ```json
   {"username": "admin", "password": "wrong"}
   ```
2. Check the HTTP status code and response body.

## Expected result
HTTP **401 Unauthorized** — the standard status for failed authentication, so clients can detect the failure by status code.

## Actual result
HTTP **200 OK** with body:
```json
{"reason": "Bad credentials"}
```

## Impact
API clients and monitoring that rely on status codes treat a failed login as a success.

## Evidence
Covered by automated test `tests/api/test_booking_api.py::test_auth_with_invalid_credentials`.

---

*Note: Restful-Booker contains intentional bugs for testing practice. Other observed quirks: `DELETE /booking/{id}` returns 201 instead of 204, `GET /ping` returns 201 instead of 200.*
