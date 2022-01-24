import os

def find_files_with_suffix(directory, suffix):
    """Takes 2 strings, directory and suffix
       Searches the directory and all of its subdirectories and returns a
       list of complete paths for all files with the given suffix"""
    result = []
    suffix_length = len(suffix)
    for(root, dirs, files) in os.walk(directory):
        for item in files:
            if item.endswith(suffix):
                result.append(os.path.join(root, item))
    return result
    
def pipe(command):
    """Runs a unix command, returns result"""
    fp = os.popen(command)
    result = fp.read()
    fp.close()
    return result
    
def find_identical_checksums(directory, suffix):
    """Takes 2 strings, a directory path and a filename suffix
       Returns a list of lists of filenames (with full path) that have
       the same md5sum"""
    result = []
    md5_dict = dict()
    
    t = find_files_with_suffix(directory, suffix)
    for file in t:
        res = pipe('md5sum ' + file)
        md5sum = res.split(' ')[0]
        if md5sum in md5_dict:
            md5_dict[md5sum] += [file]
        else:
            md5_dict[md5sum] = [file]

    for md5sum, files in md5_dict.items():
        if len(files) > 1:
            result.append(files)

    return result
    
def find_duplicates(directory, suffix):
    """Recursively searches string 'directory' for files ending with string
       'suffix'
       Prints matching files with the same md5sum and whether the diff command
       shows that they are identical"""
    res = find_identical_checksums('test_mp3s', '.mp3')
    for files in res:
        for item1 in files:
            for item2 in files:
                if item1 < item2:
                    print('These 2 files have the same md5 sum:\n', item1, item2)
                    diff = pipe('diff '+ item1 + ' ' + item2)
                    if diff == '':
                        print('and they have the same contents')
                    else:
                        print('but have different contents!')


find_duplicates('test_mp3s', '.mp3')
