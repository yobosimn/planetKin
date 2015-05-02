'''OpenGL extension ANGLE.program_binary

This module customises the behaviour of the 
OpenGL.raw.GLES2.ANGLE.program_binary to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/ANGLE/program_binary.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GLES2 import _types, _glgets
from OpenGL.raw.GLES2.ANGLE.program_binary import *
from OpenGL.raw.GLES2.ANGLE.program_binary import _EXTENSION_NAME

def glInitProgramBinaryANGLE():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION