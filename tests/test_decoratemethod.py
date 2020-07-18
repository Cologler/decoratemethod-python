# -*- coding: utf-8 -*-
#
# Copyright (c) 2020~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

from decoratemethod import decorate

def test_decorate_with_lru_cache():
    from functools import lru_cache
    from functools import singledispatch

    class Foo:
        def __init__(self):
            super().__init__()
            self.called = 0
            self.basevalue = 0

        @decorate(lru_cache)
        def add(self, value):
            self.called += 1
            return self.basevalue + value

    f1 = Foo()
    f2 = Foo()
    f1.basevalue = 15
    f2.basevalue = 30
    assert f1.add(20) == 35
    assert f2.add(30) == 60
    assert f1.add(20) == 35
    assert f2.add(30) == 60
    assert f1.called == 1
    assert f2.called == 1
    assert f1.add(50) == 65
    assert f2.add(50) == 80
    assert f1.add(50) == 65
    assert f2.add(50) == 80
    assert f1.called == 2
    assert f2.called == 2

