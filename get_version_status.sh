#/bin/bash


if (curl -Ls https://pypi.org/pypi/$pythonPackage/json | grep "Error code 404")
then
    remoteExists=0
else
    remoteExists=1
fi

localVersion=$(poetry version --short)
diff=0

echo "repo_poetry_version=$localVersion" >> $GITHUB_OUTPUT

if [ $remoteExists -eq 1 ]
then
    latestVersion=$(curl -Ls https://pypi.org/pypi/$pythonPackage/json | jq -r .info.version)
    if [ "$localVersion" != "$latestVersion" ]
    then
        diff=1
    fi
fi

if [ $diff -eq 1 ]
then
    echo "pypi_version_difference=true" >> $GITHUB_OUTPUT
else
    echo "pypi_version_difference=false" >> $GITHUB_OUTPUT
fi

if [ $remoteExists -eq 1 ]
then
    echo "pypi_package_exists=true" >> $GITHUB_OUTPUT
else
    echo "pypi_package_exists=true" >> $GITHUB_OUTPUT
fi