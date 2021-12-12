# Cookiecutter Skaffold Init

This repo is used to demo my blog posts to read more information on whats going on please see the following posts

## Sections

1) For [skaffold-installation](https://www.matthewmcleod.co.uk/skaffold-installation/)

    ```bash
    cookiecutter https://github.com/mmcloud/cookiecutter-skaffold-init --checkout v1.0.0
    ```

2) For [skaffold-profiles](https://www.matthewmcleod.co.uk/skaffold-profiles)

    ```bash
    cookiecutter https://github.com/mmcloud/cookiecutter-skaffold-init --checkout v2.0.0
    ```

3) For [skaffold-helm](https://www.matthewmcleod.co.uk/skaffold-helm)

    ```bash
    cookiecutter https://github.com/mmcloud/cookiecutter-skaffold-init --checkout v3.0.0
    ```


## Quick start


1) Install cookiecutter

    ```bash
    pip3 install cookiecutter
    ```

2) Generate template

    ```bash
    cookiecutter https://github.com/mmcloud/cookiecutter-skaffold-init
    ```

3) Change directory to generated folder (demo directory is default, change according to inputted project slug)

    ```bash
    cd demo
    ```

4) Start Minikube

    ```bash
    minikube start
    ```

5) Develop using skaffold or use cloudcode plugin

    ```bash
    skaffold dev
    ```
