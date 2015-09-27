---
title: "Fork/Clone/Modify/Add/Commit/Push"
published: true
morea_id: fork_clone_modify_add_commit_push_experience
morea_type: experience
morea_summary: "No turning back now"
morea_sort_order: 1
morea_labels:
 - 1 hr
 - 1 pt
 - closed
---

### Fork/Clone/Modify/Add/Commit/Push

Today is the day you come of age as a programmer. I'm so proud of you already.

- First, 'fork' your own copy of that 'vim_lessons' repository *in GitHub*. After you do that, you'll be able to see the code on your own GitHub page.

- Next, clone it to your local machine. Then fix the vandalized Walt Whitman poem.

- After that, use git to 'commit' the new version of the file you fixed. This is like taking a snapshot of the file, just in case a clever hacker ruins it again. This is a two step process:
  - `git add poetry/walt_whitman` will "stage" the file, i.e. make it part of the upcoming snapshot.
  - `git commit -m "fixed poem"` will take the snapshot. You can write anything you want in the quotes, but keep it relevant.

- Once you've committed, use git to 'push' your updated repository back up to GitHub. After that, you'll be able to see the *updated* code on your GitHub page.
  - `git push -u origin master` should do the trick.

There's no need to email me anything; on Friday, September 4th at midnight I'll just check GitHub to make sure you did the assignment.

Please use the command line to do this entire assignment. Please email me if you get stuck and Google can't help. Here's a [screencast](https://www.youtube.com/watch?v=G_8N4nIh7cU) of me doing the entire assignment. It is officially the most boring video on all of YouTube. Have fun!
