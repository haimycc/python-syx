#!/usr/bin/env python
# coding:utf-8
import codecs
import re
import jenkins


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
        # password = '924524abef31e057df10f9c4e2dd669a'
        timeout = 100
        self.server = self.Connect(url, username, password, timeout)

    def Used(self):
        self.get_version()

    def Connect(self, url, username, password, timeout):
        '''Create handle to Jenkins instance'''
        self.server = jenkins.Jenkins(url, username, password, timeout)
        return self.server

    def get_version(self):
        '''get jenkins version'''
        version = self.server.get_version()
        print(version)

    def job(self):
        # 创建Project,内容为空
        self.server.create_job('test', jenkins.EMPTY_CONFIG_XML)

        # job构建empty
        self.server.build_job('empty')

        # 获取job配置 prints XML configuration
        my_job = self.server.get_job_config('empty')
        print(my_job)

        # # 禁用Project
        # self.server.disable_job('empty')
        #
        # # 拷贝Project
        # self.server.copy_job('empty', 'empty_copy')
        #
        # # 启用已配置好Project
        # self.server.enable_job('empty')
        #
        # # 删除Project
        # self.server.delete_job('empty')

    def view(self):
        # 创建空视图
        self.server.create_view('EMPTY', jenkins.EMPTY_VIEW_CONFIG_XML)

        # 获取视图的配置xml信息
        view_config = self.server.get_view_config('EMPTY')

        # 获取视图信息
        views = self.server.get_views()
        print(views)

        # 删除视图
        # self.server.delete_view('EMPTY')

    def plugins(self):
        # 获取插件信息
        plugins = self.server.get_plugins_info()
        print(plugins)

    def node(self):
        # 创建node节点
        self.server.create_node('slave123456')

        ## create node with parameters
        params = {
            'port': '22',
            'username': 'juser',
            'credentialsId': '10f3a3c8-be35-327e-b60b-a3e5edb0e45f',
            'host': 'my.jenkins.slave11'
        }
        ## 名称,描述,远程工作目录,标签,用法，启动方法(连接方式),参数(如host)
        self.server.create_node(
            'slave11',
            nodeDescription='my test slave',
            remoteFS='/home/juser',
            labels='precise',
            exclusive=True,
            launcher=jenkins.LAUNCHER_SSH,
            launcher_params=params)

        # 获取node信息
        nodes = self.server.get_nodes()
        print(nodes)

        # 获取node配置信息
        node_config = self.server.get_node_info('slave123456')
        print(node_config)

        # 连接或中断node
        # self.server.disable_node('slave11')
        # self.server.enable_node('slave11')

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
            self.bulid(self.getJobName(job["name"]))
        if commonName:
            self.bulid(self.getJobName(commonName))
        else:
            self.bulid(self.getJobName("Common"))

    def bulidFromFile(self, filePath):
        file = codecs.open(filePath, "r", "utf-8")
        while 1:
            # 用缓存效率提高3倍
            lines = file.readline(100000)
            if lines:
                split = str(lines).strip().split(",")
                # 项目名必须和jenkins中的名字相同,否则找不到项目
                self.changeBranchAndBuild(split[0], split[1])
            else:
                break
        file.close()

    # 根据正则替换内容 only就只看正则能替换的部分
    def changeByPatten(self, patten, value, only_show):
        jobs = self.server.get_all_jobs()
        for job in jobs:
            fullJobName = self.getJobName(job["name"])
            # if ('App' in job["name"] or 'Schedule' in job["name"]):
            #     value = '<execCommand>cd /usr/local/dubbox/; ./' + job["name"] + '.sh restart</execCommand>'
            # else:
            #     continue
            job_config = self.server.get_job_config(fullJobName)
            # print(job_config)
            # patten = '(?<=\<url>)http(?=\:)'
            search = re.search(patten, job_config)
            # print(search)
            if (only_show):
                print(search)
            elif (search):
                reconfig = re.sub(patten, value, job_config, 0)
                # print(reconfig)
                self.server.reconfig_job(fullJobName, reconfig)
                print(fullJobName + "修改成功")
                # search = re.search(patten, job_config)
                # print(search)

    def getAllBranch(self, urlname, mastername, findBug):
        jobs = self.server.get_all_jobs()
        print("当前环境为[" + urlname + "]" + "主分支为[" + mastername + "]")
        flag = True
        for job in jobs:
            job_config = self.server.get_job_config(job["fullname"])
            branch_name = self.getBranchName(job_config)
            if findBug:
                print(job["fullname"] + " 当前分支为--> " + branch_name)
                flag = False
            else:
                if mastername.strip() != branch_name.strip():
                    print(job["fullname"] + " 当前分支为--> " + branch_name)
                    flag = False
        if flag:
            print("所有分支均为" + mastername)

    # 同步不同环境的相同配置
    def syncSettingInfo(self, target):
        jobs = self.server.get_all_jobs()
        for job in jobs:
            config = self.server.get_job_config(job["fullname"])
            target.server.create_job(job["fullname"], config)
            print(job["fullname"] + " 已经创建")

    # 只编interface
    def bulidAllInterface(self):
        jobs = self.server.get_all_jobs()
        for job in jobs:
            if "Interface" in job["name"]:
                self.changeBranchAndBuild(job["name"], "master")

    # 只编interface
    def bulidNecessarilyInterface(self):
        jobs = self.server.get_all_jobs()
        for job in jobs:
            if "Interface" in job["name"]:
                config = self.server.get_job_config(job["fullname"])
                branchName = self.getBranchName(config)
                if "master" not in branchName:
                    self.changeBranchAndBuild(job["name"], "master")
        print("编译完成")

    # 只编非master分支
    def bulidNotMasterToMaster(self):
        jobs = self.server.get_all_jobs()
        for job in jobs:
            config = self.server.get_job_config(job["fullname"])
            branchName = self.getBranchName(config)
            if "master" not in branchName:
                self.changeBranchAndBuild(job["name"], "master")
        print("编译完成")

    # 只编interface
    def bulidInterfaceNotMaster(self):
        jobs = self.server.get_all_jobs()
        for job in jobs:
            if "Interface" in job["name"]:
                config = self.server.get_job_config(job["fullname"])
                branchName = self.getBranchName(config)
                if "master" not in branchName:
                    self.bulid(self.getJobName(job["name"]))

if __name__ == "__main__":
    # 174
    # jenkins = JzPythonJenkins("admin", "111111", "http://192.168.9.174:8081/jenkins/", "ZYFAX")
    # jenkins = JzPythonJenkins("admin", "a123456", "http://10.3.100.109:8081/jenkins/", "ZYFAX")
    # jenkins.getAllBranch("109", "master", True)
    # 103
    # jenkins = JzPythonJenkins("admin", "zyxr123456", "http://192.168.9.152:8081/jenkins/", "ZYXR")
    # jenkins = JzPythonJenkins("admin", "Test123456", "http://192.168.9.104:8081/jenkins/", "ZYXR")
    # jenkins = JzPythonJenkins("admin", "Test123456", "http://192.168.9.126:8081/jenkins/", "ZYXR")
    # jenkins = JzPythonJenkins("admin", "a123456", "http://192.168.9.116:8081/jenkins/", "ZYXR")
    # jenkins = JzPythonJenkins("admin", "111111", "http://192.168.9.154:8081/jenkins/", "ZYXR")
    # jenkins = JzPythonJenkins("admin", "Test123456", "http://192.168.9.122:8081/jenkins/", "ZYXR")
    # 175
    jenkins = JzPythonJenkins("admin", "a123456", "http://192.168.9.175:8081/jenkins/", "ZYFAX")
    # jenkins.changeAllBulid("goldmaster")
    # 切换一个分支并且编译
    # jenkins.changeBranchAndBuild("AccountAdminWeb", "goldmaster")
    # jenkins.changeBranchAndBuild("AssetWeb", "gm-syx-社会码脱敏")
    # jenkins.changeBranch("ProductWeb", "master")
    # 切换所有分支为主干分支 并且编译Common
    # jenkins.changeAllBulid("master")
    # 从文件读取分支并且编译
    ########文件格式###########
    # AssetAdminWeb,goldmaster
    # TrusteeSchedule,gm-合伙人
    # UserAdminWeb,bbbb
    ##########################

    # jenkins.bulidFromFile("D:\编译分支.txt")
    # 154
    # jenkins = JzPythonJenkins("admin", "111111", "http://192.168.9.154:8081/jenkins/", "ZYXR")
    # 获取分支
    # jenkins.getAllBranch("126", "master")

    # 切换仓库
    # jenkins.changeAllRepository()
    # jenkins.getAllBranch("174", "master")
    # 切换用户
    # jenkins175.changeByPatten('(?<=<credentialsId>).*(?=</credentialsId>)', '512d8ac1-c91f-4f09-800a-3c8c25640b3c')
    # jenkins = JzPythonJenkins("admin", "a123456", "http://10.3.100.106:8081/jenkins/", "ZYFAX")
    # jenkins.changeByPatten('(?<=<credentialsId>).*(?=</credentialsId>)', '92ac09dc-b6ea-44d0-977e-5940c61e054b', False)
    # 同步配置
    # jenkins175.syncSettingInfo(jenkins)

    # 修改处理语句
    # jenkins9.changeByPatten('(?<=<execCommand>).*(?=</execCommand>)', 'cd /usr/local/dubbox/; ./AdminApp.sh restart', False)
    # jenkins9.changeByPatten('<execCommand/>', 'cd /usr/local/dubbox/; ./AdminApp.sh restart', False)
    # jenkins.changeByPatten('(?<=\<url>)https(?=\:)', 'http', True)
    # http改https
    # jenkins.changeByPatten('(?<=\<url>)http(?=\:)', 'https', False)

    # jenkins9.changeAllBulid('master')
    # jenkins.bulidAllInterface()
    # jenkins.bulidNecessarilyInterface()
    # jenkins.bulidNotMasterToMaster()
    jenkins.bulidInterfaceNotMaster()
