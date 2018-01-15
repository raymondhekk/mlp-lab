#指定要导出的模块， 使用的地方可以直接  from pack import * 
#例如
__all__ = ['funs']


#从包中的每一个模块导入其中的函数，从而能够使得函数方法能够被直接调用。
#注意，一定要写包的名称calculate.作为前缀，不然会找不到模块！
#包的编写内容比较繁杂，主要是__init__.py这一重要文件决定了包的导入和使用方式，需要细心设计，站在用户的角度设计出易于调用的包。

from mymath.funs import plus
from mymath.funs import multi
