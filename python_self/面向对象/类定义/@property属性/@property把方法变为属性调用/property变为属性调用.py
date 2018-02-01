# -*- coding:utf-8 -*-

class Student(object):
    #这个是把方法变为属性
    @property
    def score(self):
        return self._score

    #设置属性
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


s = Student()
#实际转化为s.set_score(60)
s.score = 60
print(s.score)
