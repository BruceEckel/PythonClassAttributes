// 2_default_values.cpp
// C++ automatically initializes from defaults
// Tested on http://cpp.sh
#include <iostream>

class A {
    public:
    int x = 100;
};

class B {
    public:
    static int x;
};

// Static variables must be initialized outside the class:
int B::x = 100;

// Static consts are initialized inline:
class C {
    public:
    static const int x = 100;
};

class D {
    public:
    static const int x = 100;
    // Cannot shadow identifier names:
    // int x = 1; // 'int D::x' conflicts with a previous declaration
};


int main() {
    A a;
    std::cout << a.x << std::endl;
    a.x = -1;
    std::cout << a.x << std::endl;

    B b;
    std::cout << b.x << std::endl;
    // Accessing statics via instance:
    b.x = -1;
    std::cout << b.x << std::endl;

    C c;
    std::cout << c.x << std::endl;
    // Cannot assign to const:
    // c.x = -1;
}
/*
100
-1
100
-1
100
*/
