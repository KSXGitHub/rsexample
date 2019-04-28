#!/user/bin/env python3
###################################################################################
#                                                                                 #
# NAME: conanfile.py                                                              #
#                                                                                 #
# AUTHOR: Michael Brockus.                                                        #
#                                                                                 #
# CONTACT: <mailto:michael@squidfarts.com>                                        #
#                                                                                 #
# PURPOSE:                                                                        #
#                                                                                 #
# This class represents the consumers ConanFile.  It can be used to define        #
# dependencies for a given project if any and be used by anyone that is currently #
# using Conan.                                                                    #
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
from conans import ConanFile, Meson, tools
import os


class ProjectConan(ConanFile):
    settings = "os", "compiler", "build_type",
    generators = "pkg_config"

    def configure(self):
        del self.settings.compiler.libcxx
    # end of method configure

    def build(self):
        meson = Meson(self)
        meson.configure()
        meson.build()
    # end of method build

# end of conanfile class
