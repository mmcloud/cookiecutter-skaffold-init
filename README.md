# Cookiecutter Skaffold Init

Part 1 of my blog please see: (skaffold-installation)[https://www.matthewmcleod.co.uk/skaffold-installation/]


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
