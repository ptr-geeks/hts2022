#include <stdio.h>
#include <stdbool.h>

//unsigned char f[55] = "Reverse engineering seems to be too much for this camp";
unsigned char f[55] = {0x42, 0xBF, 0xBB, 0x3F, 0xD1, 0x2A, 0xC6, 0x60, 0x17, 0xBF, 0x0C, 0xD5, 0xBF, 0x6E, 0xCA, 0xAE, 0xB5, 0x93, 0x7A, 0x90, 0x57, 0x43, 0x3E, 0x1F, 0x15, 0xEB, 0x33, 0x42, 0x49, 0xB5, 0x29, 0x35, 0xDA, 0x16, 0x4A, 0x7B, 0xBB, 0x3A, 0x3C, 0xDC, 0x83, 0x47, 0xC7, 0x9C, 0x98, 0x85, 0x55, 0x3C, 0x65, 0x68, 0x26, 0xB1, 0x12, 0xF1, 0x00};
char* key1 = "Poletn1";
char* key2 = "Tab0r";
int shift1 = 3;
int shift2 = 6;

void crypt(unsigned char* in, unsigned char* out, char* key, int shift, int n, int keyn)
{
	bool rev = false;
	if (shift < 0)
	{
		shift = -shift;
		rev = true;
	}

	for (int i = 0; i < n; i++)
	{
		unsigned char c = in[i];
		if (rev)
		{
			c = (c ^ key[i % keyn]) & 0xFF;
			c = ((c >> shift) & 0xFF) | ((c << (8-shift)) & 0xFF);
		}
		else
		{
			c = ((c << shift) & 0xFF) | ((c >> (8-shift)) & 0xFF);
			c = (c ^ key[i % keyn]) & 0xFF;
		}
		out[i] = c;
	}
}

int main()
{
	unsigned char outf[55] = { 0 };
	unsigned char in[55] = { 0 };
	unsigned char outin[55] = { 0 };

	crypt(f, outf, key1, shift2, 54, 7);

	fgets(in, 55, stdin);
	crypt(in, outin, key2, -shift1, 54, 5);

	for (int i = 0; i < 54; i++)
	{
		if (outin[i] != outf[i])
		{
			printf(":(\n");
			return 0;
		}
	}

	printf("gg ez\n");

	return 0;	
}
