# Git

### What is Git?

Git is often called version control software or source-control management software. More practically, Git is a tool that allows you to track granular changes to software (or any plain-text file) over time. This is incredibly useful for collaboration between multiple developers, identifying who made changes to software, reverting to a previous version, etc.

The use cases for Git can go on and on. Git has quickly become the most popular version control software by far and is widely used across the industry. As a result, it is useful when writing small projects by yourself or when working in large teams, and knowledge of this tool is becoming a more and more important prerequisite for many jobs/opportunities.

### Git Providers

Git stores code in what it called a repository. Every Git repository is equal and can be used to clone and push code to; however, there are many cases why choosing a 3rd party provider to host your repository is a good idea. Some of the advantages are:

- Remote code storage and backup
- Built-in devops and collaboration features
- Almost always available whenever needed

Some common providers for these services are Github, Gitlab, and Bitbucket. We'll focus on Github in this workshop, however the functionality of all of the providers is generally similar. Before beginning the rest of this workshop, you should make a free Github account. When choosing your Github username, please choose something that you will be will to use for a long time (I.e. don't use your student ID as your username and instead choose something that is unique and recognizable/easy to share for collaboration purposes).

Students can gain some paid features for free via the Github Education Pack:

[GitHub Student Developer Pack](https://education.github.com/pack)

### Initializing a Git Repository

There are 2 ways that you can initialize a git repository, locally first or remote first. We'll cover both below:

1. **Local**

In git, every repository is considered a full fledged repository and there is no real distinction between a parent repository and a clone. As such, when you create a repository locally on your machine, it is just as capable as a repository created on a remote service.

To create a local repository, first create a folder with the desired project name. They do not have to always match, but it makes sense to do so initially. Move into that folder and run the following command:

```shell
git init
```

This will create a .git folder in your current project which will allow you to start tracking changes and making commits. The folder that you run the `git init` command in does not need to be empty when running the command, though it is discouraged to run the command within another git repository. At this point, you have a fully functional git repository.

2. **Remote**

Creating a remote repository allows for backing up code and collaboration through a centralized, remote repository. We'll be using Github for this tutorial, but the process for getting started is fairly similar across similar providers. To begin, you will need a Github account. Create one now.

Once you are logged in, go to the main homepage of Github and you should see a green "New" button on the left side of the page. Click that and you will be brought to the repository creation page.

Once on the repo creation page, create a name for your project. This can be changed later, but be sure to not include spaces and remember that it will be needed to clone the repository (so shorter is often better). You can then enter an optional description (which will briefly describe your project). Some other important options you can select include:

- Public vs Private - private repos are only viewable by their creator and those who they invite. Public repositories can be viewed/cloned/forked by anyone. Note: neither public nor private repos can be modified by anyone.
- License (optional) - choose a license for how the code in your repository can be used. If you are unsure, do not include a license. It can be added later.
- .gitignore (optional) - This will be covered later, but if you know your repository is going to be written in a certain language, you can choose that language from the dropdown.
- ReadMe (optional) - Adding a readme is always a good idea, and is used by Github and new users to understand how to get started with your project.

Once you have selected your desired configuration, select the create repository button. This will create your new repository at: https://github.com/[github-username]/[repository-name]

3. **Linking a Local Repository to a Remote Repository**

The final way you can create a repository is a hybrid approach of the two. You can start with a local repository and then set an externally hosted repository as the remote. As a general rule of thumb, if you have no existing code for a project, create a remote repo first and clone it and begin working from there. If you have existing code you need to add to a repository, create a repository locally and then add a remote like we will be doing here.

To add a remote repo, first create the remote like we did previously, but leave out all of the optional files such as a License, ReadMe, and .gitignore. This will create a blank repo for you to push your existing repository's files to.

Once you have the URL for your new remote repository, run the following code (but be sure to change the `[github-username]`  to your username and the `[repository-name]`  to the name of the remote repository you just created.

```shell
git remote add origin git@github.com:[github-username]/[repository-name].git
git branch -M main
git push -u origin main
```

### Cloning a Repository

Since you will most likely be working via a remote repository for most projects, you will need a cloned copy of the repository to operate out of (make changes to). This repository isn't lesser than the original (though you can clone an incomplete history of a repository instead of the full repository; but, that is for another workshop on more advanced topics). This will typically be a bit-for-bit copy of the original. To clone a repository, you first need to decide on a protocol to use. The primary protocols for cloning a repository is either via `SSH` or via `HTTPS`. Choosing one over the other has a few practical differences. Lets take a look at what makes them unique:

- SSH
   - Uses the `.ssh/config` system configuration for all `ssh` connections.
   - Allows for key-based authentication of your Github or Gitlab user.
   - Changes the repo url format to look something like this:

```shell
git@github.com:[username]/[repository-name]
```

- HTTPS
   - Typically easier to use when cloning a repository that you will not need to make changes to.
   - Easy to simply copy the Github or Gitlab URL for a repository and it *just works.*
   - Changes the repo url format to look something like this:

```shell
https://github.com/[username]/[repository-name]
```

If you are downloading a repository that you own/can make changes to, then I highly recommend using the SSH protocol. Otherwise HTTPS is fine.

To configure `ssh` access on Github, use the following guide:

[About SSH - GitHub Docs](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/about-ssh)

To configure `ssh` access on Gitlab, use the following guide:

[Use SSH keys to communicate with GitLab | GitLab](https://docs.gitlab.com/ee/user/ssh.html)

----

To clone a repository now that you have your access setup, the command is fairly simple. Simply take the URL (in HTTPS or SSH format) and run the following command:

```shell
git clone [URL] [destination-directory]
```

Where `[URL]` is replaced with your URL, and `[destination-directory]` is an **optional** custom name/location for your repository folder. This isn't required, but if you have a large project name such as `mpi-benchmarking-testing-scripts-fork1`, it might be easier to use the file name `mpi-testing-scripts` to simplify your workflow.

### Git Remotes

As you have probably gathered from other parts of this workshop, remote's are a repository's upstream copy where changes are pushed to. You can have multiple remotes for a repo and you can change them at any time. All we will say for this beginner introduction to Git is how to view the remotes of a repository. If you have more than one copy with multiple remotes, it is nice to make sure you know where you are pulling from.

To view the remotes for a repository, run the following command:

```shell
git remote -v
```

Doing so will show the name of the remote (for both pushing and fetching) as well as the corresponding URL.

### Adding Files

Now that you have a good understanding of how to create git repositories, its important to know how to use them. Git has 2 distinct views of a file: tracked and untracked. An untracked file means that any changes to the file will not be recorded by Git, whereas a tracked file will. To begin tracking a file, you will need to first add it to the repository. To add a specific file, run the following command within the repository:

```shell
git add [relative/path/to/file]
```

The file will now be tracked and it will be listed as being ready for commit when you run the following command:

```shell
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	new file:   Hello_World_Added.txt

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	Hello_World.txt
```

Git status is an important command for viewing the current state of your repository. As you can see above, it is able to list files which have been added (ready to be committed to the history of the repository) and those which are not.

We'll talk more about commits later, but what is important right now is understanding that commits are the recorded history of a git repository. If you make a commit at any point in time, **all** files that are listed in the "Changes to be committed" category will be recorded to the history. This allows you to commit only a single file at a time or to include a larger, project-wide change in a single commit.

Another useful command is the shortcut for adding all files in a repository or subdirectory. Git behaves in such a way that, if there is a directory with numerous files changed in your repository, you can simply add the parent directory and all changed files will be recursively added. To add every file in the repository that has a change (even across multiple directories) you can use the following command:

```shell
# adds every changed file in a repository
git add -A
```

One more important note is that, after each commit to a repository, a file will need to be re-added before any new changes can be committed again.

### Committing Changes

After you have added a file, you need to commit it to the history of the repository before you can push it up or eventually revert back to that change. This is a vital step as many changes can be lost if files are improperly committed. Fortunately, its not hard to commit changes to your repository after you've added the correct files. To do this, simply run the following command:

```shell
git commit
```

Once you run this command, you will be presented with a text editor (usually vi/vim by default) where you can write a short message describing the change that will be committed to the repository. Be sure to keep this message short and succinct. You'll also notice that the editor has some text already present in your commit. These are comments. Like bash, python, etc. Git uses the `#` sign as a comment symbol, and all text on the same line following the pound symbol will be omitted from the message.

Another important shortcut is the following command:

```shell
git commit -m "Change Message Hear"
```

In the above command, you can quickly commit files without having to open an editor. The `-m` allows you to pass in a string (surrounded by quotes) into the commit message ahead of time!

Thats great and all, but oh no! Would you look at that, in our rush to commit our changes, we made a typo and used the wrong spelling for "Here". Fortunately, there is a quick way to correct this. If you run the following command, you can amend changes in the last commit:

```shell
git commit --amend
```

You can combine the `--amend` flag with other flags as well such as the `-m` . It does not need to be run as a standalone command.

### Pushing and Pulling Changes

Once you've committed your changes, you can push them to a remote if you are using one. Typically, this is as simple as running:

```shell
git push
```

If everything goes as expected, you will see some information on the changes being transferred and it will succeed. But this isn't always the case. Frequently, your changes will be refused due to changes existing on the remote that are not yet on your local copy of the repository. This is particularly common when working on a project collaboratively. To correct this, you will need to run a pull command to get the latest changes:

```shell
git pull
```

You can run a `git pull` at any time, however if you have made commits before you pull, you will need to merge the two sets of changes together. This is typically easy, but if two commits touch the same code, you may need to manually resolve any conflicts that occur. We will discuss merging in the next section. Once your merge is complete, you can re-run `git push` to push your changes to the default remote repository. Alternatively, you can push and pull from a specific remote via the following commands:

```shell
# pull from specific remote
git pull [remote_name]

# push to specific remote 
git push [remote_name]
```

### Merges

Git makes merging changes between two versions of a repository very simple. It does a pretty good job of resolving things on its own. For example, in the previous section of this workshop, we discussed the possibility of pulling changes that contained a commit that was more recent than your commits that you were trying to push to a remote repo. In this case, the act of pulling those changes kicks off a merge automatically. If the merge is easy (i.e. no overlapping changes in overlapping files), you will be allowed to edit the commit message for the merge and then it will *just happen.* This is cool, but its also optimistic. Not all merges can be easily resolved by Git, so we'll cover how to resolve a conflicted merge in a moment.

First though, we need to discuss the merge command. Its fairly simple, but it requires a concept we have not covered yet: branches. For now, think of a branch as a version of a repository that is slightly diverged from the original, and you're trying to bring those diverged changes back into the main branch. To move something from a branch into your current branch, you simply need to run:

```shell
git merge [branch_name]
```

This will merge changes from the matching [branch_name] branch into the branch you are currently on (this defaults to `main` or `master` depending on which version of git you are using).

Now that we've covered how to invoke a merge manually or automatically, we can discuss what happens when a merge goes wrong. Say for example, two people have changed the same file (in this case) `Hello_World_Added.txt`. When the second modification is pushed and subsequently refused, a merge will occur when the developer pulls in their changes. If there is a conflict that Git cannot resolve, it will look like this:

```shell
$ git pull
remote: Enumerating objects: 5, done.
remote: Counting objects: 100% (5/5), done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 1), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (3/3), 672 bytes | 336.00 KiB/s, done.
From github.com:carsonwoods/utc-workshops
   239d460..a3ebff0  main       -> origin/main
Auto-merging Hello_World_Added.txt
CONFLICT (content): Merge conflict in Hello_World_Added.txt
Automatic merge failed; fix conflicts and then commit the result.
```

As we can see, Git *tried* to fix the issue for us, but was unable to do so. So now its our turn. Lets run `git status` and see what is going on.

```shell
$ git status
On branch main
Your branch and 'origin/main' have diverged,
and have 1 and 1 different commits each, respectively.
  (use "git pull" to merge the remote branch into yours)

You have unmerged paths.
  (fix conflicts and run "git commit")
  (use "git merge --abort" to abort the merge)

Unmerged paths:
  (use "git add <file>..." to mark resolution)
	both modified:   Hello_World_Added.txt

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	Hello_World.txt

no changes added to commit (use "git add" and/or "git commit -a")
```

Ok, great. We now have an idea of what needs to be fixed and what we can do to fix it. The files listed under `Unmerged Paths:` are the files that were unable to be merged. Before we show you how to fix the conflict, first take a look at the following line from the status page:

```shell
(use "git merge --abort" to abort the merge)
```

If you decide that the merge is not what you wanted to do, then running that command will revert your changes back to your latest local commit. If you want to proceed with the merge keep, lets fix that conflict. Upon opening the conflicted file, we see the following:

```shell
<<<<<<< HEAD
  Hello and Goodbye World Added
  =======
  Hello New World with changes added.
  >>>>>>> a3ebff02098cab22f7d3d92434e40b4ebd0e407a
```

This is a pretty short file, but we can immediately see that two people tried to modify the same line with different contents. The two versions of the code are separated by a line of `=` and it is lead/tailed by `<` and `>` respectively. To fix this, you need to first identify the version of code that you want to keep. This can be the `Hello and Goodbye World Added` or the `Hello New World with changes added.`. Alternatively, you can completely rewrite the line and put whatever line you want there. Before we decide, lets look closer. The top option is listed as `HEAD` , this means it is the HEAD of your current repository's commit history (aka **your** version of the code). The section that is marked via `a3ebff02098cab22f7d3d92434e40b4ebd0e407a` is a hash representing the remote commit (aka **their** version of the code).

Maybe we were a bit hasty with our choice and we decide the other person's code is correct. To fix this, we would simply remove everything that we don't want in the file so that it looks like this:

```shell
Hello New World with changes added.
```

We can then exit our editor after saving changes and then add the file like normal. Once there, we simply need to run `git commit` to complete the merge. Then you can push your changes and the remote will have the resolved merge.

### Branching

Git branches are another core feature of Git. Git is known for being able to revert a project back to any point in its commit history. This is useful, however there are other applications of this feature. The primary one is git branches. For example, when fixing a bug or adding a new feature, code will often break/become worse before it gets better. Instead of risking your code in your `main` branch, we can create a new branch which is separate from the original. That way, changes can be made in isolation, and merged back into the main branch whenever it is production ready. To create a new branch from your current branch and switch to it, use the following commands:

```shell
# create a new branch from your current branch
git branch [new_branch_name]

# move to the new branch
git checkout [new_branch_name]

# or replace both above commands with a single shorthand version
git checkout -b [new_branch_name]
```

Once you are in a new branch, you can make changes without concern about damaging an existing code base. To view all the branches on a repository, you can use the following command:

```shell
# view branches
git branch

# view branches with brief history
git branch -v
```

Once you find a branch you want to switch to, simply run

```shell
git checkout [branch_name]
```

Checkouts will be covered in more detail next, but for now you can think of them as a way to switch between branches. Ok, now lets say you've created a new branch and you're ready to push the changes inside it to a remote repository for backup/storage. Running `git push` while on a new branch will result in an error:

```shell
$ git checkout -b new_branch
$ git push
fatal: The current branch new_branch has no upstream branch.
To push the current branch and set the remote as upstream, use

    git push --set-upstream origin new_branch

To have this happen automatically for branches without a tracking
upstream, see 'push.autoSetupRemote' in 'git help config'.
```

You need to run the specified `git push --set-upstream origin new_branch` first to make the remote repository aware of the new branch. You can replace `origin` with any remote name and you should set `new_branch` to be whatever your branch's name is. After this is done once, you can push and pull like normal.

### Checkouts

We've already covered most of the basics of checkouts in the previous section, however there is one more aspect that is important to know about. You can checkout an individual commit. You've probably noticed that for each commit of a repository, you get an associate hash value that represents that commit. You can target a hash as a checkout target to get the code at that commit's point in time. For example, lets run the following command:

```shell
$ git log
commit e7ebd3c8256c562c7263a1e626bf8298eb1e224a (HEAD -> new_branch, main)
Author: Carson Woods <cwoods289@gmail.com>
Date:   Thu Sep 15 11:00:18 2022 -0400

    Minor changes to text file

commit 239d460a595ff388e915004db6f2398e18aa15c6
Author: Carson Woods <cwoods289@gmail.com>
Date:   Thu Sep 15 10:59:14 2022 -0400

    Add new file

commit ad90fc9ce086ef251a18a6f96d01cf375c96b6e7
Author: Carson Woods <carsonwoods@users.noreply.github.com>
Date:   Fri Sep 9 09:59:30 2022 -0400

    Initial commit
```

Running `git log` give you the full history of the repo for a current branch. It also provides the hash for each commit as it occurred. Lets say we wanted to return to the `Initial Commit` change.  To do that, we would simply run:

```shell
$ git checkout ad90fc9ce086ef251a18a6f96d01cf375c96b6e7
Note: switching to 'ad90fc9ce086ef251a18a6f96d01cf375c96b6e7'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by switching back to a branch.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -c with the switch command. Example:

  git switch -c <new-branch-name>

Or undo this operation with:

  git switch -

Turn off this advice by setting config variable advice.detachedHead to false
```

You are now in a copy of the code that is at the state you requested. There are other things that can be done with checkouts, but that can be left for you to explore as you need it.

