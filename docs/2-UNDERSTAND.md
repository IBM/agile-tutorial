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
1. Everything that happens during the SCRUM cycle must be documented in an [issue board](https://en.wikipedia.org/wiki/Kanban_board).
1. Keep the board **always up-to-date**.

## Using the "GitHub Flow" branching model

1. Read the [GitHub Flow](https://guides.github.com/introduction/flow/) branching model documentation.
1. Locate the issue that has been assigned to you in the [ZenHub board](https://zenhub.ibm.com/app/workspaces/agile-tutorial-5c240173b7d41fe10dbe52e6/boards).
1. Create a new [branch](https://help.github.com/articles/github-glossary/#branch) from `master`, making sure the branch name resembles the associated issue.
1. Add new code to your branch by making [commits](https://help.github.com/articles/github-glossary/#commit) and writing meaningful commit messages.
1. Create a [Pull Request](https://help.github.com/articles/github-glossary/#pull-request) from your branch into branch `master` and explain the proposed changes.
1. Discuss you submission in the Pull Request review process, ensuring all [status checks](https://help.github.com/articles/github-glossary/#status-checks) are successful.
1. Once the Pull Request has been approved, [merge](https://help.github.com/articles/github-glossary/#merge) your branch into `master`.

## Automating integration, delivery and deployment

1. [Continuous Integration](https://en.wikipedia.org/wiki/Continuous_integration) is the practice of merging all developer branches into the `master` branch as often as possible.
1. [Continuous Delivery](https://en.wikipedia.org/wiki/Continuous_delivery) is the practice of producing fully working (tested) incremental updates that could potentially be deployed at any time.
1. [Continuous Deployment](https://en.wikipedia.org/wiki/Continuous_deployment) is the practice to automating the deployments of each new version that is delivered.
1. Although there are overlaps between those concepts, when they are all applied, one ends up with
    * a single source code repository
    * automated builds
    * automated tests
    * automated deployments
