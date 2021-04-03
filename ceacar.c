int main()
{
	char plain[100], ch;
	int i, key;
	printf("Enter plain text: ");
	gets(plain);
	printf("Enter key: ");
	scanf("%d", &key);
	for(i = 0; plain[i] != '\0'; i++)
    {
		ch = plain[i];
		if(ch >= 'a' && ch <= 'z')
        {
			ch = ch + key;
			if(ch > 'z')
            {
				ch = ch - 'z' + 'a' - 1;
			}
			plain[i] = ch;
		}
		else if(ch >= 'A' && ch <= 'Z'){
			ch = ch + key;
			if(ch > 'Z'){
				ch = ch - 'Z' + 'A' - 1;
			}
			plain[i] = ch;
		}
	}
	
	printf("Encrypted plain text : %s", plain);
	
	return 0;
}