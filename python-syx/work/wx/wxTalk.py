# -*- coding: utf-8 -*-
'''
这一次对上一个demo进行了扩充
主要是添加了tuling机器人的自动回复以及让python进程保持且可以调试
主要还是归功于wxpy的embed()函数。。。
tulingKey需要自己申请
很简单，上网站注册一下账号就ok了
下面给出图灵网址：http://www.tuling123.com/

然后就是wxpy的灵活使用，详情可以参照官网的API文档
网址：http://wxpy.readthedocs.io/zh/latest/index.html

然后接下来就是我写的一个小例子
主要功能有
1、单人聊天消息反馈（备注在代码里改，懒得写交互了，反正大家都懂得）
2、单人聊天消息发送（根据输入的备注，这里写了简单的交互，没写exception处理）
3、图灵自动聊天（可以通过关闭注册函数来关闭或者开启）

注意此代码不可直接复制粘贴：
1、需要自己申请tulingkey赋值
2、需要指定进程保持时候和谁通信
当然也可以自己做修改自由发挥！
'''

from __future__ import unicode_literals

import json

from wxpy import *
import requests

tulingKey = 'eeaa98347259474a865d3aad734d859c'
itchat = Bot(cache_path=False)
friend = itchat.friends().search(name=u'湖南中业金服不聊工作群')

# friend = itchat.friends().search(name=u'小冰')
tuling = Tuling(api_key=tulingKey)


# tuling自动回复的消息注册

def reply(msg):
    return tuling.do_reply(msg)

#接受到消息后的打印
@itchat.register(msg_types=TEXT)
def printMsg(msg):
    print(msg)
    print(tuling.url)
    print('tuling自动回复消息---'+reply(msg))


if __name__ == "__main__":
    embed()
