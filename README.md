ruby-install2rpm
================

This is a cool little bash utility I wrote a couple years back to install isolated Ruby environments compiled from source, create a generated RPM spec file from that environment to build turned into an RPM.

Why will this help me?
======================
Well it is true that are other utilities out there that do this sort of
thing but the reason I created this project was mostly because those
other utilities didn't support 'all the functionality and flexibility'
in one utility.  The main goal for this project was to create small
isolated ruby environment that can be turned into RPMs (optional) for
ease of deploying or perhaps you may find a better use for it.

I'm sharing with the public now in hopes that it will help others.

Before You Start PLEASE READ
============================
This has only been tested on CentOS/RedHat 5.x and 6.x. 
These distros has always been my main platform and this script currently
tries to install all the required packages for you before the build 
takes place but the current package names are CentOS/RedHat sytle.

Overview
========
Build an entire base ruby environment from source and create a RPM spec.

To build this new environemt, you should run this build on a build machine 
rather than a host that this build is to be installed on.  The reason
for this is because there are a lot of development packages that are
needed to compile ruby that are not needed on say your production hosts.
They are only required for the build portion.

Should any of the scipts fail, you 'should' be able to pick up at the
exact location 
of where the build failed by re-running the script that failed.  All
scripts live in
the bin/ directory.

Directory Structure
===================
bin/   -> Contains all the binaries need to create the new build
build/ -> Contails the unpacked source tar.gz file
gems/  -> The downloaded default gems to package into the ruby environment
./     -> The root directory of this project also where you place the
          source for ruby-version.tar.gz.

You download the source files for the environment you want to build and 
place it into root directory of the cloned repo.  For example, if you
cloned this into ruby-install2pm, place the SOURCE-VERSION.tar.gz into
that directory.  

NOTE: The source must be a tar.gz file... Sorry

HELP, How Does This Script Work And How Do I Build A New Ruby
=============================================================
Kind of hard to explain for all use cases but.... If you are familiar
with how kickstart does OS installs, you will see familairity between
this script and kickstart.

It is assumed you are already in the bin directory of this folder.

The file rubyinstall.rc should a symlink that points to an Ruby
environment file that contains information on how to build your new RUBY
version. When you want to build a new ruby version, you must change this
symlink manually.

Each ruby-version-install.rc file is bash script that contains run time
configuration info for the Ruby environment you are building.  Here is
an example for Ruby 1.9.3-p0

While back in the day when I created this script I originally tried to
reduce the duplication in these '.rc' files there were certain
situations (normally with older rubies) that I felt like it was better
to just copy and paste these files rather than inherit defaults.... etc.

```
$ cat ruby-1.9.3-p0-install.rc 
#!/bin/bash

# The directory that we will install the built package
# this should be the root directory for the install.
export INSTALL_ROOT_DIR="/opt"

# compile options to be used
export
CONFIGURE_OPTS="--enable-shared,--enable-rpath,--disable-install-doc,--without-X11,--without-tk"

# make install options
#export MAKE_INSTALL_OPTS="DESTDIR=/some/path"

# The version of ruby
export RUBY_VER="1.9.3-p0"
export RUBY="ruby-${RUBY_VER}"
export RUBY_DIR="$INSTALL_ROOT_DIR/$RUBY"

# This is the tar file that will contain the built package
export OUTPUT_TARGZ="${RUBY}-environment.tar.gz"

# The RPM release version, make sure to increment this if you make
changes
export RPM_RELEASE_VER="1"
```

When this file is created it is essentially the master file that is
sourced for other portions of the build process, there are many proceses
this script uses to build a new version of ruby.  T

NOTE: This detail below is the order in which install.sh sees the
files/scripts.

bin/install.sh => Is the master script, run this script with an
                  environment configuration as it's first argument without
                  the .rc at the end. Example: ./install.sh rubyinstall

bin/pkg.list   => This file contains a list of CentOS/RedHat/Fedora
                  package names used to build the new version of ruby.
                  Each package name should be on it's own line.

bin/build-ruby => The heard of the Ruby compiling: configuring, make, make
                  install. This uses values contained in the
                  ruby-version-install.rc run time configuration file.  
```
eval CFLAGS='$CFLAGS' ./build-ruby --package "$RUBY" --install-dir
"$INSTALL_ROOT_DIR" --configure-opts "$CONFIGURE_OPTS"
```

bin/post-install-ruby => This script is in charge of installing post
                         compile stuff like installing rubygems and
                         other base gems like rake, bundler.  For now
                         you need to manually add the gems you want to
                         install in this script.

bin/cleanup           => Runs the clean up script to clean out anything
                         you don't care about.  Normally this is just
                         the unpacked SOURCE in build/
```
eval ./cleanup "$BUILD_DIR"
```

bin/gen-rpmspec        => Generates an RPM spec for your newly created Ruby.
```
eval ./gen-rpmspec "$RC" 
```
 
Steps To Build A New Ruby
=========================
To build a new ruby environment just run the following script.
NOTE: Each time you run this script it will remove the old environment 
and there are no warning messages.

[INSTALL NOTES:]
Become root
cd bin
./install.sh rubyinstall

NOTE: You don't need to include the '.rc' at the end (even though on
disk it is runinstall.rc)

If any of the scripts fail, see if the problem can be fixed and re-run
the main install.sh
script to start over or if possible run the script that failed.
