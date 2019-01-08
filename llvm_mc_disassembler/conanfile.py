from conans import python_requires
import os

common = python_requires('llvm-common/0.0.0@Manu343726/testing')

class LLVMMCDisassembler(common.LLVMModulePackage):
    version = common.LLVMModulePackage.version
    name = 'llvm_mc_disassembler'
    llvm_component = 'llvm'
    llvm_module = 'MCDisassembler'
    llvm_requires = ['llvm_mc', 'llvm_support']
    include_dirs = [os.path.join('llvm', 'MC', 'MCDisassembler')]
