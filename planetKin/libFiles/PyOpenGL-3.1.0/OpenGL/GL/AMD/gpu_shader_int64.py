'''OpenGL extension AMD.gpu_shader_int64

This module customises the behaviour of the 
OpenGL.raw.GL.AMD.gpu_shader_int64 to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/AMD/gpu_shader_int64.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.AMD.gpu_shader_int64 import *
from OpenGL.raw.GL.AMD.gpu_shader_int64 import _EXTENSION_NAME

def glInitGpuShaderInt64AMD():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

# INPUT glUniform1i64vNV.value size not checked against count
glUniform1i64vNV=wrapper.wrapper(glUniform1i64vNV).setInputArraySize(
    'value', None
)
# INPUT glUniform2i64vNV.value size not checked against None
glUniform2i64vNV=wrapper.wrapper(glUniform2i64vNV).setInputArraySize(
    'value', None
)
# INPUT glUniform3i64vNV.value size not checked against None
glUniform3i64vNV=wrapper.wrapper(glUniform3i64vNV).setInputArraySize(
    'value', None
)
# INPUT glUniform4i64vNV.value size not checked against None
glUniform4i64vNV=wrapper.wrapper(glUniform4i64vNV).setInputArraySize(
    'value', None
)
# INPUT glUniform1ui64vNV.value size not checked against count
glUniform1ui64vNV=wrapper.wrapper(glUniform1ui64vNV).setInputArraySize(
    'value', None
)
# INPUT glUniform2ui64vNV.value size not checked against None
glUniform2ui64vNV=wrapper.wrapper(glUniform2ui64vNV).setInputArraySize(
    'value', None
)
# INPUT glUniform3ui64vNV.value size not checked against None
glUniform3ui64vNV=wrapper.wrapper(glUniform3ui64vNV).setInputArraySize(
    'value', None
)
# INPUT glUniform4ui64vNV.value size not checked against None
glUniform4ui64vNV=wrapper.wrapper(glUniform4ui64vNV).setInputArraySize(
    'value', None
)
glGetUniformi64vNV=wrapper.wrapper(glGetUniformi64vNV).setOutput(
    'params',size=_glgets._glget_size_mapping,pnameArg='location',orPassIn=True
)
# OUTPUT glGetUniformui64vNV.params COMPSIZE(program,location) 
# INPUT glProgramUniform1i64vNV.value size not checked against count
glProgramUniform1i64vNV=wrapper.wrapper(glProgramUniform1i64vNV).setInputArraySize(
    'value', None
)
# INPUT glProgramUniform2i64vNV.value size not checked against None
glProgramUniform2i64vNV=wrapper.wrapper(glProgramUniform2i64vNV).setInputArraySize(
    'value', None
)
# INPUT glProgramUniform3i64vNV.value size not checked against None
glProgramUniform3i64vNV=wrapper.wrapper(glProgramUniform3i64vNV).setInputArraySize(
    'value', None
)
# INPUT glProgramUniform4i64vNV.value size not checked against None
glProgramUniform4i64vNV=wrapper.wrapper(glProgramUniform4i64vNV).setInputArraySize(
    'value', None
)
# INPUT glProgramUniform1ui64vNV.value size not checked against count
glProgramUniform1ui64vNV=wrapper.wrapper(glProgramUniform1ui64vNV).setInputArraySize(
    'value', None
)
# INPUT glProgramUniform2ui64vNV.value size not checked against None
glProgramUniform2ui64vNV=wrapper.wrapper(glProgramUniform2ui64vNV).setInputArraySize(
    'value', None
)
# INPUT glProgramUniform3ui64vNV.value size not checked against None
glProgramUniform3ui64vNV=wrapper.wrapper(glProgramUniform3ui64vNV).setInputArraySize(
    'value', None
)
# INPUT glProgramUniform4ui64vNV.value size not checked against None
glProgramUniform4ui64vNV=wrapper.wrapper(glProgramUniform4ui64vNV).setInputArraySize(
    'value', None
)
### END AUTOGENERATED SECTION