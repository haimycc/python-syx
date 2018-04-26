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

    def getAllBranch(self, urlname, mastername):
        jobs = self.server.get_all_jobs()
        print("当前环境为[" + urlname + "]" + "主分支为[" + mastername + "]")
        flag = True
        for job in jobs:
            job_config = self.server.get_job_config(job["fullname"])
            branch_name = self.getBranchName(job_config)
            if mastername.strip() != branch_name.strip():
                print(job["fullname"] + " 当前分支为--> " + branch_name)
                flag = False
        if flag:
            print("所有分支均为" + mastername)


if __name__ == "__main__":
    cf = configparser.ConfigParser()
    configDir = os.getcwd()
    cf.read(configDir + "\jenkinsConfig.txt")
    sections = cf.sections()
    username = str(cf.get("config", "username")).strip()
    password = str(cf.get("config", "password")).strip()
    url = str(cf.get("config", "url")).strip()
    view = str(cf.get("config", "view")).strip()
    mastername = str(cf.get("config", "mastername")).strip()
    try:
        jenkins = JzPythonJenkins(username, password, url, view)
        jenkins.getAllBranch(url, mastername)
    except Exception as e:
        print(e)
    finally:
        os.system('pause')
