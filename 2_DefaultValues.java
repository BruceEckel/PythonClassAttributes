// DefaultValues.java
// Java automatically initializes from defaults
class A {
    int x = 100;
    public A() {
        // x is already initialized:
        System.out.println("In A constructor: " + this);
    }
    @Override
    public String toString() {
        return "x = " + x;
    }
}

class B {
    static int x = 100;
    @Override
    public String toString() {
        // Accessing static via instance:
        return "x = " + x;
        // Same as Integer.toString(this.x)
    }
    static public String statics() {
        return "B.statics(): B.x = " + B.x;
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
        System.out.println("a: " + a);

        B b = new B();
        System.out.println("b: " + b);
        System.out.println(B.statics());
        // Accessing static via instance:
        b.x = -1;
        System.out.println("b: " + b);
        System.out.println(B.statics());
        B b2 = new B();
        System.out.println("b2: " + b2);
    }
}
/*
In A constructor: x = 100
a: x = 100
a: x = -1
b: x = 100
B.statics(): B.x = 100
b: x = -1
B.statics(): B.x = -1
b2: x = -1
*/
