'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.EGL import _types as _cs
# End users want this...
from OpenGL.raw.EGL._types import *
from OpenGL.raw.EGL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'EGL_HI_clientpixmap'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.EGL,'EGL_HI_clientpixmap',error_checker=_errors._error_checker)
EGL_CLIENT_PIXMAP_POINTER_HI=_C('EGL_CLIENT_PIXMAP_POINTER_HI',0x8F74)
@_f
@_p.types(_cs.EGLSurface,_cs.EGLDisplay,_cs.EGLConfig,ctypes.POINTER(_cs.EGLClientPixmapHI))
def eglCreatePixmapSurfaceHI(dpy,config,pixmap):pass
