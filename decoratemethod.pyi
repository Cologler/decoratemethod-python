# -*- coding: utf-8 -*-
#
# Copyright (c) 2020~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

from typing import Any, Callable, TypeVar

_T = TypeVar('_T')

def decorate(decorator_func: Callable[..., _T]) -> _T: ...
