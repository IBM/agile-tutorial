# Developing an application collaboratively

## Using Slack to monitor the development cycle

1. Open the [`agile-tutorial`](https://ibm-research.slack.com/messages/GF23AGU4A) Slack channel.
1. Note how every `git push` generates a message from **GitHub Enterprise** bot.
1. Note how every automated build generates a message from **Travis CI Enterprise** bot.
1. Note how every issue closed or created generates a message from **GitHub Enterprise** bot.
1. Note how every modification of an issue's details generates a message from **ZenHub** bot.

## Planning the sprint

In this section we will go over the practical steps that were broadly described in [*Having SCRUM meetings*](2-UNDERSTAND.md#having-scrum-meetings).
We will assume, for the sake of this exercise, that **each sprint lasts 15 minutes**.

1. Open the [ZenHub board](https://github.ibm.com/brl-its/agile-tutorial#zenhub) or [web application](https://zenhub.ibm.com/app/workspaces/agile-tutorial-5c240173b7d41fe10dbe52e6/boards).
1. Discuss with the **SCRUM master** which issues should be addressed during this sprint.
1. Once identified, move these issues to the **Sprint Backlog**.
1. Assign these issues to the appropriate sprint using **Set milestone**.
1. Discuss among the **Development team** who should address each issue.
1. Once you identified your issue, click on it to open the detailed description.
1. Assign it to yourself using the menu on the right.
1. Read the issue description and use the **Labels** menu to mark it as `question` if you need further information.
1. Discuss your questions with the SCRUM master and make sure there is **no blocking issue** preventing you.
1. When you are ready to start contributing, move your assigned issue to **In Progress**.

## Contributing to your branch

In this section we will go over the practical steps that were broadly described in [*Using the "GitHub Flow" branching model*](2-UNDERSTAND.md#using-the-github-flow-branching-model).

1. Open the `agile-tutorial` repository in Visual Studio Code.
1. Click the :arrows_counterclockwise: icon in the bottom left corner to synchronise your local repository with GitHub Enterprise.
1. Click the `master` button in the bottom left corner and select **Create new branch**.
1. Choose a descriptive name for your branch that resembles the issue that it addresses.
    * *Example*: `basic_input-3` is a *very good* name for [issue #3](https://github.ibm.com/brl-its/agile-tutorial/issues/3) (Create `/basic/input` resource).
1. Perform all the code changes described in your issue.
1. Open the **Source Control** panel in the top left bar.
1. Click the `+` icon next to all the modified files to **Stage Changes**.
1. Write a meaningful commit message that explains the changes introduced by this commit.
1. Click the :heavy_check_mark: icon in the top left to commit your changes to your local repository.
1. Click the :arrows_counterclockwise: icon in the bottom left to synchronise your local repository with GitHub Enterprise.

## Submitting your Pull Request

1. After your commits have been synchronised, open the [`brl-its/agile-tutorial`](https://github.ibm.com/brl-its/agile-tutorial) repository.
1. Select your branch from the drop-down menu on the left and then click **New pull request**.
1. Write a meaningful title for the Pull Request, preferably one that refers to the issue that it addresses.
1. Describe the changes introduced by the Pull Request in the **Summary** section.
1. Revise the **Checklist**, marking actions as "done" using `[x]`.
1. Add the number `#N` of the **Related Issue** that is closed by this Pull Request.
1. In case there is any information that would help the reviewer, add it to **Notes to Reviewer**.
1. Select the SCRUM master as reviewer from the **Reviewers** menu on the right.
1. Assign yourself from the **Assignees** menu on the right.
1. Select the appropriate labels from the **Labels** menu on the right.
1. Click the **Connect with an issue** button and enter the related issue number.
1. Submit the Pull Request using the **Create pull request** button.

## Tracking status checks

1. Once submitted, find your Pull Request in the [open PR list](https://github.ibm.com/brl-its/agile-tutorial/pulls).
1. Scroll to the bottom and look for the status checks.
1. Click **Show all checks** and click **Detail** to see the Travis CI build log.
1. In the Travis CI build log, make sure
    * all files are compliant with `flake8` linter
    * all tests in `test/*_test.py` have **PASSED**
    * all files in `src/*.py` have **100%** test coverage.
1. If the build failed for any reason, go back to Visual Studio Code, perform the required changes, commit and synchronise your work.
1. Re-do the status checks by monitoring the new [Travis CI build](https://travis.ibm.com/brl-its/agile-tutorial/branches) in your branch.

## Merging and moving on

1. Once the status checks are all successful warn the reviewer that your Pull Request is pending approval.
1. The reviewer will either **Approve** or **Request changes** to your PR.
1. If the reviewer **Requested changes**, you should address them by submitting new code to your branch.
1. If the reviewer **Approved** your Pull Request, no action is required.
1. After all the approvals, status checks and branch protections have been satisfied, your branch will be merged into `master`.
1. Go back to Visual Studio Code and click the button with your branch name in the bottom left corner.
1. Synchronise your local `master` branch with that of GitHub Enterprise by clicking the :arrows_counterclockwise: icon on the bottom left bar.
1. Get ready for the next sprint!!!