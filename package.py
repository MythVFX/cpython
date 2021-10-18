name = "python"

version = "3.7.7.x.1.0.0"

authors = [
    "Guido van Rossum",
    "nico.vandenbosch@mythimage.com"
]

description = \
    """
    It's Python 3
    https://www.python.org/downloads/release/python-377/
    """
variants = [
    ['platform-linux', 'arch-x86_64'],
    ['platform-osx', 'arch-x86_64']
]

requires = [
]

# this is a pretty ugly way of building all the different variants but it works
# also, for some reason rez expands ths install_path to include the '/mnt/oracle/la', so
# we include some extra nastiness to strip it off so it doesn't get put into the RPATH of
# libraries
build_command = "cd {root};make clean;" \
                "./configure --prefix={install_path};"\
                "make install -j;"\
                "cd {install_path}/bin;ln -s python3 python"


uuid = "python"

# this appears to be the recommended way to install internally developed packages
# into a non-default release path
# unclear if support for multiple release paths was actually implemented/released in rez:
#https://github.com/nerdvegas/rez/issues/426
#https://github.com/nerdvegas/rez/pull/402
with scope("config") as c:
#    release_path = str(c.release_packages_path)
#    c.release_packages_path = release_path.replace("external", "internal")
    c.release_packages_path = "/software/packages/internal"

def commands():
    env.PATH.prepend("{root}/bin")
