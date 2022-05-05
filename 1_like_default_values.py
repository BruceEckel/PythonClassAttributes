class A:
    x = 100
    y = 200
    z = 300

if __name__ == '__main__':
    a = A()
    print(f"{a.x = }, {a.y = }, {a.z = }")
    # a.x = 100, a.y = 200, a.z = 300
    a.x = -1
    a.y = -2
    a.z = -3
    print(f"{a.x = }, {a.y = }, {a.z = }")
    # a.x = -1, a.y = -2, a.z = -3

"""
// Java automatically initializes from defaults

class A {
    int x = 100;
    int y = 200;
    int z = 300;
    @Override public String toString() {
        return x + ", " + y + ", " + z;
    }
}

public class DefaultValues {
    public static void main(String []args){
        A a = new A();
        System.out.println(a);
        a.x = -1;
        a.y = -2;
        a.z = -3;
        System.out.println(a);
    }
}
/*
100, 200, 300
-1, -2, -3
*/
"""
