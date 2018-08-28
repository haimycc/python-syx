#!/usr/bin/env python
# coding:utf-8
import codecs
import configparser
import re
import jenkins
import os


class JzPythonJenkins(object):
    '''
    Installing:
        pip install python-jenkins

    Import:
        import jenkins
    '''

    global globalName

    def __init__(self, username, password, url, foldName):
        global globalName
        globalName = foldName
        self.server = self.Connect(url, username, password, 100)

    def Connect(self, url, username, password, timeout):
        '''Create handle to Jenkins instance'''
        self.server = jenkins.Jenkins(url, username, password, timeout)
        return self.server

    # 编译
    def bulid(self, jobName):
        self.server.build_job(jobName)
        print(jobName + "已经编译")

    # 切换一个分支
    def changeBranch(self, jobName, branchName):
        fullJobName = self.getJobName(jobName)
        job_config = self.server.get_job_config(fullJobName)
        patten = '(?<=\*/).*(?=</name>)'
        reconfig = re.sub(patten, branchName.strip(), job_config, 0)
        self.server.reconfig_job(fullJobName, reconfig)
        print(str(jobName).strip() + "将分支从 " + self.getBranchName(job_config) + " --> " + branchName)

    # 切换分支并且编译
    def changeBranchAndBuild(self, jobName, branchName):
        fullJobName = self.getJobName(jobName)
        self.changeBranch(jobName, branchName.strip())
        self.bulid(fullJobName)

    # 获取被切换的分支名
    def getBranchName(self, repl):
        patten = '(?<=\*/).*(?=</name>)'
        res = re.findall(patten, repl)
        if (len(res) > 1):
            print("匹配的位置超过预期" + str(res))
        return str(res[0])

    def getJobName(self, job):
        return globalName + "/" + str(job).strip()

    # 切换所有分支并且编译
    def changeAllBulid(self, branchName, commonName=None):
        jobs = self.server.get_all_jobs()
        for job in jobs:
            self.changeBranch(job["name"], branchName.strip())
        if commonName:
            self.bulid(commonName)
        else:
            self.bulid("Common")

    def bulidFromFile(self, filePath):
        file = codecs.open(filePath, "r", "utf-8")
        while 1:
            # 用缓存效率提高3倍
            lines = file.readline(100000)
            if lines:
                split = str(lines).strip().split(",")
                #项目名必须和jenkins中的名字相同,否则找不到项目
                self.changeBranchAndBuild(split[0], split[1])
            else:
                break
        file.close()

    # 只编interface
    def bulidInterfaceNotMaster(self):
        jobs = self.server.get_all_jobs()
        for job in jobs:
            if "Interface" in job["name"]:
                config = self.server.get_job_config(job["fullname"])
                branchName = self.getBranchName(config)
                if "master" not in branchName:
                    self.bulid(self.getJobName(job["name"]))


#除了common之外重编所有Interface
if __name__ == "__main__":
    cf = configparser.ConfigParser()
    configDir = os.getcwd()
    cf.read(configDir + "\jenkinsConfig.txt")
    sections = cf.sections()
    username = str(cf.get("config", "username")).strip()
    password = str(cf.get("config", "password")).strip()
    url = str(cf.get("config", "url")).strip()
    view = str(cf.get("config", "view")).strip()
    try:
        jenkins = JzPythonJenkins(username, password, url, view)
        jenkins.bulidInterfaceNotMaster()
    except Exception as e:
        print(e)
    finally:
        os.system('pause')


