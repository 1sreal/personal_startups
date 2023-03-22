#include <iostream> 
using namespace std; 

long hms_to_sec(int hours, int minutes, int seconds)
{ 
  long total_seconds = (hours * 3600) + (minutes * 60) + seconds;
  return total_seconds;
}

int main()
{ 
  int hours, minutes, seconds;
  long total_seconds;
  
  while (true) 
  {
    cout << "Enter the time in the format HH:MM:SS" << endl;
    cin >> hours >> minutes >> seconds;

    cout << "Time inputted: " << hours << ":" << minutes << ":" << seconds << endl;
    
    total_seconds = hms_to_sec(hours, minutes, seconds);
    cout << "Total time in seconds: " << total_seconds << endl;
  }

  return 0;
}
