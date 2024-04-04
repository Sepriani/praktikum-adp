#include <iostream>
#include <iomanip>

int main(){
	
	int totalDOR = 0;
    
	
		 
	for (int i = 1; i <= 100; i++) {
		
		if (i % 3 == 0) {
	
			std::cout << std::right << std::setw(4) << " DOR ";
			
			totalDOR++;
	
		} else if (i % 5 == 0) {
		    std::cout << std::right << std::setw(4) << " DOR ";
		    
		    totalDOR++;
			
		} else {
			
			std::cout << std::right << std::setw(4) << i << " ";
		}
		
		
		
    	if (i % 10 == 0) {
		
			std::cout << std::endl;
		}
		
	}
	
	std::cout << std::endl << "Total DOR yang muncul sebanyak = " << totalDOR << std::endl;
	
	// informasi pembuat program
	std::cout << std::endl <<
	"NAMA  : SEPRIANI"
	<< std::endl <<
    "NIM   : 2310432017"
    << std::endl <<
    "TUGAS : PERULANGAN DAN PENGKONDISIAN(4)"
    << std::endl <<
	"SHIFT : 4"
    << std::endl;
    
	return 0;
}