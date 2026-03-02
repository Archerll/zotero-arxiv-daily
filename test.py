import os
secrets = ["ZOTERO_ID", "ZOTERO_KEY", "SENDER", "RECEIVER", "SENDER_PASSWORD", "OPENAI_API_KEY", "OPENAI_API_BASE"]
for secret in secrets:
    val = os.environ.get(secret, "")
    print(f"{secret}: length={len(val)}, startswith={val[:5]}")
