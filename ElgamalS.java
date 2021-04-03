import java.math.*;
import java.util.*;
import java.security.*;
import java.io.*;
import java.net.*;

public class ElgamalS {
    public static void main(String[] args) throws IOException {
        try {
            Socket s = new Socket("localhost", 6666);
            DataOutputStream dou = new DataOutputStream(s.getOutputStream());
            BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
            BigInteger p, b, c, secret;
            Random sc = new SecureRandom();
            Scanner in = new Scanner(System.in);
            secret = new BigInteger("12345678901234567890");

            System.out.println("secretKey = " + secret);
            p = BigInteger.probablePrime(64, sc);
            b = new BigInteger("3");
            c = b.modPow(secret, p);

            System.out.print("Enter your Big Number message -->");
            String str = in.nextLine();
            BigInteger X = new BigInteger(str);
            BigInteger r = new BigInteger(64, sc);
            BigInteger EC = X.multiply(c.modPow(r, p)).mod(p);
            BigInteger brmodp = b.modPow(r, p);
            dou.writeUTF(brmodp.toString());
            dou.writeUTF(secret.toString());
            dou.writeUTF(p.toString());
            dou.writeUTF(EC.toString());

        } catch (Exception e) {

        }

    }

}
