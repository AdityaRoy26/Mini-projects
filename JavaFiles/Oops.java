//POLYMORPHISM

// class Student{
//     String name;
//     int age;
//     public void printInfo(String name){
//     System.out.println(name);
//     }

//     public void printInfo(int age){
//     System.out.println(age);
//     }

//     public void printInfo(String name, int age){
//     System.out.println(name + " " + age);
//     }
// }

//INHERITANCE

// import bank.Bank;
// class Shape{
//     public void area(){
//         System.out.println("Displays area");
//     }
// }
// class Triangle extends Shape{
//     public void area(int l,int h){
//         System.out.println(1/2* l*h);
//     }
// }
// class EquiTriangle extends Triangle{
//     public void area(int l,int h){
//         System.out.println(1/2*l*h);
//     }
// }

// public class Oops{
//     public static void main(String[] args) {
//         Triangle t1=new Triangle(); 
//     }
// }

// ABSTRACT CLASS

abstract class Animal{
    public void walk(){

    }
}
class Horse extends Animal{
    public void walk(){
        System.out.println("walks on 4 legs");
    }
}
class Chicken extends Animal{
    public void walk(){
        System.out.println("walks on 2 legs");
    }
}
public class Oops{ 
    public static void main(String[] args){
    }
}