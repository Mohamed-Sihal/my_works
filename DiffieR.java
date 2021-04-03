import java.net.*;
import java.io.*;
import java.util.*;

public class DiffieR {
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
            ServerSocket ss = new ServerSocket(6666);
            Socket s = ss.accept();
            DataInputStream din = new DataInputStream(s.getInputStream());
            Scanner sc = new Scanner(System.in);
            DataOutputStream dout = new DataOutputStream(s.getOutputStream());

            long Ya = din.readLong();
            q = din.readLong();
            long a = din.readLong();
            System.out.println("Enter Private key for B : ");
            long Xb = sc.nextLong();
            long Yb = power(a, Xb);
            System.out.println("B's Public Key : " + Yb);
            dout.writeLong(Yb);
            long k = power(Ya, Xb);
            System.out.println("Shared Secret key: " + k);
            dout.writeLong(k);

        } catch (Exception e) {
            System.out.println(e);
        }
    }

}
