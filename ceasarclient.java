import java.io.DataOutputStream;
import java.net.Socket;
import java.io.*;
import java.util.Scanner;

class ceasarclient {
	public static final String ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
	public static final int shiftKey = 3;

	public static void main(String args[]) {
		String message, em;

		Scanner sc = new Scanner(System.in);

		try {

			Socket socket = new Socket("localhost", 5000);
			System.out.println("Connected with Server...");
			DataInputStream din = new DataInputStream(socket.getInputStream());
			DataOutputStream dout = new DataOutputStream(socket.getOutputStream());
			String cipherText = "";
			// cipherText=din.readLine();
			cipherText = (String) din.readUTF();
			System.out.println("Cipher Text received is :" + cipherText);
			String plainText = "";
			for (int i = 0; i < cipherText.length(); i++) {
				int charPosition = ALPHABET.indexOf(cipherText.charAt(i));
				int keyVal = (charPosition - shiftKey) % 26;
				if (keyVal < 0) {
					keyVal = ALPHABET.length() + keyVal;
				}
				char replaceVal = ALPHABET.charAt(keyVal);
				plainText += replaceVal;
			}
			System.out.println("PlainText is :" + plainText);
			dout.flush();
			dout.close();
			socket.close();
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
}
