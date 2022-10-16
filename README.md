# compare-pypi-poetry-version

Github Action to compare pypi and poetry version of repo.

Takes `package_name` as an input (pypi package) - gives step output:

* `pypi_package_exists` - 'true' or 'false' there is a pypi item for this repo
* `pypi_version_difference` - 'true' or 'false' if there is a difference between poetry and pypi version
* `repo_poetry_version` - the current version in poetry (`poetry version --short`).
* `repo_poetry_version_tags` - space-seperated list of tags based on version (e.g. 'v1.3.2 v1.3 v1')
