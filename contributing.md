# ***CONTRIBUTING***

## So your contributing to the project
==========================

By making a contribution to this project, I certify that:

(a) The contribution was created in whole or in part by me and I
    have the right to submit it under the open source license 
    indicated in the file; or

(b) The contribution is based upon previous work that, to the best
    of my knowledge, is covered under an appropriate open source 
    license and I have the right under that license to submit that
    work with modifications, whether created in whole or in part by
    me, under the same open source license (unless I am permitted 
    to submit under a different license), as indicated in the file; or

(c) The contribution was provided directly to me by some other person
     who certified (a), (b) or (c) and I have not modified it.

(d) I understand and agree that this project and the contribution 
    are public and that a record of the contribution (including all 
    personal information I submit with it, including my sign-off) is 
    maintained indefinitely and may be redistributed consistent with 
    this project or the open source license(s) involved.



## Requirements.
==========================

* [Meson](https://github.com/mesonbuild/meson.git) version 0.50.0 or newer.
* [Ninja](https://github.com/ninja-build/ninja.git) version 1.14.0 or newer.
* [Python3](https://www.python.org) version 3.6 or newer.


## Why Have A Coding Standard?
==========================

Being consistent makes code easier to understand. I'm trying to keep this
project standard and simple because I also believe that we can only expect
someone to follow something that is understandable.  Please do your best.


## Readable
==========================

We want to read our code. This means we like names and flow that are more 
naturally read.  We try to avoid double negatives.  We try to avoid cryptic 
abbreviations (sticking to ones we feel are common).


## Naming
==========================

Let's talk about naming things. Programming is all about naming things. We
name files, functions, variables, and so much more. While we're not always 
going to find the best name for something.

When naming things, we follow this hierarchy, the first being the most 
important to us (but we do all four when possible):

1. Readable
2. Descriptive
3. Consistent
4. Memorable


## Git commit messages
==========================

## Basic Git Commit Message Tag Naming

By making good Git commit messages with common tagging for categorizing 
a contribution to this project, it can become esay to manage what commits where 
done and what time they where made.  I have written a list of what I consider a 
good collection of useful Git commit messages.

This commit message should only be used when you are going to update an 
excesting artifact from the project.

```console
Update: <example description> and <example of why>
```

This commit message should only be used when you are going to delete an 
artifact from the project.

```console
Delete: <example description> and <example of why>
```

This commit message should only be used when you are going to move an
artifact from one directory into another directory in the project.

```console
Move: <example description> and <example of why>
```

This commit message should only be used when you are going to add a new
artifact to the project.

```console
Add: <example description> and <example of why>
```

This commit message should only be used when you are going to fix a buggy
artifact in the project.

```console
Fix: <example description> and <example of why>
```


## Project CI/CD Work Flow
==========================

## Basic Overview 

I use ``Jenkins`` and ``Docker`` to automate this process of continues integration
and continues deployment so I may have time to do gardening, writing tutorials and
examples for new programmers and to have time to do programming work for other
suffocated companies like Google for example.

Developers of this project will only branch from and commit to ``develop`` so
I can marge the new committed fetchers into ``master`` branch.
