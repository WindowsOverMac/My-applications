#include <iostream>
#include <algorithm>
using namespace std;

int main() 
{
  string response;
    cout << "Want to hear a fun fact?";
    std::cin >> response;
     transform(response.begin(), response.end(), response.begin(), ::tolower);
    if (response =="yes"||response == "Yes"||response =="ye"||response == "Ye"||response == "sure"||response =="Sure"||response =="y"||response =="Y"){
    cout << "Undertale is an anagram of deltarune!"<< endl;
    } else{
      cout << "Okay, no fun fact told." << endl;
   } return 0;
}