# Hardcoded credentials
# CWE-798 | Severity: HIGH
# File: scripts/create-astrid-094-fixture.py line 103

**Risk:** Credentials hardcoded in source. Anyone with repo access can extract them.

**Fix:** Use os.environ.get('SECRET') or a secrets manager. Never commit credentials.
