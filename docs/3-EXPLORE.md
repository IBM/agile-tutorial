# Exploring the Python application

## Cloning the repository

1. Go to [IBM GitHub Enterprise](https://github.ibm.com/).
1. Login using your IBM credentials.
1. From the drop-down menu on the left, choose the [`brl-its`](https://github.ibm.com/brl-its) organization.
1. Go to the [`agile-tutorial`](https://github.ibm.com/brl-its/agile-tutorial) repository page.
1. Click the green button **Clone or download** and copy the address `git@github.ibm.com:brl-its/agile-tutorial.git`.
1. Open **Visual Studio Code** and summon the **Command Palette** with
    * `Ctrl + Shift + P` in [Fedora](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-linux.pdf)
    * `Ctrl + Shift + P` in [Windows](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-windows.pdf)
    * `Cmd + Shift + P` in [macOS](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-macos.pdf)
1. Type `clone` and select **Git: Clone** from the list.
1. Paste the `git@github.ibm.com:brl-its/agile-tutorial.git` address and select the destination.
1. Open the newly cloned repository.

## Exploring the files

1. The [`.github/`](../.github/) folder contains the templates used when a new issue or pull request is created.
1. The [`docs/`](../docs/) folder contains the step-by-step instructions for the tutorial.
1. The [`src/`](../src/) folder contains the Python code for the API services.
1. The [`test/`](../test/) folder contains the Python code for the API tests.
1. The [`.editorconfig`](../.editorconfig) file contains the standardisation of coding style.
1. The [`.gitignore`](../.gitignore) file contains the names of the files to be ignore by `git`.
1. The [`.travis.yml`](../.travis.yml) file contains the build, test and deploy instructions for Travis CI.
1. The [`LICENSE`](../LICENSE.md) file contains the standard `Apache-2.0` open-source license.
1. The [`Procfile`](../Procfile) file contains the command required to launch the Cloud Foundry Application on IBM Cloud.
1. The [`README.md`](../README.md) file contains the welcome page and table of contents for the tutorial.
1. The [`main.py`](../main.py) file contains the Python code for the API resources.
1. The [`manifest.yml`](../manifest.yml) file contains the definition of the Cloud Foundry Application on IBM Cloud.
1. The [`requirements.txt`](../requirements.txt) file contains the list of Python dependencies.
1. The [`runtime.txt`](../runtime.txt) file contains Python version to be used by the Cloud Foundry Application on IBM Cloud.

## Testing the example implementation

1. Open the <https://agile-tutorial.mybluemix.net/> application in a browser.
1. Click the `default` namespace to expose its API resources.
1. Click the `/answer` API resources to expose its documentation.
1. Click the **Try it out** button and then **Execute**.
1. Confirm if the **Response body** contains the [correct answer](https://goo.gl/6gFWyU).

## Understanding the API resources

1. Open the `agile-tutorial` repository in Visual Studio Code.
1. Open the `main.py` file.
1. Read the code block associated with the `/answer` resource and compare it to the live application.
    * `@api.route()` defines the endpoint URL.
    * `@api.doc()` provides the documentation.
    * `get()` determines the [HTTP method](https://spring.io/understanding/REST#http-methods).
    * `return` calls an external service located in `src/default_services.py`.
1. Note how an external file was included by `from src import default_services as ds`.

## Understanding the API services

1. Open the `agile-tutorial` repository in Visual Studio Code.
1. Open the `src/default_services.py` file.
1. Read the code block associated with the `TheAnswerToLifeTheUniverseAndEverything()` service and compare it to the live application.
    * `TheAnswerToLifeTheUniverseAndEverything()` is the function name evoked in the `return` statement of the `/answer` resource.
    * The documentation block explains the scope of the service and its input/output parameters.
    * `return 42` determines the **Response body** in the live application.

## Understanding the API tests

1. Open the `agile-tutorial` repository in Visual Studio Code.
1. Open the `test/default_test.py` file.
1. Read the code block associated with the `test_answer()` test and compare it to the Travis CI [build log](https://travis.ibm.com/brl-its/agile-tutorial).
    * `from src import default_services as ds` includes the external file containing the service to be tested.
    * `assert` determines what is the expect behaviour for that service.
