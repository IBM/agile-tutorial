# Installing developer tools and environments

## Setting up GitHub Enterprise environment

1. Go to [IBM GitHub Enterprise](https://github.ibm.com/).
1. Login using your IBM credentials.
1. Update your [profile page](https://github.ibm.com/settings/profile).
1. Install a Git client
    * macOS: Download [GitHub Desktop Client](https://desktop.github.com) or `brew cask install github`.
    * Windows: Download [GitHub Desktop Client](https://desktop.github.com).
    * Fedora: `sudo dnf install git`.
1. Follow the [instructions](https://help.github.com/desktop/guides/getting-started-with-github-desktop/setting-up-github-desktop/) to setup GitHub Desktop to use <https://github.ibm.com> as GitHub Enterprise server.
    * *Note to Windows users*: In case Firefox cannot handle the operation, copy and paste the URL into Internet Explorer.
1. Define your Git identification credentials
    * macOS and Windows: Under **Preferences / Options**, go to the **Git** tab and fill in your **Name** and **Email** address.
    * Fedora: Open a terminal and enter
        ```Shell
        git config --global user.name "Your Name"
        git config --global user.email "username@br.ibm.com"
        ```
1. (macOS) Open GitHub Desktop and click **Install Command Line Tool...**.

## Installing Visual Studio Code

1. Go to [Visual Studio Code download page](https://code.visualstudio.com/Download).
    * *Note*: Consider changing temporarily to the **IBMInternet** WiFi network if the download fails
1. Choose the installer according to your operational system and follow the instructions.
    * *Note to macOS users*: You can also do `brew cask install visual-studio-code`.
1. Open Visual Studio Code and install extensions
    * Python: [click "Install"](https://marketplace.visualstudio.com/items?itemName=ms-python.python) or hit `Ctrl + P` and enter `ext install ms-python.python`.
    * Output Colorizer: [click "Install"](https://marketplace.visualstudio.com/items?itemName=IBM.output-colorizer) or hit `Ctrl + P` and enter `ext install IBM.output-colorizer`.
    * EditorConfig for VS Code: [click "Install"](https://marketplace.visualstudio.com/items?itemName=EditorConfig.EditorConfig) or hit `Ctrl + P` and enter `ext install EditorConfig`.
