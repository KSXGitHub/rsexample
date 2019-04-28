###################################################################################
#                                                                                 #
# NAME: meson.build                                                               #
#                                                                                 #
# AUTHOR: Michael Brockus.                                                        #
#                                                                                 #
# CONTACT: <mailto:michael@squidfarts.com>                                        #
#                                                                                 #
# NOTICES:                                                                        #
#                                                                                 #
# MIT License                                                                     #
#                                                                                 #
# Copyright (c) 2019 Micheal Brockus                                              #
#                                                                                 #
# Permission is hereby granted, free of charge, to any person obtaining a copy    #
# of this software and associated documentation files (the "Software"), to deal   #
# in the Software without restriction, including without limitation the rights    #
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell       #
# copies of the Software, and to permit persons to whom the Software is           #
# furnished to do so, subject to the following conditions:                        #
#                                                                                 #
# The above copyright notice and this permission notice shall be included in all  #
# copies or substantial portions of the Software.                                 #
#                                                                                 #
# DISCLAIMERS:                                                                    #
#                                                                                 #
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR      #
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,        #
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE     #
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER          #
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,   #
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE   #
# SOFTWARE.                                                                       #
#                                                                                 #
###################################################################################



##
#
# Meson: Include directories
#
##
exe_dir = include_directories('.')



##
#
# Meson: List an array of source files
#
##
exe_src = files('main.rs')



##
#
# Meson: Check my targets headers.
#
##
assert(py3_mod.language_version().version_compare('>= 3.6.0'), 'Python version 3.6.0 or newer is required!')



##
#
# Meson: Create my target.
#
##
exe_main = executable(meson.project_name(),
    sources: exe_src,
    include_directories: exe_dir,
    dependencies: [ threads_dep, python3_dep, libmath_dep ],
    install: get_option('install_exe'))




##
#
# Meson: Test target.
#
##
benchmark('benchmark item exe.' ,exe_main)



##
#
# Meson: Test target.
#
##
test('testing my exe.' ,exe_main)
test('testing conanfile.', py3, args : join_paths('..', 'conanfile.py'))