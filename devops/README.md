# DevOps

### What is DevOps

DevOps is a fairly broad term which encompasses all of the infrastructure, practices, and methodologies surrounding developing a project. Generally, this becomes more important the more people work on a project. This can include bug tracking, contribution management, deployment of changes, etc.

It is worth noting that DevOps practices change from organization to organization, however many of the fundamentals covered in this workshop will be used in some form at any collaborative group/company. The underlying software may change depending on the infrastructure used for a specific project, however the information covered will still be useful not matter what software will be used.

### Issues

Issues are a fundamental part of managing a project on any public platform. They can take many forms, but issues are a way to track bugs, missing features, or any outstanding task for a project. Github offers many features related to issues, but typically a reasonable workflow involves first creating an issue. Once an issue has been created, a maintainer can pick up the issue and work on a fix or implementation. Issues also serve as a semi-reasonable forum for users to ask questions about how to use various aspects of the project. This can be used to identify documentation areas which need more documentation.

#### Labels

Labels are a Github feature which allows for features to be labeled with a category that best applies to them. Good issue labels include bugs, question, feature request, etc. They can be used to let developers/maintainers quickly identify new things that need to be done.

#### Assignees

An assignee is a person who has been assigned to manage an issue. This is informal, but it can be used by a team to link a certain person to a certain issue so they can see all the relevant dialogue on the issue.

### Pull Requests

Pull requests are the de facto way that code changes are merged into collaborative projects. Github (and other git providers) offer a mechanism for code to be reviewed and discussed before being merged into the repository.

#### Forks

Forks are a feature provided by many git providers. It allows an individual (who may not have direct commit access to a project) to create a personal copy of an open source project which they have access to. Once they have access to their fork, they can modify their fork with any desired changes. Once those changes are ready, a pull request can be created to move the changed code from the fork back into the parent project. This is useful when you don't want to give the general public direct commit access to code (this should never be done).

#### Creating a Pull Request

To create a pull request, you simply navigate to the parent project on Github. You can then navigate to the pull request tab and create a new pull request. You will be asked to select a target and a source for the pull request. The target is the branch of the parent repository where you want your new code to end up. The source is the branch (or fork) from which you are sourcing your code changes.

Once you have selected a source and target, you will be asked to title and describe your pull request. Do your best to succinctly describe your changes while following any guidelines for the project you are working on.

#### Branch Protection

Branch protection does not require much description, but it is a useful tool. You can configure a repository such that Github will not allow code to be directly committed to the main/release branch of the repository. That will ensure that all changes are properly reviewed in a pull request before being merged in. This can also ensure that unit tests from Github Actions (explained later) finish running successfully.

#### Code Reviews

A code review is a vital part of the DevOps process. It is what allows other developers on a project to review your code before it becomes a part of the project. Reviewers can approve, deny, or suggest changes to any of your code that you with to merge in with the pull request. The code review interface is fairly self explanatory, and allows for dialogue to occur directly inline against the code in question.

#### Closing Issues Syntax

If a pull request resolves an issue, you can close an issue using certain syntax in the pull request. Please see specific documentation here:

[Linking a pull request to an issue - GitHub Docs](https://docs.github.com/en/issues/tracking-your-work-with-issues/linking-a-pull-request-to-an-issue)

### Github Actions

Github actions (or Gitlab CI/CD if you use Gitlab) is an increasingly popular offering for enabling automated actions based on various events in a projects lifespan. For example, unit tests can be run on every commit for every pull request to ensure that no regressions have occurred in new changes. Another option is deploying a new version of an application when a new release is created. There are infinite possibilities with Github actions, so we will be covering some of the more common use cases here.

#### Continuous Integration

Continuous integration (the CI part of CI/CD) is the idea of automatically running unit tests against every commit to a code base. These can be particularly useful for identifying when a code change breaks a feature or aspect of your project.

There can also be other types of tests such as style checks which ensures that your code matches a certain style for the project. This can dramatically improve readability and consistency across diverse development teams with many members.

#### Continuous Deployment

Continuous deployment (the CD part of CI/CD) is the idea of automatically deploying a new version of software for each new release. This is not going to be covered in depth for this workshop due to the massive variety of options for how to deploy code, however it is worth reading up on and is used by many employers and projects.

#### Writing a Github Action

A full guide to Github Actions (and the most recent syntax) can be found here:

[Essential features of GitHub Actions - GitHub Docs](https://docs.github.com/en/actions/learn-github-actions/essential-features-of-github-actions)

A full guide to Gitlab Runners (and its most recent syntax) can be found here:

[GitLab CI/CD | GitLab](https://docs.gitlab.com/ee/ci/)

### Github Projects

Github projects are a recent project management tool by Github. This is a kanban style board which allows for automatically sorting Issues, Pull Requests, and more into categories which can help track large milestones. This can be used to track releases and new feature development as well as specific sprints for projects (if that model of project management is used).

### Releases (and tags)

Releases are a way for you to distribute your code and a change log for your project. To create a new release, first create a Git tag for a commit that you want to create a release of. Once tagged (and pushed to the repository) you can navigate to the releases tag for a repository. From there, you can fill out the web form describing and naming your release. It also allows you to choose the tag that you want to release the code for.

Release can also trigger actions (such as a continuous deployment action in Github Actions).

