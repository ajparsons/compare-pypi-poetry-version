# compare-pypi-poetry-version

Github Action to compare pypi and poetry version of repo.

Takes `package_name` as an input (pypi package), returns:

* `remote_exists` - 'true' or 'false' there is a pypi item for this repo
* `version_difference` - 'true' or 'false' if there is a difference between poetry and pypi version
* `poetry_version` - the current version in poetry (`poetry version --short`).
* `version_tags` - space-seperated list of tags based on version (e.g. 'v1.3.2 v1.3 v1)
