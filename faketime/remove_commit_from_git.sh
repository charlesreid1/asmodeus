
# http://stackoverflow.com/questions/448919/how-can-i-remove-a-commit-on-github#448929


git reset --soft HEAD^
git push origin +master




git stash
git rebase -i HEAD~2
git push origin +master



git push -f origin HEAD^:master
