# Security audit: unicity-aos/aos-ce

Date: 2026-11-12 | Auditor: [mutsuumii](https://github.com/mutsuumii)

## Summary

Found 1 issue(s): 1 high.

## Findings

### 1. [HIGH] Hardcoded credentials

**CWE-798** | `scripts/create-astrid-094-fixture.py` line 103

Credentials hardcoded in source. Anyone with repo access can extract them.

```
write(root, "secrets/providers.toml", 'token = "synthetic-secret"\n')
```

**Fix:** Use os.environ.get('SECRET') or a secrets manager. Never commit credentials.
---
