class A:
    x = 100
    y = 200
    z = 300


if __name__ == '__main__':
    a = A()
    print(f"{a.x = }, {a.y = }, {a.z = }")
    a.x = -1
    a.y = -2
    a.z = -3
    print(f"{a.x = }, {a.y = }, {a.z = }")

"""
// C++ automatically initializes from defaults
#include <iostream>
#include <string>

class A {
    public:
    int x = 100;
    int y = 200;
    int z = 300;
};


int main() {
    A a = A();
    std::cout << a.x << ", " << a.y << ", " << a.z << std::endl;
    a.x = -1;
    a.y = -2;
    a.z = -3;
    std::cout << a.x << ", " << a.y << ", " << a.z << std::endl;
}
/*
100, 200, 300
-1, -2, -3
*/
"""
