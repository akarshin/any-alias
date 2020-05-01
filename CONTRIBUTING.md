# Contributing

## How do I... <a name="toc"></a>

* [Use This Guide](#introduction)?
* Ask or Say Something? 🤔🐛😱
  * [Request Support](#request-support)
  * [Report an Error or Bug](#report-an-error-or-bug)
  * [Request a Feature](#request-a-feature)
* Make Something? 🤓👩🏽‍💻📜🍳
  * [Project Setup](#project-setup)
  * [Contribute Documentation](#contribute-documentation)
  * [Contribute Code](#contribute-code)
* Manage Something ✅🙆🏼💃👔
  * [Provide Support on Issues](#provide-support-on-issues)
  * [Label Issues](#label-issues)
  * [Clean Up Issues and PRs](#clean-up-issues-and-prs)
  * [Review Pull Requests](#review-pull-requests)
  * [Merge Pull Requests](#merge-pull-requests)
  * [Tag a Release](#tag-a-release)
  * [Join the Project Team](#join-the-project-team)
* Add a Guide Like This One [To My Project](#attribution)? 🤖😻👻

## Introduction

Thank you so much for your interest in contributing! All types of contributions are encouraged and valued. See the [table of contents](#toc) for different ways to help and details about how this project handles them!📝

Please make sure to read the relevant section before making your contribution! It will make it a lot easier for maintainers to make the most of it and smooth out the experience for all involved. 💚

## Request Support

If you have a question about this project, how to use it, or just need clarification about something:

* Open an Issue at https://github.com/akarshin/any-alias/issues
* Provide as much context as you can about what you're running into.
* Provide project and platform versions, depending on what seems relevant. If not, please be ready to provide that information if maintainers ask for it.

Once it's filed:

* Someone will try to have a response soon.
* Please avoid filing new issues as extensions of one you already made.

## Report an Error or Bug

If you run into an error or bug with the project:

* Open an Issue at https://github.com/akarshin/any-alias/issues
* Include *reproduction steps* that someone else can follow to recreate the bug or error on their own.
* Provide project and platform versions, depending on what seems relevant. If not, please be ready to provide that information if maintainers ask for it.

Once it's filed:

* A team member will try to reproduce the issue with your provided steps. If there are no repro steps or no obvious way to reproduce the issue, maintainers will ask you for those steps and mark the issue as `needs-clarification`. Bugs with the `needs-clarification` tag will not be addressed until they are reproduced.
* If maintainers are able to reproduce the issue, it will be marked `needs-fix`, as well as possibly other tags (such as `critical`), and the issue will be left to be [implemented by someone](#contribute-code).
* Please avoid filing new issues as extensions of one you already made.

## Request a Feature

If the project doesn't do something you need or want it to do:

* Open an Issue at https://github.com/akarshin/any-alias/issues
* Provide as much context as you can about what you're running into.
* Please try and be clear about why existing features and alternatives would not work for you.

Once it's filed:

* Maintainers will evaluate the feature request, possibly asking you more questions to understand its purpose and any relevant requirements. If the issue is closed, maintainers will convey their reasoning and suggest an alternative path forward.
* If the feature request is accepted, it will be marked for implementation with `feature-accepted`, which can then be done by either a maintainer or by anyone in the community who wants to [contribute code](#contribute-code).

Note: The team is unlikely to be able to accept every single feature request that is filed. Please understand if they need to say no.

## Project Setup

So you wanna contribute some code! That's great! This project uses GitHub Pull Requests to manage contributions, so [read up on how to fork a GitHub project and file a PR](https://guides.github.com/activities/forking) if you've never done it before.

If this seems like a lot or you aren't able to do all this setup, you might also be able to [edit the files directly](https://help.github.com/articles/editing-files-in-another-user-s-repository/) without having to do any of this setup. Yes, [even code](#contribute-code).

If you want to go the usual route and run the project locally, though:

* Install Python 3
* [Fork the project](https://guides.github.com/activities/forking/#fork)

Then in your terminal:
* `cd path/to/your/clone`
* `./install.sh`

And you should be ready to go!

## Contribute Documentation

Documentation is a super important, critical part of this project. Docs are how we keep track of what we're doing, how, and why. It's how we stay on the same page about our policies. And it's how we tell others everything they need in order to be able to use this project -- or contribute to it. So thank you in advance.

Documentation contributions of any size are welcome! Feel free to file a PR even if you're just rewording a sentence to be more clear, or fixing a spelling mistake!

To contribute documentation:

* [Set up the project](#project-setup).
* Edit or add any relevant documentation.
* Make sure your changes are formatted correctly and consistently with the rest of the documentation.
* Re-read what you wrote, and run a spellchecker on it to make sure you didn't miss anything.
* Write clear, concise commit message(s) using [conventional-changelog format](https://github.com/conventional-changelog/conventional-changelog-angular/blob/master/convention.md). Documentation commits should use `docs(<component>): <message>`.
* Go to https://github.com/akarshin/any-alias/pulls and open a new pull request with your changes.
* If your PR is connected to an open issue, add a line in your PR's description that says `Fixes: #123`, where `#123` is the number of the issue you're fixing.

Once you've filed the PR:

* One or more maintainers will use GitHub's review feature to review your PR.
* If the maintainer asks for any changes, edit your changes, push, and ask for another review.
* If the maintainer decides to pass on your PR, they will thank you for the contribution and explain why they won't be accepting the changes. That's ok! We still really appreciate you taking the time to do it, and we don't take that lightly. 💚
* If your PR gets accepted, it will be marked as such, and merged into the `latest` branch soon after. Your contribution will be distributed to the masses next time the maintainers [tag a release](#tag-a-release)

## Contribute Code

We like code commits a lot! They're super handy, and they keep the project going and doing the work it needs to do to be useful to others.

Code contributions of just about any size are acceptable!

The main difference between code contributions and documentation contributions is that contributing code requires inclusion of relevant tests for the code being added or changed. Contributions without accompanying tests will be held off until a test is added, unless the maintainers consider the specific tests to be either impossible, or way too much of a burden for such a contribution.

To contribute code:

* [Set up the project](#project-setup).
* Make any necessary changes to the source code.
* Include any [additional documentation](#contribute-documentation) the changes might need.
* Write tests that verify that your contribution works as expected.
* Write clear, concise commit message(s) using [conventional-changelog format](https://github.com/conventional-changelog/conventional-changelog-angular/blob/master/convention.md).
* Dependency updates, additions, or removals must be in individual commits, and the message must use the format: `<prefix>(deps): PKG@VERSION`, where `<prefix>` is any of the usual `conventional-changelog` prefixes, at your discretion.
* Go to https://github.com/akarshin/any-alias/pulls and open a new pull request with your changes.
* If your PR is connected to an open issue, add a line in your PR's description that says `Fixes: #123`, where `#123` is the number of the issue you're fixing.

Once you've filed the PR:

* One or more maintainers will use GitHub's review feature to review your PR.
* If the maintainer asks for any changes, edit your changes, push, and ask for another review. Additional tags (such as `needs-tests`) will be added depending on the review.
* If the maintainer decides to pass on your PR, they will thank you for the contribution and explain why they won't be accepting the changes. That's ok! We still really appreciate you taking the time to do it, and we don't take that lightly. 💚
* If your PR gets accepted, it will be marked as such, and merged into the `latest` branch soon after. Your contribution will be distributed to the masses next time the maintainers [tag a release](#tag-a-release)

## Review Pull Requests

While anyone can comment on a PR, add feedback, etc, PRs are only *approved* by maintainers.

PR reviews use [GitHub's own review feature](https://help.github.com/articles/about-pull-request-reviews/), which manages comments, approval, and review iteration.

Some notes:

* You may ask for minor changes ("nitpicks"), but consider whether they are really blockers to merging: try to err on the side of "approve, with comments".
* *ALL PULL REQUESTS* should be covered by a test: either by a previously-failing test, an existing test that covers the entire functionality of the submitted code, or new tests to verify any new/changed behavior. All tests must also pass and follow established conventions. Test coverage should not drop, unless the specific case is considered reasonable by maintainers.
* Please make sure you're familiar with the code or documentation being updated, unless it's a minor change (spellchecking, minor formatting, etc). You may @mention another project member who you think is better suited for the review, but still provide a non-approving review of your own.
* Be extra kind: people who submit code/doc contributions are putting themselves in a pretty vulnerable position, and have put time and care into what they've done (even if that's not obvious to you!) -- always respond with respect, be understanding, but don't feel like you need to sacrifice your standards for their sake, either. Just don't be a jerk about it?


