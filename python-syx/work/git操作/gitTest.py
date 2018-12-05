from git.cmd import Git
from git import Repo

repo = Repo('D:/HNXJ/allBranchs/BusinessOpenInterface')

# fetch = repo.remote().fetch()
# g = Git(r'D:\code\BusinessOpenInterface')
g = Git(r'D:/HNXJ/allBranchs/BusinessOpenInterface')
#['git', 'fetch', 'origin', '--prune']
remote = repo.remote()
repo.git.fetch()
# remote.push()
# branch = repo.git.branch(all=True)
# print(branch)
# execute = g.execute('git pull ')
# print(execute)
# print(remote)
# print(remotes)
# remote.pull()

repo = Repo(r'D:/HNXJ/allBranchs/BusinessOpenInterface')
repo.git.fetch()


# execute = g.('git fetch -v --progress "origin"')
# print(str(execute))
# print(str(fetch))
