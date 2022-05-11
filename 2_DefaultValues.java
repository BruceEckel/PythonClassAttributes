// 2_DefaultValues.java
// Rename to DefaultValues.java
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
    // Same as "x = " + this.x;
  }
  static public String statics() {
    return "B.statics(): B.x = " + B.x;
  }
  // Cannot shadow identifier names:
  // int x = -1;
  // Variable 'x' is already defined in the scope
}

public class DefaultValues {
  public static void main(String[] args) {
    A a = new A();
    // In A constructor: x = 100
    System.out.println("a: " + a);
    // a: x = 100
    a.x = -1;
    System.out.println("a: " + a);
    // a: x = -1
    System.out.println("new A(): " + new A());
    // In A constructor: x = 100
    // new A(): x = 100

    B b = new B();
    System.out.println("b: " + b);
    // b: x = 100
    System.out.println(B.statics());
    // B.statics(): B.x = 100
    // Accessing static via class:
    B.x = -1;
    System.out.println("b: " + b);
    // b: x = -1
    System.out.println(B.statics());
    // B.statics(): B.x = -1
    B b2 = new B();
    System.out.println("b2: " + b2);
    // b2: x = -1
  }
}
