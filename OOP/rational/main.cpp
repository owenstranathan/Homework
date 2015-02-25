/*
THIS IS A PROGRAM TO DEMONSTRATE THE RATIONAL NUMBER CLASS
*/

#include "rational.hpp"
#include <iostream>
#include <vector>

using namespace std;

int main(){
  cout << "This program demonstrates the Rational number class\nauthored by Owen D. Stranathan, "
        << "as prompted by Dr. Sutton for OOP class.\n" << endl;

  cout << "Using overloaded '=' to set one Rational equal to the value of another" << endl;
  Rational r1(1,2);
  Rational r2(4,5);
  cout << "The first Rational is r1 = " << r1 << endl << "The second Rational is r2 = " << r2 << endl;

  cout << "Now I am setting the value of r1 to r2" << endl;
  r1=r2;
  cout << "r1 now equals "<< r1 << endl << endl;

  cout << "I will now add r1 and r2 together into r3 which should mean r3 = 8/5" << endl;
  Rational r3 = r1 + r2;
  cout << "r3 = " << r3 << endl << endl;

  cout << "Reseting r1 to 1/2" << endl << endl;
  r1.setNumerator(1);
  r1.setDenominator(2);

  r3 = r3 - r1;
  cout << "r3 = 8/5; r1 = 1/2"<< endl;
  cout <<"r3 - r1 = " << r3 << endl << endl;;

  r3 = r3 * r1;
  cout << "r3 = 11/10 and r1 = 1/2" << endl;
  cout << "r3 * r1 = " << r3 << endl<< endl;


  cout << "r3 = " << r3 <<" and r2 = " <<r2<< endl;
  r3 = r3 /r2;

  cout <<"r3 / r2 = " <<  r3 << endl << endl;

  r3.set(15,39); r2.set(15,26);
  cout << "r3 = " << r3 << "; r2 = " << r2 << endl;
  cout << "r3 == r2" << " : ";
  cout << (r3 ==r2 ? "True":"False") << endl;
  cout << "r3 <= r2" << " : ";
  cout << (r3 <=r2 ? "True":"False") << endl;
  cout << "r3 >= r2" << " : ";
  cout << (r3 >=r2 ? "True":"False") << endl;
  cout << "r3 > r2" << "  : ";
  cout << (r3 > r2 ? "True":"False") << endl;
  cout << "r3 < r2" << "  : ";
  cout << (r3 < r2 ? "True":"False") << endl;

  return 0;
}
