Writer of this essay used OWASP 2012 top ten list. 

1. csrf
   @csrf_exempt remove those

2. A09:2021-Security Logging and Monitoring Failures
   doesn't exist

3. A03:2021-Injection (tee joku)

4. ssrf (race condition) A10:2021 – Server-Side Request Forgery (SSRF)
   exists for multiple users polling at the same exact moment
   https://docs.djangoproject.com/en/3.1/ref/models/expressions/#avoiding-race-conditions-using-f

5. A01:2021 – Broken Access Control
   vulnerability to path traversal as explained here https://security.snyk.io/vuln/SNYK-PYTHON-DJANGO-1298665 fixed by upgrading to higher version of Django.
