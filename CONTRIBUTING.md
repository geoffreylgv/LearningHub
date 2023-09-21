## Contributing

### Structure of the repository
In the repository, we have the principal README, and in every folder and sub-folder (if applicable), we should have a README describing the content of the folder.
In case the sub-folder has a sub-folder, follow the same structure by adding a README and so on so far, add a link for external resources if applicable, moreover, 
if you have multiple links, list them.  
Each README file follows the structure as follows:

!> Always use relative path when refering to a root file or folder.

`README.md`

| Project    | Description    |
| :--- | :--- |
|[Folder name](Folder name)|Code in the _forlder name_ are implemented to ...|

---

`Folder/README.md`

| File    | Description    | External resource |
| :--- | :--- | :--- |
|[Folder name or file name](Folder name or file name)| Brief description of the code or of the file | <ul> <li>[Link](url to external resource)</li> <li>[Link](url to external resource)</li> |

---

`Folder/Sub-folder/README.md`

| File    | Description    | External resource |
| :--- | :--- | :--- |
|[Sub-Folder name or file name](Sub-Folder name or file name)| Brief description of the code or of the file | [Link](url to external resource) |

?> The external resource is for a breve explanation or overview of the concept. Link a good resource of overview referring to the specific topic of resource we are adding **(note that it's optional)**
 
?> we should add a link containing an explanation on how to test efficaciously the simple shell or the learning material we've added.

?> Also we can add an external link to maybe a GitHub page that explains how to test it in this case.

?> Another thing, in the way the external link column is optional, we are not obliged to add it, we can leave it blank.

[**See the conversation here**](https://github.com/geoffreylgv/LearningHub/pull/13)

### How to contriute

#### If you don't have git on your machine, [ install it](https://docs.github.com/en/get-started/quickstart/set-up-git).

##### Fork this repository

Fork this repository by clicking on the fork button on the top of this page.
This will create a copy of this repository in your account.

#### Clone the repository

Now clone the forked repository to your machine. Go to your GitHub account, open the forked repository, click on the code button and then click the _copy to clipboard_ icon.

Open a terminal and run the following git command:

```
git clone "url you just copied"
```

where "url you just copied" (without the quotation marks) is the url to this repository (your fork of this project). See the previous steps to obtain the url.

For example:

```
git clone https://github.com/yourusername/LearningHub.git
```

where `yourusername` is your GitHub username. Here you're copying the contents of the LearningHub repository on GitHub to your computer.

#### Create a branch

Change to the repository directory on your computer (if you are not already there):

```
cd LearningHub
```

Now create a branch using the `git switch` command:

```
git switch -c your-new-branch-name
```

For example:

```
git switch -c add-custom-itoa-function
```

#### Make necessary changes and commit those changes

If you go to the project directory and execute the command `git status`, you'll see there are changes.

Add those changes to the branch you just created using the `git add` command:

```
git add _your file_ or git add . #for multiple files
```
Now commit those changes using the `git commit` command:

```
git commit -m "your relevant message that shows the change you have done"
```

#### Push changes to GitHub

Push your changes using the command `git push`:

```
git push -u origin your-branch-name
```

replacing `your-branch-name` with the name of the branch you created earlier.

#### Submit your changes for review

If you go to your repository on GitHub, you'll see a `Compare & pull request` button. Click on that button.  
Now submit the pull request.  
Soon I'll be merging all your changes into the main branch of this project. You will get a notification email once the changes have been merged.

### Where to go from here?

Congrats! You just completed the standard _fork -> clone -> edit -> pull request_ workflow that you'll often encounter as a contributor!

Celebrate your contribution and share it with your friends and followers on Twitter and tag the team.

### Adding resources
- If you added a new resource to an existing `resources.md` or `learning-material.md` file, just run `sort-resources.py` directly.
    
- If you added a new `resources.md` or `learning-material.md` file, add the path to the file to the RESOURCE_FILE_PATHS list below and then run `sort-resources.py`.

To run this script, open a terminal or command prompt and navigate to the directory that contains this script.

If you're using a Mac or a Linux distribution, you can run this script from the terminal by typing the following command: `python3 sort_resource_links.py`

If you're using Windows, you can run this script from the command prompt by typing the following command:
`python sort_resource_links.py`

Note 1: The links must be in the following format: `- [Link text](link URL)`. If you use a different format, the script will not work. 

Note 2: The heading for the sections must use a h4 heading (`####`). If you use a different heading, the script will not work.

Note 3: You must have Python 3 installed on your computer to run this script. If you don't have 
Python 3 installed, you can download it from https://www.python.org/downloads/. Make sure you 
download the version for your operating system (Windows, Mac, or Linux).

Note 4: This script assumes that it is at the root of the repository. If you move this script to 
a different location, you will need to update the RESOURCE_FILE_PATHS list below to include the 
correct paths to the resources.md and learning-material.md files.