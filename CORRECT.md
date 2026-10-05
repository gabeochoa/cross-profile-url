# CORRECT — cross-profile-url (tiny repo: 5 commits, 2 real classes)
| # | Class | Evidence (2+) | Level / why | Guard (fails on past) | Commit |
|---|---|---|---|---|---|
|1|URL interpolated into a shell command (RCE)|cbc8781 unquoted `{url}` shell=True; 305f291 "fix" only wrapped url in quotes — embedded `"` still breaks out (same mistake, second form)|Architecture — `subprocess.run(argv)`, no shell at all; type-level validation http(s)+netloc, profile allowlist|`test_oip.py`: evil url is exactly one argv element, shell unset, non-http rejected; old oip.py has shell=True -> source test fails|2ce659c|
|2|Native-host protocol violated / silent crash|oip.py `print()` to stdout (the length-prefixed wire) x2 + `data['url']`/bad-length raising with no response; JS side of same class fixed 8d91920 (`!response`)|Architecture — every path returns one framed `{success}`; diagnostics stderr only|`test_oip.ProtocolT`: missing-url input gets success=False, bare print() forbidden; old code raised KeyError/printed -> fails|6857b79|

## Rule table
| Do | Never |
|---|---|
|Pass URLs as single argv elements; validate scheme before launch|`shell=True`, f-string commands, quoting-as-sanitising|
|Reply framed on every path; log to stderr| `print()` in oip.py; let exceptions escape main()|
Run: `python3 -m unittest`
