
# Install:

add to your `.vimrc` the lines:

    Plugin 'dense-analysis/ale'
    Plugin 'fbkl/ros_ale_compile'

Make sure you have clangd (will provide the ALEGoTo... navigation) and clang-tidy (will do the syntax):

    $ sudo apt install clangd clang-tidy -y

You may want to update your alternatives in case you have different versions of clangd and clang-tidy installed, like:

    $ sudo update-alternatives --install /usr/bin/clangd clangd /usr/bin/clangd-10 100
    $ sudo update-alternatives --install /usr/bin/clang-tidy clang-tidy /usr/bin/clang-tidy-10 100

Now you need the `compile_commands.json` files to be generated. Either do:

    $ catkin config -cmake-args -DCMAKE_EXPORT_COMPILE_COMMANDS=ON

or add to each CMakeLists.txt the line:

    set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
