#ifndef RATIONAL_H
#define RATIONAL_H

#include <iostream>

//This class always represents a number of the Rational set of numbers, expressed as a ratio
//of two integers.

class Rational{
private:
    long n;  //numerator
    long d;  //demonimator

    Rational();

public:


    Rational(int, int);
        //initializes Numerator and Denominator to the values first and second arguments
        //respectively, throws exception if Denominator is zero

    void setNumerator(int);
        //Sets the numerator of the Rational to the value of the arguments

    void setDenominator(int);
        //Sets the denominator of the Rational to the value of the argument, throws exception if Denominator is zero

    void set(int, int);
        //takes two ints to set the Numerator and Denominator of the Rational
        //throws exception if Denominator is zero

    int getNumerator() const;
        //gets the numerator

    int getDenominator() const;
        //gets the denominator

    void reduce();
        //reduces the ratio of the Rational to simplest form


    void operator=(const Rational&);
        //sets one Rational to another Rational's value


};

//OPERATIONS OF TWO RATIONALS

Rational operator+(const Rational&, const Rational&);
//adds two Rationals

Rational operator-(const Rational&, const Rational&);
//subtracts two Rationals

Rational operator*(const Rational&, const Rational&);
//multiplies two Rationals

Rational operator/(const Rational&, const Rational&);
//Divides one Rational by another

bool operator==(const Rational&, const Rational&);
//compares two Rationals

bool operator<=(const Rational&, const Rational&);
//compares two Rationals for less than or equals to

bool operator>=(const Rational&, const Rational&);
//compares two Rationals for greater than or equals to

bool operator<(const Rational&, const Rational&);
//compares two Rationals for less than

bool operator>(const Rational&, const Rational&);
//compares two  Rationals for greater than


//OPERATIONS OF A RATIONAL AND AN INTEGER

Rational operator+(const Rational&, int);
//adds and integer to a Rational

Rational operator-(const Rational&, int);
//subtracts an integer from a Rational

Rational operator*(const Rational&, int);
//multiplies a Rational by an integer

bool operator==(const Rational&, int);
//compare a Rational and an integer for equality

bool operator<=(const Rational&, int);
//compares a Rational and an integer for less than or equals

bool operator>=(const Rational&, int);
//compares a Rational and an integer for greater than or equals

bool operator<(const Rational&, int);
//compares a Rational and an integer for less than

bool operator>(const Rational&, int);
//compares a Rational and an integer for greater than

std::ostream& operator<<(std::ostream&, const Rational&);
//puts a simplified representation of the Rational into the output stream

//Greatest common divisor function for reduce;
int gcd(int a, int b);
//returns

#endif
