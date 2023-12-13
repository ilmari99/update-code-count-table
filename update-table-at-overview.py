""" 
For each repo in the current directory, pull the latest changes from main or master branches
"""

import os
import json
import datetime
from github import Github

env_file = json.load(open('__private_env.json'))

UNAME = env_file['username']
TOKEN = env_file['token']
EXCLUDE_FILES = env_file['exclude_from_table']

DO_UPDATE = False


gh = Github(TOKEN)

if DO_UPDATE:
    # Find all my repos, and clone them as "__<repo_name>__"
    repos = [repo for repo in gh.get_user().get_repos()]
    print(f"Found repos:")
    for repo in repos:
        print(f"    {repo}")

    repos_hidden_names = [repo.name + "__" for repo in repos]

    # Go through each repo, and
    #1. Check if it's already cloned
    #2. If not, clone it
    #3. If yes, pull
    for repo_local_name, repo in zip(repos_hidden_names, repos):
        if repo_local_name not in os.listdir():
            # Clone the repo
            repo_address = repo.clone_url
            print(f"Cloning from {repo_address}")
            os.system(f"git clone {repo_address} {repo_local_name}")
        else:
            os.chdir(repo_local_name)
            os.system("git pull")
            print(f"Pulled {repo}")
            os.chdir("..")


input(f"Please count the lines of code using VSCode, and then press Enter to continue...")

EXCLUDE_FILES = ["CSV", "Excel", "JSON", "XML", "CSS", "YAML", "pip requirements", "Ini", "Groovy", "Diff", "TSV", "Properties", "Markdown"]
# Go to folder ".VSCodeCounter", and find the folder with the latest changes (timestamp)
# and parse it by removing the counts of the excluded files

# Find the latest folder
os.chdir(".VSCodeCounter")
folders = os.listdir()
# Find the folder with the latest timestamp
latest_folder = max(folders, key=os.path.getctime)
print(f"Found latest folder: {latest_folder}")
# Now go the folder and remove lines starting with "| <filetype>" where filetype is in EXCLUDE_FILES
os.chdir(latest_folder)
# Read the file
with open("results.md", "r") as f:
    lines = f.readlines()
# Remove lines
lines = [line for line in lines if not any([exclude in line for exclude in EXCLUDE_FILES])]
# Write the file
with open("results.md", "w") as f:
    f.writelines(lines)

print(lines)
# Take the text between "## Languages" and the next "##"
start_idx = lines.index("## Languages\n")
# Find the next "##"
end_idx = start_idx + 1
while "##" not in lines[end_idx]:
    end_idx += 1
code_count_table = lines[start_idx + 1:end_idx]
# On each line, find the last enclosed | <> | (if it exists) and put |**<>**| instead
for i, line in enumerate(code_count_table):
    if i <= 1:
        continue
    if line.count("|") > 1:
        # Find the last enclosed | <> |
        last_idx = line.rfind("|") - 1
        first_idx = line[:last_idx].rfind("|") + 1
        #print(f"Converting {line} to {line[:first_idx]} **{line[first_idx + 1:last_idx]}** {line[last_idx + 1:]}")
        code_count_table[i] = line[:first_idx] + " **" + line[first_idx + 1:last_idx] + "** " + line[last_idx + 1:]

code_count_table = "".join(code_count_table)

print(f"Updated code count table: {code_count_table}")

# Finally, update the overview page by going to folder with your username, and updating its README.md file
os.chdir("..")
os.chdir("..")
print(f"Changed directory to {os.getcwd()}")
os.chdir(UNAME + "__")
print(f"Changed directory to {os.getcwd()}")
# Read the file
with open("README.md", "r") as f:
    lines = f.readlines()
# Find the line with the code count table
start_idx = 0
while not lines[start_idx].startswith("### Lines of code"):
    start_idx += 1
end_idx = start_idx + 1
while "##" not in lines[end_idx]:
    end_idx += 1
# Replace the code count table
lines[start_idx + 1:end_idx] = code_count_table
# Update the first line to read "(Updated on <date>)"
lines[start_idx] = f"### Lines of code in my GitHub repositories (updated on {datetime.datetime.now().strftime('%d %B %Y')})\n"
print(lines[start_idx:end_idx])

# Write the file
with open("README.md", "w") as f:
    f.writelines(lines)

print(f"Pushing changes to {UNAME}__")
# Show repo upstream
os.system("git remote -v")
os.system("git remote update")
os.system("git fetch")
os.system("git status")
# Finally, push the changes
os.system("git add README.md")
os.system("git commit -m \"Automatic update of code count table\"")
os.system("git pull")
os.system("git push")
os.chdir("..")
