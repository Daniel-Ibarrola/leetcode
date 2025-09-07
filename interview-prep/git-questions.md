# Git Questions

### 1. What is the difference between `git pull` and `git fetch`?

Both commands are used to download new data from a remote repository, but they differ in what they do with that new data.

*   **`git fetch`**: This is the "safe" option. It downloads all the new commits, files, and branches from the remote repository into your local repository, updating your remote-tracking branches (like `origin/main`). However, it **does not** automatically integrate any of this new data into your local working branches. This gives you a chance to review the changes before deciding to merge them.

*   **`git pull`**: This command is more aggressive. It is essentially a `git fetch` followed immediately by a `git merge` (or `git rebase`, depending on your configuration). It downloads the new changes from the remote *and* tries to merge them into your current local branch.

**Analogy:**
*   `git fetch` is like getting a letter in the mail. You have the new information, but it's separate from your current work. You can read it whenever you want.
*   `git pull` is like getting the letter and immediately writing its contents into the document you are currently working on.

**When to use which:**
*   Use `git fetch` when you want to see what others have been working on without having to merge it into your local branch just yet.
*   Use `git pull` when you are ready to update your local branch with the latest changes from the remote.

---

### 2. What is `git rebase` and how does it differ from `git merge`?

Both `git rebase` and `git merge` are designed to solve the same problem: integrating changes from one branch into another. However, they do it in very different ways, which results in a different project history.

#### `git merge`
When you merge a feature branch into `main`, `git merge` takes the histories of both branches and ties them together. It creates a new, special commit (a "merge commit") that has two parent commits. This preserves the historical context of the feature branch exactly as it happened.

*   **Resulting History:** A graph-like structure showing where branches diverged and were merged back in. It's a truthful but potentially messy history.
*   **Pros:** Non-destructive. It doesn't change existing commits.
*   **Cons:** Can create a cluttered commit history with lots of merge commits.

#### `git rebase`
Rebasing solves the same problem differently. Instead of creating a merge commit, `git rebase` takes all the commits from your feature branch, temporarily saves them, and then reapplies them one by one on top of the latest commit of the `main` branch.

*   **Resulting History:** A clean, linear history. It looks like you developed your feature sequentially right after the latest work on `main`.
*   **Pros:** Creates a simple, easy-to-read commit history.
*   **Cons:** It **rewrites commit history** (the commits get new hashes).

**The Golden Rule of Rebasing:**
**Never rebase a branch that has been pushed to a public or shared repository.** Because rebasing rewrites history, it can create massive confusion for collaborators who have based their work on the original commits. It's best used only on your local, private branches.

---

### 3. How do you resolve a merge conflict?

A merge conflict occurs when Git is unable to automatically merge changes because two different branches have modified the same lines in the same file. Git will stop the merge process and ask you to resolve the conflict manually.

Here is the step-by-step process:

1.  **Identify the Conflict:** Git will tell you which files have conflicts. You can also run `git status` to see a list of "unmerged paths."

2.  **Open the Conflicting File:** Inside the file, you'll see conflict markers added by Git:
    *   `<<<<<<< HEAD`: This marks the beginning of the conflicting lines from your current branch (the "HEAD").
    *   `=======`: This separates your changes from the changes in the other branch.
    *   `>>>>>>> [other-branch-name]`: This marks the end of the conflicting lines from the other branch.

3.  **Edit the File:** Your job is to decide what the code should look like. You might keep your version, their version, or a combination of both. **You must also delete all the conflict markers** (`<<<`, `===`, `>>>`).

4.  **Stage the Resolved File:** After you have manually edited the file and are satisfied with the result, tell Git that you've resolved the conflict by staging the file:
```shell script
git add <path/to/the/resolved/file.txt>
```


5.  **Commit the Merge:** Once you have resolved and staged all conflicting files, commit the changes to finalize the merge. Git will usually provide a default commit message.
```shell script
git commit
```


---

### 4. What is `git cherry-pick`?

`git cherry-pick` is a command that allows you to select a specific commit from one branch and apply it onto another branch.

Instead of merging an entire branch with all its commits, `cherry-pick` lets you pick out a single commit you're interested in and apply its changes to your current branch. Git creates a **new commit** on your current branch that contains the exact same changes as the commit you picked.

**Common Use Cases:**
*   **Fixing a Bug:** A bug fix is committed to a feature branch, but you need that fix *now* in your `main` or `release` branch without merging the entire unfinished feature.
*   **Copying a Small Feature:** You implemented a small, useful feature in one branch and want to quickly duplicate it in another without a formal merge.

**Usage:**
```shell script
# First, switch to the branch where you want to apply the commit
git switch main

# Then, cherry-pick the specific commit by its hash
git cherry-pick <commit-hash>
```


---

### 5. What is the difference between `git reset` and `git revert`?

Both commands undo changes in your repository, but they are fundamentally different in their approach.

#### `git reset`
`git reset` is a **history-rewriting** command. It moves the current branch pointer back to a previous commit, effectively making it look like the subsequent commits never happened.

It has three common modes:
*   `--soft`: Moves the branch pointer. The changes from the "undone" commits are kept in your staging area.
*   `--mixed` (default): Moves the branch pointer and unstages the changes, leaving them in your working directory.
*   `--hard`: Moves the branch pointer and **discards all changes** completely. This is a dangerous, destructive operation.

Because it alters history, `git reset` should **only be used on local, private branches.**

#### `git revert`
`git revert` is a **history-preserving** command. It undoes the changes from a previous commit by creating a **brand new commit** that does the inverse. For example, if the old commit added a line of code, the revert commit will remove that line.

The original commit remains in the project's history, and a new "revert" commit is added. This is a safe, non-destructive way to undo changes.

**When to use which:**
*   Use `git revert` to undo changes on a **public, shared branch** because it doesn't change the project history that others may be relying on.
*   Use `git reset` to undo changes on a **local, private branch** when you are still cleaning up your work and haven't shared it yet.