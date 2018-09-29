import configparser
import os
import codecs
from git import Repo
from git.cmd import Git


class GitPython():
    def getModuleAndBranch(self, filePath):
        file = codecs.open(filePath, "r", "utf-8")
        mbDict = {}
        while 1:
            # 用缓存效率提高3倍
            lines = file.readline(100000)
            if lines:
                split = str(lines).strip().split(",")
                # 项目名必须和jenkins中的名字相同,否则找不到项目
                mbDict[split[0]] = split[1]
            else:
                break
        file.close()
        return mbDict

    def GitPython(self, rootPath, moduleName, branchName):
        # repoPath = r'D:\python-syx'
        replace = str(rootPath + moduleName).replace("\\", "/")
        print(replace)
        g = Git(replace)

        #['git', 'fetch', 'origin', '--prune']
        execute = g.execute('git fetch -v --progress "origin"')
        for e in execute:
            print(e)
        print('ss' + str(execute))
        repo = Repo(rootPath + moduleName)
        git = repo.git
        log = git.log(
            'origin/' + branchName,
            # graph=True,
            decorate=True,
            oneline=True,
            simplify_by_decoration=True,
            all=False)
        branchFir = str(log).splitlines()[0]
        if ('origin/master' in branchFir):
            pass
        else:
            branchSec = str(log).splitlines()[1]
            if ('origin/master' in branchSec):
                pass
            else:
                print("==================================================")
                print("-->" + moduleName + "的[" + branchName + "]分支未合并master")
                logmaster = git.log(
                    'origin/master',
                    # graph=True,
                    decorate=True,
                    oneline=True,
                    simplify_by_decoration=True,
                    all=True)
                print(logmaster)


if __name__ == "__main__":
    cf = configparser.ConfigParser()
    configDir = os.getcwd()
    cf.read(configDir + r"\jenkinsConfig.txt", encoding='utf-8')
    sections = cf.sections()
    moduleRoot = str(cf.get("config", "moduleRoot")).strip()
    moduleAndBranch = (configDir + "\编译分支.txt")
    gitPython = GitPython()
    try:
        mbDict = gitPython.getModuleAndBranch(moduleAndBranch)
        for mb in mbDict:
            print("本次检测分支为" + mb + "的" + mbDict[mb])
        for mb in mbDict:
            print("==================================================")
            gitPython.GitPython(moduleRoot, mb, mbDict[mb])
    except Exception as e:
        print(e)
    finally:
        print("==================================================")
        print("检测完毕")
        # os.system('pause')
