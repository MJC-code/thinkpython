def sed(pattern_string, repl_string, input_file, output_file):
    """Reads input_file, writes output_file, replacing any occurrences of
    pattern_string with repl_string"""
    try:
        fin = open(input_file)
    except:
        print('Invalid input file given')
        return
    
    try:
        fout = open(output_file, 'w')
    except:
        print('Unable to open output file')
        return

    for line in fin:
        if pattern_string in line:
            line = line.replace(pattern_string, repl_string)
        fout.write(line)

    try:
        fin.close()
    except:
        print('Error closing input file')
        return
        
    try:
        fout.close()
    except:
        print('Error closing output file')
        return
        
    
