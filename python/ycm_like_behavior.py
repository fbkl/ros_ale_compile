#!/usr/bin/env python
""" Implements the same behavior i had for youcompleme with ALE """

from __future__ import print_function
from os import path
from glob import glob
import xml.etree.ElementTree as ET
try:
    from catkin.find_in_workspaces import get_workspaces
except:
    print('#ERROR: cannot import catkin.find_in_workspaces. Is ROS installed? Did you source your environment?')

def find_compile_commands(some_file_ref):
    """
        finds the relevant compile_commands.json for a file with a given path
    """
    some_file = path.abspath(some_file_ref)
    my_workspaces = get_workspaces()
    
    found_ws = None
    is_isolated = False
    for devel_name in ['devel_isolated','devel']: 
        trimmed_devel = []
        for ws in my_workspaces:
            if devel_name in ws:
                trimmed_devel.append(ws.split(devel_name)[0])
        #print(trimmed_devel)
        for ws in trimmed_devel:
            if ws in some_file:
                found_ws = ws
                break 
        if found_ws:
            if devel_name == 'devel_isolated':
                is_isolated = True
            break

    if not found_ws:
        print('#ERROR: could not find file in any workspace. Worspaces need to be sourced for this thing to work!!')
        return
        #print(found_ws)
        ### create the build dir for this guy

    ## find the package name
    file_dir = path.split(some_file)[0]
    all_files_in_dir = glob(path.join(file_dir, '*'))
    #print(all_files_in_dir)
    found_package_xml = False
    while not found_package_xml:
        for a_file in all_files_in_dir:
            if "package.xml" in a_file:
                found_package_xml = True
                break
        if found_package_xml:
            break #I miss goto sometimes...
        file_dir = path.realpath(path.join(file_dir, ".."))
        if file_dir == "/":
            print('#ERROR: could not find package.xml in any upstream directory')
            return
            # break
        all_files_in_dir = glob(path.join(file_dir, '*'))
        #print(all_files_in_dir)
    ## should have found package, then the name of the package is not necessari
    tree = ET.parse(path.join(file_dir, "package.xml"))
    package_name = ""
    root = tree.getroot()
    try:
        for child in root.getchildren():
            if child.tag == 'name':
                package_name = child.text
    except:
        package_name = root.find('name').text
    if not package_name:
        print('#ERROR: could not parse package.xml in found package folder: '+file_dir)
        return

    build_dir_name = "build"
    if is_isolated:
        build_dir_name = "build_isolated"
    
    my_build_dir_ccs = path.join(found_ws, build_dir_name, package_name, "compile_commands.json")
    my_build_dir = path.join(found_ws, build_dir_name, package_name)
    
    if path.exists(my_build_dir_ccs):
        print(my_build_dir, end="")
        return
    else:
        #print(glob(path.join(my_build_dir, "*")))
        pass
    ## found what should be the compile_commands, but it isn't there
    print('#ERROR: no compile_commands.json in '+my_build_dir)


    #print(some_file)

if __name__ == "__main__":
    import sys
    find_compile_commands(sys.argv[1])
