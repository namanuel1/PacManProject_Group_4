Ebony was responsible for completing Step 1, forking the repository, setting up collaborators, and configuring remotes. Ebony also used `grep` and `sed` commands to rename instances of player to pacman throughout the project:
# Find and replace all instances of 'player' in files
grep -rnw '.' -e 'player'

find . -type f -name "*.py" -exec sed -i 's/player/pacman/g' {} +

# Double-check replacement in files
sed -i 's/player/pacman/g' pacman.py

sed -i 's/player/pacman/g' test_pacman.py

Vishnu and Nahom worked together on Step 2, renaming components, updating branches, and cleaning up the Git history.
Gautham successfully handled Step 3, setting up the GitHub Actions CI/CD pipeline for automated testing and linting.
Gaoussou reviewed the code contributions from team members and wrote this report to summarize our work.
