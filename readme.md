# ***rustProject***


## Description
==========================

This is a second generation out of the box project template using Meson build system.


## About
==========================

***rustProject*** is a second generation out of the box project template that uses 
the Meson build system.  Designed and deployed from a multi programming language 
codebase, currently home of C, C++, Rust, and Python.


## Features
==========================

* [x] Meson as the tool for generating build files.
* [x] Support for native package manager as will as WrapDB.
* [x] Project uses pkg-config to find external dependencies.
* [x] Python as the main scripting language.
* [x] Docker as the continuousness delivery tool.
* [x] Jenkins as the continuousness integration tool.
* [x] Distributed under the MIT license. See ``LICENSE`` for more information.
* [x] Example of a will structured GitHub project.  
* [x] Extremely generic project structure. 
* [x] Works out of the box.


## Required
==========================

* [Meson](https://github.com/mesonbuild/meson.git) version 0.50.0 or newer.
* [Ninja](https://github.com/ninja-build/ninja.git) version 1.14.0 or newer.
* [Python3](https://www.python.org) version 3.6 or newer.


## Downloding
==========================

To install this project the simplest way is to grab it off github with
this command the Github command looks something like this:

```console
git clone https://github.com/squidfarts/rsexample.git
```
You can also download it as a zip if you prefer.


## Build and install
==========================

## Setting up Meson.

Meson is a build system that is designed to be as user-friendly as possible without
sacrificing performance. The main tool for this is a custom language that the user
uses to describe the structure of his or her build. The main design goals of this
language has been simplicity, clarity and conciseness. Much inspiration was drawn
from the Python programming language, which is considered very readable, even to
people who have not programmed in Python before.

*Meson* has two main dependencies.

* [Python 3](https://python.org)
* [Ninja](https://github.com/ninja-build/ninja/)


## Running Meson

Meson requires that you have a source directory and a build directory and that these
two are different. In your source root must exist a file called 'meson.build'. To generate
the build system run this command:

```console
meson <source directory> <build directory>
```

Depending on how you obtained Meson the command might also be called `meson.py`
instead of plain `meson`. In the rest of this document we are going to use the latter form.


## Configuring the build directory

Let us assume that we have a source tree that has a Meson build system. This means
that at the topmost directory has a file called meson.build. We run the following
commands to get the build started.

```console
meson setup <build dir name>
```

The main usability difference between Ninja and Make is that Ninja will automatically
detect the number of CPUs in your computer and parallelize itself accordingly. You can
override the amount of parallel processes used with the command line argument
-j <num processes>.

OR:

By default Meson will use the Ninja backend to build your project. If you wish to use
any of the other backends, you need to pass the corresponding argument during
configuration time. As an example, here is how you would use Meson to generate a
Visual Studio 2017 project.

```console
meson setup <build dir name> --backend=vs2017
```

You can then open the generated solution with Xcode and compile it in the usual way.
A list of backends can be obtained with meson setup --help.

## Building from the source
If you are not using an IDE, Meson uses the Ninja build system to actually build the
code. To start the build, simply type the following command.

```console
ninja -C <build dir name>
```

## Running tests
Meson provides native support for running tests. The command to do that is simple.

```console
meson test -C <build dir name> --num-processes
```

## Installing
Installing the built software with Meson is just as simple as.

```console
meson install -C <build dir name>
```

This should build the project and install the project.


## Options
==========================

Most non-trivial builds require user-settable options.  As an example a program may 
have two different data backends that are selectable at build time. Meson provides 
for this by having a option definition file. Its name is ``meson_options.txt`` and 
it is placed at the root of your source tree.


## Options for features and libraries

Option ``use_theads`` is of type feature and is set to disabled by default this can be
changed by switching from enabled or disabled depending if you would like to use 
threads in your project.

Option ``use_python3`` is of type feature and is set to disabled by default this can be
changed by switching from enabled or disabled depending if you would like to use 
python3 lib in your project.

Option ``use_libmath`` is of type feature and is set to disabled by default this can be
changed by switching from enabled or disabled depending if you would like to use 
the math library in your project.


## Options for installing

Option ``install_exe`` is of type boolean and is set to true by default this can be
changed by switching from true or false depending if you would like to install your
project.

Option ``install_doc`` is of type boolean and is set to false by default this can be
changed by switching from true or false depending if you would like to install your
documentation with your project.


## Options for flags

Option ``let_werror`` is of type boolean and is set to true by default this can be 
changed by switching from true or false depending if you would like to use ``-Werror``
flag in your project.

To change their values use the -D option:
```console
meson configure -D<my amazing option>=<new option value>
```
This should help you configure the project settings to your liking.


## Contributing to the project
==========================

* Read the code_of_conduct.txt file first.
* Then go read the contributing.txt file.
* And don't forget license.txt.


## Contact
==========================

#### Developer and maintainer

* e-mail: "michael@squidfarts"


***Happy coding...***
