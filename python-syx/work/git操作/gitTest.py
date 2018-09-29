from git.cmd import Git
from git import Repo

repo = Repo('D:/HNXJ/allBranchs/VisualDataAdminWeb')

# fetch = repo.remote().fetch()
g = Git(r'D:\HNXJ\allBranchs\VisualDataAdminWeb')
#['git', 'fetch', 'origin', '--prune']
execute = g.execute('git fetch -v --progress "origin"')
print(str(execute))
# print(str(fetch))
