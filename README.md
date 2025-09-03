
# Install:

add to your `.vimrc` the lines (this uses Vundle):

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

# How it works:

This will find the `compile_commands.json` files for each of your packages and use those commands to add the necessary flags for both clangd and clang-tidy. Unfortunately if you use different flags for gcc, this might not work properly. 

For this to be possible you need to source the workspace which you are going to be using.

##  Usage:

Source the workspace that you already compiled:

    $ source devel/setup.bash

Then open vim/neovim. 

# Debug:

Use `:ALEInfo` inside vim to find out what went wrong.
