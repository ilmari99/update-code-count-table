# Automatic code line table generator with VSCode
This script fetches all your GitHub repositories, and pushes the latest code line counts to your GitHub overview repo, i.e. the repo named as your username.

All you need is this VSCode extension: [Code counter](https://github.com/uctakeoff/vscode-counter), and a GitHub token with `repo` scope.

Also, somewhere in your README.md, you need to have the following line to tell the script where to put the table:
```markdown
### Lines of code
```

## How to use
1. Clone this repo `git clone https://github.com/ilmari99/update-code-count-table.git`
2. `cd update-code-count-table`
3. Install the VSCode extension: search for `VS Code Counter` in the extensions tab, and select the first one
4. Create a GitHub token with `repo` scope: [Creating a GitHub Personal Access Tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-fine-grained-personal-access-token)
5. Copy and modify the example enviornment json: `cp example_env.json __private_env.json` and update the `__private_env.json` with your GitHub username, the token, and optional exclusions from the code table.
6. Run the script `python update_code_count_table.py`. The script will stop, and ask you to code the lines of code. Right-click on your file explorer in VS Code, and select `Count lines in directory`. When the counting is done, press Enter to continue the script, and push the changes to your GitHub overview repo.



## Example:
### Lines of code in my GitHub repositories (updated on 07 August 2024)
| language | files | code | comment | blank | total |
| :--- | ---: | ---: | ---: | ---: | ---: |
| Python | 467 | 46,775 | 5,847 | 8,461 | **61,083** |
| Java | 72 | 8,854 | 566 | 1,799 | **11,219** |
| MATLAB | 44 | 3,501 | 1,009 | 991 | **5,501** |
| C | 29 | 2,506 | 790 | 485 | **3,781** |
| JavaScript | 14 | 2,369 | 341 | 451 | **3,161** |
| SQL | 5 | 2,078 | 5 | 54 | **2,137** |
| Shell Script | 29 | 798 | 308 | 311 | **1,417** |
| HTML | 18 | 677 | 43 | 135 | **855** |
| C++ | 11 | 351 | 371 | 187 | **909** |
| Batch | 5 | 193 | 60 | 102 | **355** |
| LaTeX | 3 | 140 | 0 | 44 | **184** |
| CUDA C++ | 1 | 100 | 42 | 35 | **177** |
| Assembly | 2 | 75 | 0 | 2 | **77** |
| Makefile | 6 | 61 | 1 | 26 | **88** |