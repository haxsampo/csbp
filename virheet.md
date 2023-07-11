LINK: https://github.com/haxsampo/csbp
Installation instructions: when cloned the server should run with
`python manage.py runserver`

Writer of this essay used OWASP 2012 top ten list. Used django version was 3.1, as the given template and its docs were for that version. 

FLAW 1. CSRF
source link: https://github.com/haxsampo/csbp/blob/a3c0cae102e1b2a90b800cb7077858f5f30bdaad/polls/views.py#L11
The app doesn't currently use CSRF tokens. Tokens are carried by session and each request, and if they do not match the request is rejected. 
Django provides a csrf middleware to protect from csrf attacks. To fix the current bug in the code, the @csrf_exempt tags ought to be changed to @csrf_protect, as well as adding the correct imports to the view files. That is `from django.views.decorators.csrf import csrf_protect`

2. FLAW 2 https://owasp.org/Top10/A09_2021-Security_Logging_and_Monitoring_Failures/
Django (at least 3.1) doesn't natively catch and log csrf attacks.
One way to fix this problem would be to add "CSRF_FAILURE_VIEW = 'app_name.views.csrf_failure'" to https://github.com/haxsampo/csbp/blob/master/csb/settings.py and then add then add something like `def csrf_failure(request, reason=""):
    # Do stuff here.
    return HttpResponse(status=403)` https://github.com/haxsampo/csbp/blob/master/polls/views.py



3. A03:2021-Injection (tee joku)

4. ssrf (race condition) A10:2021 – Server-Side Request Forgery (SSRF)
   exists for multiple users polling at the same exact moment
   https://docs.djangoproject.com/en/3.1/ref/models/expressions/#avoiding-race-conditions-using-f

5. A01:2021 – Broken Access Control

   vulnerability to path traversal as explained here https://security.snyk.io/vuln/SNYK-PYTHON-DJANGO-1298665 fixed by upgrading to higher version of Django.
