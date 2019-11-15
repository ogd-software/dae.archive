import git
from functools import reduce

repo = git.Repo("/home/jbg/Development/dae.archive")
#commits = list(repo.iter_commits("master", max_count=5)))
commits = list(repo.iter_commits("master"))

def is_exists(filename, sha):
    """Check if a file in current commit exist."""
    files = repo.git.show("--pretty=", "--name-only", sha)
    if filename in files:
        return True

def get_file_commits(filename):
    file_commits = []
    for commit in commits:
        if is_exists(filename, commit.hexsha):
            file_commits.append(commit)

    return file_commits

file_commits = get_file_commits('README.md')

#print(file_commits)
a = []
for commit in commits:
    a.append(commit.message.strip())

print(a)
