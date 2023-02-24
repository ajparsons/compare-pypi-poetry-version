# Compare Pypi and Poetry version

Version: 1.0.0

Create outputs future steps can use depending if the pypi version is out of sync

## Usage

```yaml

# It is better practice to use the SHA hash of this tag rather than the tag itself.
- uses: ajparsons/compare-pypi-poetry-version@v1
  id: example-step 
  with:
    package_name: '' 

```

## Inputs

### package_name

Required.

Name of pypi package

## Outputs

### pypi_package_exists

'true' or 'false' there is a pypi item for this repo

### pypi_version_difference

'true' or 'false' if there is a difference between poetry and pypi version

### repo_poetry_version

Current poetry semvar version

