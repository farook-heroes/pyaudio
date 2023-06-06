import java.util.*;


class obj
{
    int name;
    int val;
    static int n;
    static {
        n = 0;
        System.out.println("hello static");
    }
    obj()    
    {
        name=0;
        val=0;
        n=1;
        System.out.println("hello con");
    }
    public int getName() {
        return name;
    }
    public int getVal() {
        return val;
    }
    public static int getN() {
        return n;
    }
    public void setName(int name) {
        this.name = name;
    }
    public void setVal(int val) {
        this.val = val;
    }
    public static void setN(int n) {
        obj.n = n;
    }
}


class Hello
{
    public static void main(String args[]) throws ClassNotFoundException
    {
        Class.forName("obj");
        // obj o1=new obj();
        // obj o2=new obj();
    }  
}