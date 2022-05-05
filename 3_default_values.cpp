// 2_default_values.cpp
// C++ automatically initializes from defaults
// Tested on http://cpp.sh
#include <iostream>

class A {
    public:
    int x = 100;
    int y = 200;
    int z = 300;
};

class B {
    public:
    static int x;
    static int y;
    static int z;
};

// Static variables must be initialized outside the class:
int B::x = 100;
int B::y = 200;
int B::z = 300;

// Static consts are initialized inline:
class C {
    public:
    static const int x = 100;
    static const int y = 200;
    static const int z = 300;
};

class D {
    public:
    static const int x = 100;
    // Cannot shadow identifier names:
    // int x = 1; // 'int D::x' conflicts with a previous declaration
};


int main() {
    A a;
    std::cout << a.x << ", " << a.y << ", " << a.z << std::endl;
    a.x = -1;
    a.y = -2;
    a.z = -3;
    std::cout << a.x << ", " << a.y << ", " << a.z << std::endl;

    B b;
    std::cout << b.x << ", " << b.y << ", " << b.z << std::endl;
    // Accessing statics via instance:
    b.x = -1;
    b.y = -2;
    b.z = -3;
    std::cout << b.x << ", " << b.y << ", " << b.z << std::endl;

    C c;
    std::cout << c.x << ", " << c.y << ", " << c.z << std::endl;
    // Cannot assign to const:
    // c.x = -1;
    // c.y = -2;
    // c.z = -3;
}
/*
100, 200, 300
-1, -2, -3
100, 200, 300
-1, -2, -3
100, 200, 300
*/
