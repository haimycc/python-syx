#为了编写单元测试，我们需要引入Python自带的unittest模块
import unittest
from Dict import Dict

#引入Python自带的unittest模块
class TestDict(unittest.TestCase):
    def test_init(self):
        #生成类对象
        d = Dict(a=1, b='test')
        #判断类对象的构造函数参数
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        #生成类对象
        d = Dict()
        d['key'] = 'value'
        #判断类对象的构造函数参数
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        #生成类对象
        d = Dict()
        d.key = 'value'
        #判断类对象的构造函数参数
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        #生成类对象
        d = Dict()
        #判断类对象的构造函数参数
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        #生成类对象
        d = Dict()
        #判断类对象的构造函数参数
        with self.assertRaises(AttributeError):
            value = d.empty

#这样就可以把mydict_test.py当做正常的python脚本运行：
if __name__ == '__main__':
    unittest.main()
