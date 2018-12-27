# Understanding agile development practices and frameworks

## Having SCRUM meetings

1. The SCRUM methodology is characterized by having specific [roles](https://en.wikipedia.org/wiki/Scrum_(software_development)#Roles) and [workflows](https://en.wikipedia.org/wiki/Scrum_(software_development)#Workflow).
1. The SCRUM [roles](https://en.wikipedia.org/wiki/Scrum_(software_development)#Roles) can be summarized as
    * Product Owner: represents the product's stakeholders and the voice of the customer.
    * Scrum master: a facilitator that helps to ensure the team follows the agreed processes.
    * Development team: responsible for delivering potentially shippable product increments.
1. The SCRUM [workflows](https://en.wikipedia.org/wiki/Scrum_(software_development)#Workflow) can be summarized as
    * Sprint planning: bi-weekly meetings for agreeing on the tasks to be done during that sprint.
    * Daily scrum: 15-min meeting to report on what was done the previous day, the plans for that day and potential impediments.
    * Sprint review: after the sprint, the team reviews what was done and what can be improved in the next sprints.
1. Everything that happens during the SCRUM cycle should be captured in a [issue board](https://en.wikipedia.org/wiki/Kanban_board) which should be **always up-to-date**.

## Using the "GitHub Flow" branching model

1. Read the [GitHub Flow](https://guides.github.com/introduction/flow/) branching model documentation.
1. Locate the issue that has been assigned to you in the [ZenHub board](https://zenhub.ibm.com/app/workspaces/agile-tutorial-5c240173b7d41fe10dbe52e6/boards).
1. Create a new [branch](https://help.github.com/articles/github-glossary/#branch) from `master`, making sure the branch name resembles the associated issue.
1. Add new code to your branch by making [commits](https://help.github.com/articles/github-glossary/#commit) and writing meaningful commit messages.
1. Create a [Pull Request](https://help.github.com/articles/github-glossary/#pull-request) from your branch into branch `master` and explain the proposed changes.
1. Discuss you submission in the Pull Request review process, ensuring all [status checks](https://help.github.com/articles/github-glossary/#status-checks) are successful.
1. Once the Pull Request has been approved, [merge](https://help.github.com/articles/github-glossary/#merge) your branch into `master`.

## Submitting a Pull Request

1. After all commits have been made to your branch, open the [`brl-its/agile-tutorial`](https://github.ibm.com/brl-its/agile-tutorial) repository on GitHub.
1. Select your branch from the drop-down menu on the left and then click **New pull request**.
1. Write a meaningful title for the Pull Request, preferably one that refers to the issue that it addresses.
1. Describe the changes introduced by the Pull Request in the **Summary** section.
1. Revise the **Checklist**, marking actions as "done" using `[x]`.
1. Add the number `#N` of the **Related Issue** that is closed by this Pull Request.
1. In case there is any information that would help the reviewer, add it to **Notes to Reviewer**.
1. Select a reviewer from the **Reviewers** menu on the right.
1. Assign yourself from the **Assignees** menu on the right.
1. Select the appropriate labels from the **Labels** menu on the right.
1. Click the **Connect with an issue** button and enter the related issue number.
1. Submit the Pull Request using the **Create pull request** (green) button.

## Tracking test status and coverage

1. Once submitted, find your Pull Request in the [open PR list](https://github.ibm.com/brl-its/agile-tutorial/pulls).
1. Scroll to the bottom and look for the status checks.
1. Click **Show all checks** and click **Detail** to see the Travis CI build log.
1. In the Travis CI build log, make sure
    * all files are compliant with `flake8` linter
    * all tests in `test/*_test.py` have **PASSED**
    * all files in `src/*.py` have **100%** test coverage.
