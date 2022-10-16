import sys, os

def add_to_step_output(**kwargs):
    """
    Add kwargs to the step outputs
    """
    with open(os.environ["GITHUB_OUTPUT"], 'a') as f:
        for k, v in kwargs.items():
            f.write(f'\n"{k}"="{v}"')

sem_var = os.environ.get("POETRY_VERSION", "")
print(f"Current version is {sem_var}")
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

print(tags)
space_seperated_tags = " ".join(tags)

add_to_step_output(repo_poetry_version_tags=space_seperated_tags)