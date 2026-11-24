// Scratch probe: Gemmi 0.7.5 cif::is_numb acceptance for a token list (stdin, one per line).
#include <gemmi/numb.hpp>
#include <iostream>
int main(){ std::string s; while (std::getline(std::cin, s)) std::cout << s << "\t" << gemmi::cif::is_numb(s) << "\n"; }
