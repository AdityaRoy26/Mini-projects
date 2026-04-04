package bank;
class Account{
    public String name;
    protected String email;
    private String pswd;

    public String getPswd(){
        return this.pswd;
    }
    public void setPswd(String pass){
        this.pswd=pass;
    }
}
public class Bank {
    public static void main(String []args){
        Account account1=new Account();
        account1.name="Apna college";
        account1.email="aditya.roy2006@gmail.com";
        account1.setPswd("234324");
        System.out.println(account1.getPswd());
    }
}
