#landing script
#options to load in datasets
#display help to choose:
#file locations
#formatting options

#if __name__ == "__main__":
#    parser = OptionParser()
#    parser.add_option("-d", "--dir", dest="pwd", default="../data_files/")
#    parser.add_option("-m", "--maps", dest="maps")
#    parser.add_option("-p", "--pulse", dest="pulse")
    #parser.add_option("-e", "--end", dest="end")
    #parser.add_option("-n", "--normalize", dest="normalize",
    #                  action="store_true", default=False)
#    parser.add_option("-t", "--tempfile", dest="use_tempfile",
#                      action="store_true", default=False)
#    (options, args) = parser.parse_args()
#    if len(args) not in [1, 2]:
#        print ("Incorrect arguments")
#        print (__doc__)
#        sys.exit()
#    kwargs = dict(
#        pwd=options.pwd,
#        maps=options.maps,# or 'all',
#        pulse=options.pulse,# or 0,
        #end=options.end,
        #normalize=options.normalize,
#        use_tempfile=options.use_tempfile)
#    main(*args, **kwargs)

from argparse import ArgumentParser
import sys

parser = ArgumentParser(
	prog="catchy name",#name of program to be displayed in the help msg
	description="sRNA target hybridization. Please make sure that the MAPS and the PULSE datasets are in the following format:",#description
	epilog="",)#final msg to be displayed, if anything
	
params = parser.add_argument_group("parameters")
params.add_argument(
    "-d", "--path",
    #nargs="?",
    default="../data_files/",
    #metavar=("X", "Y"),#to add as help/usage what possible values can be selected
    help="path to the data files (default: %(default)s)",
)
params.add_argument("-m", "--maps", nargs="*", 
    help="MAPS input data, accepts multiple datasets")
params.add_argument("-p", "--pulse", nargs="*",
    help="PULSE input data, accepts multiple datasets")
params.add_argument("-ril", "--rilseq",
    help="RILSeq input data, accepts multiple datasets")
params.add_argument("-x",
    help="Future: other datasets")
params.add_argument("-i", "--intarna", action="store_false",
    help="hybridization using intaRNA")

params.add_argument(
    "--version", action="version", version="%(prog)s 0.1")
    
args = parser.parse_args()

#print(args)

def query(question, default=None):
    valid = {"yes": True, "y": True, "Y": True, "no": False, "n": False, "N": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)
        
    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if default is not None and choice == "":
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Y/y/yes " "or 'y' or 'N/n/no'.\n")
    
query("Do you want to proceed?")
