#!/bin/bash
################################################################################
# Author: Cody Lane
# Date: 11-11-11
#
# This is the script that wraps up all the other scripts in this directory so
# we have a one stop shop to build, install, cleanup a new ruby environment.
################################################################################

function err() {
    echo "ERR: $*" >&2
    exit 1
}

function usage() {
    echo "$CMD Usage: The environment rc configuration name."
    echo 
    echo "Example: If there was a config named rubyinstall.rc"
    echo "         Run the following: $CMD rubyinstall"
    exit 0
}

function create-rubyenv-script() {
    echo "# Auto-generated from $CMD on $(date +%Y-%m-%d) by $(whoami)"
    echo
    echo "RUBY_ROOT=\"$INSTALL_ROOT_DIR\""
    echo "RUBY_VER=\"$RUBY_VER\""
    echo 'RUBY_DIR="$RUBY_ROOT/ruby-$RUBY_VER"'
    echo
    echo '[ -d "$RUBY_DIR" ] && export LD_LIBRARY_PATH="$RUBY_DIR/$(ls $RUBY_DIR |grep lib)"'
    echo 'PATH="$RUBY_DIR/bin:$PATH"'
    echo "export RUBY_DIR"
}

### main ###

# global variables
CMD="${0##*/}"
BIN_DIR="${0%/*}"

# make sure we are running from the script locaction
cd "$BIN_DIR"
BIN_DIR="$(pwd)"

# if no command line arguments print the usage
[ "$#" -lt 1 ] && usage

RC="$1.rc"

source $RC

[ ! -e "$RC" ] && err "The RC file '$RC' doesn't exist. Unable to continue"

# set the full path to the root dir
cd "../"
ROOT_DIR="$(pwd)"
cd - >>/dev/null

[ -z "$ROOT_DIR" ] && err "The root directory variable ROOT_DIR has not be set or is undefined."

# try and source some ruby environment variables
RUBYENV_SCR="rubyenv.sh"
create-rubyenv-script >"$RUBYENV_SCR"

source "$RUBYENV_SCR"

# BUILD options
BUILD_DIR="$ROOT_DIR/build/$RUBY"

ME="$(whoami)"
[ "$ME" != "root" ] && err "You must be root to run this script."

# make sure we have the required variables before we continue
[ -z "$RUBY" ] && err "You must set the RUBY variable in $RC"
[ -z "$INSTALL_ROOT_DIR" ] && err "You must set the INSTALL_ROOT_DIR variable in $RC"
[ -z "$OUTPUT_TARGZ" ] && err "You must set the OUTPUT_TARGZ file in $RC"

# check to make sure the required dependency packages are instsalled
INSTALL_DEPS=$(eval ./check-packages --file "pkg.list")
[ $? -ne 0 ] && [ -z "$INSTALL_DEPS" ] && err "We need to install some pre-reqs but didn't get a list of files to install, unable to continue"

if [ -n "$INSTALL_DEPS" ]; then
    yum -y install $INSTALL_DEPS
    [ $? -ne 0 ] && err "Failed to install required package: '$i'"
fi

# build the ruby environment
eval CFLAGS='$CFLAGS' ./build-ruby --package "$RUBY" --install-dir "$INSTALL_ROOT_DIR" --configure-opts "$CONFIGURE_OPTS"
[ $? -ne 0 ] && err "The build-ruby script failed, unable to continue"

# post install for ruby
eval ./post-install-ruby

# cleanup
eval ./cleanup "$BUILD_DIR"

echo 
eval ./gen-rpmspec "$RC"

echo 
echo "Tarring up the installed source: '$RUBY_DIR'"
tar czf "$OUTPUT_TARGZ" "$RUBY_DIR" >>/dev/null

echo "Created tar file $OUTPUT_TARGZ"
echo "done."
