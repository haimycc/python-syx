import git
from git import Repo
import os.path

repo = Repo("D:\python-syx")
print(repo.branches)    # 获取所有的分支
print(repo.untracked_files) # 获取所有未加入版本的文件
print(repo.active_branch)   # 当前活动分支
print(repo.head.reference)  # 当前活动分支
print(repo.remotes.origin)  # 获取一个运程库
origin = repo.remotes.origin
print(origin.exists())      # 判断一个远程库是否存在

from git import Repo
repoPath = r'D:\python-syx'
repo = Repo(repoPath)
master = repo.heads.master          # 获取master分支
# print(master.log())
tree  = repo.heads.master.commit.tree
# for entry in tree:                                         # intuitive iteration of tree members
# print(entry.name)
curBranch = repo.head.reference     # 当前活动分支

git = repo.git
#--graph --decorate --oneline --simplify-by-decoration --all
log = git.log('syx', graph=True, decorate=True, oneline=True, simplify_by_decoration=True, all=False)
# log = git.log('master', graph=True, decorate=True, oneline=True, simplify_by_decoration=True)
branchNow = str(log).splitlines()[0]
# print(branchNow)
if ('origin/master' in branchNow):
    print(str(curBranch) + "分支已经合并了master")
else:
    print(str(curBranch) + "分支未合并master")