import java.net.*;
import java.io.*;
import java.util.*;
import java.math.*;

public class RsaR {
    static int gcd(int e, int z) {
        if (e == 0)
            return z;
        else
            return gcd(z % e, e);
    }

    public static void main(String args[]) {
        try {
            Socket s = new Socket("localhost", 6666);
            DataOutputStream dou = new DataOutputStream(s.getOutputStream());
            BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
            Scanner in = new Scanner(System.in);
            int p, q, n, tp, d = 0, e, i;
            System.out.println("Enter a number for encryption : ");
            int msg = in.nextInt();
            double c;

            System.out.println("Enter a prime Number for p : ");
            p = in.nextInt();
            System.out.println("Enter a prime Number for q : ");
            q = in.nextInt();
            n = p * q;
            tp = (p - 1) * (q - 1);
            System.out.println("Enter a prime Number for e : ");
            e = in.nextInt();

            while (e < tp) {
                if (gcd(e, tp) == 1) {
                    break;
                }
                e++;
            }

            for (i = 0; i <= 9; i++) {
                int x = 1 + (i * tp);

                if (x % e == 0) {
                    d = x / e;
                    break;
                }
            }
            c = (Math.pow(msg, e)) % n;
            System.out.println("Encrypted message is : " + c);
            dou.writeInt(n);
            dou.writeDouble(c);
            dou.writeInt(d);

        } catch (Exception e) {
            System.out.println(e);
        }
    }

}
