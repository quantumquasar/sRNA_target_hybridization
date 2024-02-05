from data_prep_initial import exec
from combine import start

#use argparse to specify and select for smoother running: 
#working dir
#where the MAPS + pulse data files are
#where intarna output files are

def main():
	print ("Starting data preprocessing...")
	exec()#should contain files
	print ("End of data preprocessing")
	print ("p value combination...")
	start()
	
if __name__ == "__main__":
	main()
