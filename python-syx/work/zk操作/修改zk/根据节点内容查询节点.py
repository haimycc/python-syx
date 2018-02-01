from kazoo.client import KazooClient
import traceback
import lxml.etree
import re

# 开发环境zk

devZk = KazooClient(hosts='192.168.9.173:2181')
devZk.start()


def getDiff(idcZk, nodeName):
    idcNodes = idcZk.get_children(nodeName)
    patten = b'<root.*</root>'
    for idcNode in idcNodes:
        modelNames = idcZk.get_children(nodeName + "/" + idcNode)
        for model in modelNames:
            logBackNode = nodeName + "/" + idcNode + "/" + model + "/YunWei/logback"
            try:
                modelYunWei = idcZk.get(logBackNode)
                textToReplace = b'<root level="ERROR"> \\n    <appender-ref ref="ASYNC"/>  \\n    <appender-ref ref="ASYNC-ERROR"/>  \\n    <appender-ref ref="SYSLOG"/>  \\n    <appender-ref ref="socket"/> \\n  </root>'
                # match = re.findall(patten, str(modelYunWei), re.S)
                ret = re.sub(patten, textToReplace, modelYunWei[0], 0, re.S)
                idcZk.set(logBackNode, ret)
                print(model + "修改")
            except:
                print(model)

getDiff(devZk, "/AppConfig")
devZk.stop()
