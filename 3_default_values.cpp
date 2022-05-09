// 3_default_values.cpp
// C++ automatically initializes from defaults
// Tested on http://cpp.sh
#include <iostream>

class A {
    public:
    int x = 100;
    A() { // x is already initialized:
        std::cout << "constructor: " << x << std::endl;
    }
};

class B {
    public:
    static int x;
    // Cannot shadow identifier name:
    // int x = 1;
    // 'int B::x' conflicts with a previous declaration
};

// Static variables must be initialized outside the class:
int B::x = 100;

// Static consts are initialized inline:
class C {
    public:
    static const int x = 100;
};

int main() {
    A a;
    // constructor: 100
    std::cout << a.x << std::endl;
    // 100
    a.x = -1;
    std::cout << a.x << std::endl;
    // -1

    B b;
    std::cout << b.x << std::endl;
    // 100
    // Accessing static via instance:
    b.x = -1;
    std::cout << b.x << std::endl;
    // -1
    // Accessing static via class:
    B::x = -99;
    std::cout << b.x << std::endl;
    // -99

    C c;
    std::cout << c.x << std::endl;
    // 100
    // Cannot assign to const:
    // c.x = -1;
}