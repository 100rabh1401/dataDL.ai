# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_interpreter_wrapper')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_interpreter_wrapper')
    _interpreter_wrapper = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_interpreter_wrapper', [dirname(__file__)])
        except ImportError:
            import _interpreter_wrapper
            return _interpreter_wrapper
        try:
            _mod = imp.load_module('_interpreter_wrapper', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _interpreter_wrapper = swig_import_helper()
    del swig_import_helper
else:
    import _interpreter_wrapper
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0


def PyListToStdVectorString(list, strings):
    return _interpreter_wrapper.PyListToStdVectorString(list, strings)
PyListToStdVectorString = _interpreter_wrapper.PyListToStdVectorString
class InterpreterWrapper(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, InterpreterWrapper, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, InterpreterWrapper, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __swig_destroy__ = _interpreter_wrapper.delete_InterpreterWrapper
    __del__ = lambda self: None

    def AllocateTensors(self):
        return _interpreter_wrapper.InterpreterWrapper_AllocateTensors(self)

    def Invoke(self):
        return _interpreter_wrapper.InterpreterWrapper_Invoke(self)

    def InputIndices(self):
        return _interpreter_wrapper.InterpreterWrapper_InputIndices(self)

    def OutputIndices(self):
        return _interpreter_wrapper.InterpreterWrapper_OutputIndices(self)

    def ResizeInputTensor(self, i, value):
        return _interpreter_wrapper.InterpreterWrapper_ResizeInputTensor(self, i, value)

    def NumTensors(self):
        return _interpreter_wrapper.InterpreterWrapper_NumTensors(self)

    def TensorName(self, i):
        return _interpreter_wrapper.InterpreterWrapper_TensorName(self, i)

    def TensorType(self, i):
        return _interpreter_wrapper.InterpreterWrapper_TensorType(self, i)

    def TensorSize(self, i):
        return _interpreter_wrapper.InterpreterWrapper_TensorSize(self, i)

    def TensorSizeSignature(self, i):
        return _interpreter_wrapper.InterpreterWrapper_TensorSizeSignature(self, i)

    def TensorQuantization(self, i):
        return _interpreter_wrapper.InterpreterWrapper_TensorQuantization(self, i)

    def TensorQuantizationParameters(self, i):
        return _interpreter_wrapper.InterpreterWrapper_TensorQuantizationParameters(self, i)

    def SetTensor(self, i, value):
        return _interpreter_wrapper.InterpreterWrapper_SetTensor(self, i, value)

    def GetTensor(self, i):
        return _interpreter_wrapper.InterpreterWrapper_GetTensor(self, i)

    def ResetVariableTensors(self):
        return _interpreter_wrapper.InterpreterWrapper_ResetVariableTensors(self)

    def NumNodes(self):
        return _interpreter_wrapper.InterpreterWrapper_NumNodes(self)

    def NodeName(self, i):
        return _interpreter_wrapper.InterpreterWrapper_NodeName(self, i)

    def NodeInputs(self, i):
        return _interpreter_wrapper.InterpreterWrapper_NodeInputs(self, i)

    def NodeOutputs(self, i):
        return _interpreter_wrapper.InterpreterWrapper_NodeOutputs(self, i)

    def tensor(self, base_object, i):
        return _interpreter_wrapper.InterpreterWrapper_tensor(self, base_object, i)

    def ModifyGraphWithDelegate(self, delegate):
        return _interpreter_wrapper.InterpreterWrapper_ModifyGraphWithDelegate(self, delegate)
    if _newclass:
        CreateWrapperCPPFromFile = staticmethod(_interpreter_wrapper.InterpreterWrapper_CreateWrapperCPPFromFile)
    else:
        CreateWrapperCPPFromFile = _interpreter_wrapper.InterpreterWrapper_CreateWrapperCPPFromFile
    if _newclass:
        CreateWrapperCPPFromBuffer = staticmethod(_interpreter_wrapper.InterpreterWrapper_CreateWrapperCPPFromBuffer)
    else:
        CreateWrapperCPPFromBuffer = _interpreter_wrapper.InterpreterWrapper_CreateWrapperCPPFromBuffer
InterpreterWrapper_swigregister = _interpreter_wrapper.InterpreterWrapper_swigregister
InterpreterWrapper_swigregister(InterpreterWrapper)

def InterpreterWrapper_CreateWrapperCPPFromFile(*args):
    return _interpreter_wrapper.InterpreterWrapper_CreateWrapperCPPFromFile(*args)
InterpreterWrapper_CreateWrapperCPPFromFile = _interpreter_wrapper.InterpreterWrapper_CreateWrapperCPPFromFile

def InterpreterWrapper_CreateWrapperCPPFromBuffer(*args):
    return _interpreter_wrapper.InterpreterWrapper_CreateWrapperCPPFromBuffer(*args)
InterpreterWrapper_CreateWrapperCPPFromBuffer = _interpreter_wrapper.InterpreterWrapper_CreateWrapperCPPFromBuffer

# This file is compatible with both classic and new-style classes.


