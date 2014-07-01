import os, re, shutil, itom

#this scripts overwrites the .rst-files for the single plugin documentations from the real source
#of the plugin documentation files

def scanForRstFiles(folder, recursive = True):
    dirEntries = os.listdir(folder)
    result = []
    
    for entry in dirEntries:
        path = os.path.join(folder, entry)
        
        if (os.path.isdir(path)):
            if (recursive):
                result += scanForRstFiles(path, recursive)
        else: #file
            if re.match(".*\.rst", entry):
                result.append( [entry, path] )
    
    return result

#scan all rst-files in mainsite_hidden/source/plugins
abspath = os.path.join(itom.getCurrentPath(), "source/plugins")

destinations = scanForRstFiles(abspath, True)

dir = itom.ui.getExistingDirectory("Source directory that is recursively scanned for the rst-files of each plugin", getCurrentPath())

if (not dir is None):
    sources = scanForRstFiles(dir, True)
    
    for dest in destinations:
        filename = dest[0]
        destPath = dest[1]
        
        for src in sources:
            if (src[0] == filename):
                shutil.copy(src[1], destPath)
                print("copy", src[1], "to", destPath)