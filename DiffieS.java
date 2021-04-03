import java.net.*;
import java.io.*;
import java.util.*;

public class DiffieS {
    static long q;

    public static boolean isprime(long num) {
        for (long i = 2; i < num; i++) {
            if (num % i == 0)
                return false;
        }
        return true;
    }

    public static long power(long base, long exp) {
        long t = 1L;
        while (exp > 0) {
            if (exp % 2 != 0)
                t = (t * base) % q;
            base = (base * base) % q;
            exp /= 2;
        }
        return t % q;
    }

    public static void main(String args[]) {
        try {
            Socket s = new Socket("localhost", 6666);
            DataOutputStream dout = new DataOutputStream(s.getOutputStream());
            BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
            Scanner sc = new Scanner(System.in);
            DataInputStream din = new DataInputStream(s.getInputStream());

            System.out.println("Enter P and primitive root(G) : ");
            q = sc.nextLong();
            long a = sc.nextLong();
            if (!isprime(q)) {
                System.out.println("enter a prime number");
                q = sc.nextLong();
            }
            System.out.println("Enter Private key for A : ");
            long Xa = sc.nextLong();
            long Ya = power(a, Xa);
            System.out.println("A's Public Key: " + Ya);
            dout.writeLong(Ya);
            dout.writeLong(q);
            dout.writeLong(a);
            long Yb = din.readLong();
            long k = power(Yb, Xa);
            System.out.println("Computed Symmetric key : " + k);
            long bk = din.readLong();
            if (k == bk)
                System.out.println("Shared Secret key : " + k);

        } catch (Exception e) {
            System.out.println(e);
        }
    }

}
