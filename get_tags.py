import sys, os
import json

sem_var = os.environ.get("POETRY_VERSION", "")
tags = []

if "-" not in sem_var:
    if "+" in sem_var:
        sem_var = sem_var.split("+", maxsplit=1)[0]

    if "." in sem_var:
        major, minor, patch = sem_var.split(".")

        tags.append(f"v{major}")
        tags.append(f"v{major}.{minor}")
        tags.append(f"v{major}.{minor}.{patch}")

if (v := f"v{sem_var}") not in tags and sem_var:
    tags.append(v)

print(f"::set-output name=tags::{json.dumps(tags)}")
