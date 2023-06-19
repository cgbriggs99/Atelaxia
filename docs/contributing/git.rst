Using Git to Contribute
=======================

When contributing to this project, we recommend following these steps. These are only a recommendation. If you have a workflow that you are familiar with and you know works, then you are welcome to use it. These steps will be elaborated in the following sections.

1. Fork the repository. This should only be done once.
2. Clone the repository. This should only be done once.
3. Create a remote branch.
4. Create a local branch.
5. Add a commit.
6. Create a pull request.
7. Update your branch.
8. Wait for merge.

Fork the repository
-------------------

This step is the easiest. Use the GitHub webpage and select the "fork" button in the upper right. This separates your code from the production code, so if something goes wrong on your end, it doesn't destroy the project.

Clone the repository
--------------------

After forking the repository, your fork should be cloned to your local machine. If using the command line, the following command can be used.

.. code::

   git clone [copy-paste from GitHub clone button]

On your fork's "code" page, there should be a green button that reads "<> Code". This can be used to generate a URI for the ``git clone`` command. If you are not using the command line, read the documentation for your preferred Git manager.

Create a Remote Branch
----------------------

After forking the repository, you should create a branch for your code. To do this, select the "branches" menu from the GitHub webpage. Then, in the search bar that shows up, type the name for your new branch. When prompted, select the version of the repository to use as a base. It is recommended that you use the active development branch if you don't know which to choose.


Create a Local Branch
---------------------

Using the command line or your favorite GitHub manager, create a branch on your local machine to mirror the remote branch. On command line, the following commands can be used.

.. code::

   # Create the branch and switch to that branch.
   git branch -m [branch name]

   # Set the  branch to mirror the remote version of the branch.
   git branch --set-upstream-to=[remote branch name] [local branch name]

After setting the upstream branch, pull the contents into the local.

.. code::

   # Get the contents of the remote branches.
   git pull

Create a Commit
---------------

Now you can finally start doing stuff. Make the changes you need. Then add the files you changed to the index. On command line, this can be done using the following command.

.. code::

   git add [list of files that you want to add]

However, if you simply want to add all files changed so far, except those excluded by ``.gitignore``, you may use the following command.

.. code::

   git add .

To check which files have been added, use the following commands.

.. code::

   git status

If you want undo adding a file to the commit you are building, you may use the following command.

.. code::

   # Remove the file from the commit, but don't delete the file.
   git rm --cached [file or files to removed]

   # Remove the file from the commit and from your hard drive.
   git rm [file or files to be removed]

If you want to force removal, use the ``-f`` option. If you want to remove all files in a directory, then delete the directory, use the ``-r`` option. If you want to remove both, use the ``-rf`` option. These options are placed between the "rm" and the first file to be removed.

After your commit has been set up using ``git add``, you can finally commit. To do this, use the ``git commit`` command. This will give you a prompt asking for a commit message. Write something descriptive, but keep it to one sentence max. A commit message like "commit" or "made changes" is not descriptive. However, your commit will not be denied based on this as long as you can describe at least briefly what was changed when you go to finish your pull request. After your code is committed, it needs to be uploaded to GitHub. This can be done by simply using the ``git push`` command.

Create a Pull Request
---------------------

Once you have made at least one commit to your branch, you may start a pull request. To do this, there will be a prompt on your fork's GitHub page. This will allow you to choose a branch to merge from and a branch to merge into. It is suggested that you make the pull request from your branch into the active development branch. Then, you will be taken to a page that asks for a description as well as some other options. We ask that you write a short description of what was done, and give the pull request a descriptive title. If you feel so inclined, you may add extras, like tags and labels, but this is optional. You may also link issues to your pull request. If you are not done with your pull request, it will update as you push commits to your branch.

Updating Your Branch
--------------------

As changes are made to the base project, your branch will drift from the parts it is based on. If you wish to update parts of your branch that you are not actively changing, you may make a pull request from the base branch to your branch. When the pull request is merged, it will update your branch. If there are merge conflicts, you should try to fix it yourself to learn how to do it, but we on the Discord will also happily help you or do it for you.

Wait for Merge
--------------

So you've finished your code. Your pull request is all done, and it is based on the most up-to-date code base. Now all you have to do is wait for it to be merged. Once you finish your pull request, message one of the repository managers for a review. If we find issues, we will point those out. We may also offer fixes for these. If we don't we will tell you. Once your pull request has enough sign-offs, it will become part of the official code base. Congratulations! After the pull request has been merged, you may delete your branch safely. You will also be offered a place in the "contributors" section in the build and in the repo.
