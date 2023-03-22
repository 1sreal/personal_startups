#include <iostream>
using namespace std;
int main () {
	float gal_per_3foot = 7.485 ;  
	float gals; 
	cout << "Enter the number of gallons to be converted to feet "<<		endl;
	cin >> gals ;
	float gal_in_feet = (gal_per_3foot * gals);
	cout << gals << " gallons equals " << gal_in_feet << " ft" <<  endl;
	return 0;    