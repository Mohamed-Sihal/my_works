import java.io.*;
import java.net.*;
public class Ceaser_Sender{
	public static void main(String args[]) throws Exception{
	
		Socket s=new Socket("localhost",6666);  
		DataOutputStream dout=new DataOutputStream(s.getOutputStream()); 
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));

		System.out.println("\nSender is Ready...");
		System.out.println("Enter the Plain Text");
		String str=(String)br.readLine();
		System.out.println("Enter the key value ");
		String ke=(String)br.readLine();
		int key=Integer.parseInt(ke);		

		System.out.println("Plain Text : "+str);
		System.out.println("Key : "+key);
		
		String encryptstr=" ";
		char ch;
		for(int i = 0; i < str.length(); ++i)
		{
		ch = str.charAt(i);
			
		if(ch >= 'a' && ch <= 'z')
		{
			ch = (char)(ch + key);
	        if(ch > 'z')
			{
	        	ch = (char)(ch - 'z' + 'a' - 1);
			}
			encryptstr += ch;
		}
			
	        else if(ch >= 'A' && ch <= 'Z')
			{
	            ch = (char)(ch + key);
	           	if(ch > 'Z')
					{
						ch = (char)(ch - 'Z' + 'A' - 1);
					}
	            	encryptstr += ch;
	       	}
	        else
		 	{
	        	encryptstr += ch;
	        }
		}
		System.out.println("Encrypted(Cipher) Text is : "+encryptstr);
		//String key1=Integer.toString(key);
		//dout.writeUTF(key1);
		dout.writeUTF(encryptstr);
		
		System.out.println("Cipher Text and key has been sent to the receiver.");
		s.close();
		dout.close();

}
}
	