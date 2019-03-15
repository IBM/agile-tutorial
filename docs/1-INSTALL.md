# Installing developer tools and environments

## Setting up GitHub Enterprise environment

1. Go to [IBM GitHub Enterprise](https://github.ibm.com/).
1. Login using your IBM credentials.
1. Update your [profile page](https://github.ibm.com/settings/profile).
1. Install a Git client
    * macOS: Download [GitHub Desktop Client](https://desktop.github.com) or `brew cask install github`.
    * Windows: Download [GitHub Desktop Client](https://desktop.github.com).
    * Fedora: `sudo dnf install git`.
1. Follow the [instructions](https://help.github.com/desktop/guides/getting-started-with-github-desktop/authenticating-to-github/) and setup GitHub Desktop to use <https://github.ibm.com> as GitHub Enterprise server.
    * *Note to Windows users*: In case Firefox cannot handle the operation, copy and paste the URL into Internet Explorer.
1. Define your Git identification credentials according to your [profile page](https://github.ibm.com/settings/profile).
    * macOS and Windows: Under **Preferences / Options**, go to the **Git** tab and fill in your **Name** and **Email** address.
    * Fedora: Open a terminal and enter
        ```Shell
        git config --global user.name "Your Name"
        git config --global user.email "username@br.ibm.com"
        ```
1. (macOS) Open GitHub Desktop and click **Install Command Line Tool...**.

## Setting up Travis CI Enterprise

1. Go to [Travis CI Enterprise](https://travis.ibm.com/).
1. Click **Sign in with GitHub** and enter your w3 credentials.
1. Hover the mouse over your profile name in the top-right corner and click **Accounts**.
1. Click the **Sync account** button on the top-right corner.
1. Access the [`brl-its/agile-tutorial`](https://travis.ibm.com/brl-its/agile-tutorial) dashboard.
1. Analyze the steps of the latest build log and compare it to the commands in the [`.travis.yml`](../.travis.yml) file.
1. Check the status of each build in the [Branches](https://travis.ibm.com/brl-its/agile-tutorial/branches) tab.

## Setting up ZenHub

1. Go to the [ZenHub Browser Extension](https://www.zenhub.com/extension) page.
1. Install the appropriate browser extension (only for Google Chrome and Firefox).
    * *Note*: Alternatively, you can use the [ZenHub Web Application](https://app.zenhub.com/login) in any browser.
1. Sign in with your **GitHub** credentials.
1. Select `neumannrf` as organization and `agile-tutorial` as repository in the [web app](https://app.zenhub.com/workspaces/cloud--iot--ufrj-5c8aff81fd0adb6f09c8371b/boards) or the [ZenHub tab](https://github.com/neumannrf/agile-tutorial#zenhub) using the browser extension.

## Installing Visual Studio Code

1. Go to [Visual Studio Code download page](https://code.visualstudio.com/Download).
    * *Note*: Consider changing temporarily to the **IBMInternet** WiFi network if the download fails
1. Choose the installer according to your operational system and follow the instructions.
    * *Note to macOS users*: You can also do `brew cask install visual-studio-code`.
1. Open Visual Studio Code and install extensions
    * Python: [click "Install"](https://marketplace.visualstudio.com/items?itemName=ms-python.python) or hit `Ctrl + P` and enter `ext install ms-python.python`.
    * Output Colorizer: [click "Install"](https://marketplace.visualstudio.com/items?itemName=IBM.output-colorizer) or hit `Ctrl + P` and enter `ext install IBM.output-colorizer`.
    * EditorConfig for VS Code: [click "Install"](https://marketplace.visualstudio.com/items?itemName=EditorConfig.EditorConfig) or hit `Ctrl + P` and enter `ext install EditorConfig`.
