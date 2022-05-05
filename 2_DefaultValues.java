// DefaultValues.java
// Java automatically initializes from defaults
class A {
    int x = 100;
    int y = 200;
    int z = 300;
    public A() {
        // x, y, and z are already initialized:
        System.out.println("In A constructor: " + this);
    }
    @Override
    public String toString() {
        return x + ", " + y + ", " + z;
    }
}

class B {
    static int x = 100;
    static int y = 200;
    static int z = 300;
    @Override
    public String toString() {
        // Accessing statics via instance:
        return x + ", " + y + ", " + z;
        // (Same as this.x, this.y, this.z)
    }
    static public String statics() {
        return "B.statics(): " + B.x + ", " + B.y + ", " + B.z;
    }
}

class C {
    static int x = 100;
    // Cannot shadow identifier names:
    // int x = -1; // Variable 'x' is already defined in the scope
}

public class DefaultValues {
    public static void main(String[] args) {
        A a = new A();
        System.out.println("a: " + a);
        a.x = -1;
        a.y = -2;
        a.z = -3;
        System.out.println("a: " + a);

        B b = new B();
        System.out.println("b: " + b);
        System.out.println(B.statics());
        // Accessing statics via instance:
        b.x = -1;
        b.y = -2;
        b.z = -3;
        System.out.println("b: " + b);
        System.out.println(B.statics());
        B b2 = new B();
        System.out.println("b2: " + b2);
    }
}
/*
In A constructor: 100, 200, 300
a: 100, 200, 300
a: -1, -2, -3
b: 100, 200, 300
B.statics(): 100, 200, 300
b: -1, -2, -3
B.statics(): -1, -2, -3
b2: -1, -2, -3
*/
