/*2048�C��*/
#include <stdio.h>
#include <memory.h>
#include <stdlib.h>
#include <time.h>
#include<conio.h>
#define MAX 4
int num = 0;         //���ʦ���
int times = 0;       //�C������
int map[MAX][MAX] = { 0 }, history_str[MAX][MAX] = { 0 }; // �C���Ʀr�y�а}�C & ���v�̰��Ʀr
void re();  //���ư��檺�Ƶ{��

/*��l�ƼƲ�*/
void init(){
	memset(map, 0, sizeof(map));
}
/*�b�Y�@�ӪŪ���m�Ы��H���� & ��{�C���O�_����*/
void CreateRandNumber()
{
	int flag = 0, pos = 0;
	int str[MAX][MAX] = { 0 };
	int x, y, i, j, row, col;
	int r[MAX*MAX];
	int c[MAX*MAX];
	int k = 0,l;

	/*�P�_���Ǧ�m�i��*/
	for (row = 0; row<MAX; row++)
	{
		for (col = 0; col<MAX; col++)
		{
			if (map[row][col] == 0)  //�Ymap[row][col]���šA�̦��s�J:
			{                        //k = 0 �� map[r][c] �B
				r[k] = row;          //k = 1 �� map[r][c] ...
				c[k] = col;          //...�H������
				k++;
			}
		}
	}
	/*�p�G�S�Ů�i�H�Ы��H���ܼơA����U�C�{��*/
	if (k == 0)
	{    /*��Ҧ��۾F�ƬҤ��۵��ɡA�C������(GAME OVER)*/
		if ((map[0][0] != map[0][1]) && (map[0][0] != map[1][0]) && (map[0][1] != map[0][2]) && (map[0][1] != map[1][1]) && (map[0][2] != map[0][3]) && (map[0][2] != map[1][2]) && (map[0][3] != map[1][3]) &&
			(map[1][0] != map[1][1]) && (map[1][0] != map[2][0]) && (map[1][1] != map[1][2]) && (map[1][1] != map[2][1]) && (map[1][2] != map[1][3]) && (map[1][2] != map[2][2]) && (map[1][3] != map[2][3]) &&
			(map[2][0] != map[2][1]) && (map[2][0] != map[3][0]) && (map[2][1] != map[2][2]) && (map[2][1] != map[3][1]) && (map[2][2] != map[2][3]) && (map[2][2] != map[3][2]) && (map[2][3] != map[3][3]) &&
			(map[3][0] != map[3][1]) && (map[3][1] != map[3][2]) && (map[3][2] != map[3][3])  //��{�Ҧ��۾F�ƬO�_�Ҥ��۵�
			){
			for (i = 0; i < 4; i++){
				for (j = 0; j < 4; j++){
					if (str[MAX][MAX] < map[i][j]){
						str[MAX][MAX] = map[i][j]; //�p�⥻���̰��Ʀr
					}
				}
			}
			if (str[MAX][MAX] > history_str[MAX][MAX]){
				history_str[MAX][MAX] = str[MAX][MAX];  //��{�����̰��Ʀr�O�_�����v�̰��Ʀr�C�Y�O�A�h���N
			}
			printf("\n");   //�N...��� GAME OVER ��...
			printf("�@�������@�@���@�@���@���@�������@�@�������@���@���@�������@������\n");
			printf("�@���@�@�@���@���@�������@���@�@�@�@���@���@���@���@���@�@�@���@��\n");
			printf("�@���@���@�������@���@���@�������@�@���@���@���@���@�������@������\n");
			printf("�@���@���@���@���@���@���@���@�@�@�@���@���@���@���@���@�@�@�����@\n");
			printf("�@�������@���@���@���@���@�������@�@�������@�@���@�@�������@���@��\n");
			printf("\n\n\t     �̰����ʦ��ơG%d\n\t     �����̰��Ʀr�G%d\n\t     ���v�̰��Ʀr�G%d\n\tENTER���s�}�l�C���AESC���}�C��\n\n", num - 1, str[MAX][MAX], history_str[MAX][MAX]);
		}
		/*���M���۾F�ƦC�۵��A�����ʿ��~�A�h����ܲ��ʵL�Ĵ���*/
		else  printf("\n\n\t  �����ʵL��(�w����%d��)\a\n", num - 1);
	}
	/*�p�G���Ů�i�H�Ы��H���ܼơA����U�C�{��*/
	else {
		printf("\n");
		srand(time(0));
		pos = rand() % k;  //�H����ܪŮ��
		x = r[pos];
		y = c[pos];
		l = rand() % 10;
		if (l == 0)map[x][y] = 4;
		else map[x][y] = 2;    //�q�Ū���m�����ͤ@���H����2��4
		num++;                               //�W�[���ʦ���
		if (num != 1)printf("\n\t        ���ʲ�%d��\n", num - 1);  //�̶}�l���L�X���ʦ���
		else printf("\n\n");
	}
}
/*��ܹC�����*/
void show_map()
{
	int loop = 0, row, col;


	for (row = 0; row<4; row++){
		if (loop == 0){
			printf("\t��������������������������\n"); //���W���
		}
		else {
			printf("\t��������������������������\n"); //��椤���
		}

		loop++;

		for (col = 0; col<4; col++)
		{
			if (col == 0)printf("\t��");          //�̥��䪺�@�ƽݮ�
			if (map[row][col] == 0){              // map[row][col]���S������ơA�u�L�X�ݮ�
				printf("�@�@��");
			}
			else{                                 // map[row][col]�����ơA�L�X�Ʀr�M�ݮ�
				printf("%-4d��", map[row][col]);
			}
		}
		printf("\n");
	}
	printf("\t��������������������������"); //���U���
	if (num == 1 && times == 0){ printf("\n\t��JENTER�h���s�}�l�s�C��"); }
}
/*�V������*/
void toward_left()
{
	int loop, i, j;

	for (loop = 0; loop<4; loop++)
	{
		/*���ʼƦr*/
		for (i = 1; i <= 3; i++)
		{
			for (j = i; j>0; j--)
			{
				if (map[loop][j - 1] == 0)
				{
					map[loop][j - 1] = map[loop][j];
					map[loop][j] = 0;
				}
			}
		}
		/*�X�֬ۦP�Ʀr*/
		for (i = 1; i <= 3; i++)
		{
			if ((map[loop][i] == map[loop][i - 1]) && (map[loop][i - 1] != 0))
			{
				map[loop][i - 1] = 2 * map[loop][i - 1];
				map[loop][i] = 0;
			}
		}
		/*���ʼƦr*/
		for (i = 1; i <= 3; i++)
		{
			for (j = i; j>0; j--)
			{
				if (map[loop][j - 1] == 0)
				{
					map[loop][j - 1] = map[loop][j];
					map[loop][j] = 0;
				}
			}
		}

	}
}
/*�V�W����*/
void toward_up()
{
	int loop, i, j;

	for (loop = 0; loop<4; loop++)
	{
		//���ʼƦr
		for (i = 1; i <= 3; i++)
		{
			for (j = i; j>0; j--)
			{
				if (map[j - 1][loop] == 0)
				{
					map[j - 1][loop] = map[j][loop];
					map[j][loop] = 0;
				}
			}
		}
		//�X�֬ۦP�Ʀr
		for (i = 1; i <= 3; i++)
		{
			if ((map[i - 1][loop] == map[i][loop]) && (map[i - 1][loop] != 0))
			{
				map[i - 1][loop] *= 2;
				map[i][loop] = 0;
			}
		}
		//���ʼƦr
		for (i = 1; i <= 3; i++)
		{
			for (j = i; j>0; j--)
			{
				if (map[j - 1][loop] == 0)
				{
					map[j - 1][loop] = map[j][loop];
					map[j][loop] = 0;
				}
			}
		}

	}
}
/*�V�U����*/
void toward_down()
{
	int loop, i, j;

	for (loop = 0; loop<4; loop++)
	{
		//���ʼƦr
		for (i = 3; i>0; i--)
		{
			for (j = i; j <= 3; j++)
			{
				if (map[j][loop] == 0)
				{
					map[j][loop] = map[j - 1][loop];
					map[j - 1][loop] = 0;
				}
			}
		}
		//�X�֬ۦP�Ʀr
		for (i = 3; i>0; i--)
		{
			if ((map[i][loop] == map[i - 1][loop]) && (map[i][loop] != 0))
			{
				map[i][loop] *= 2;
				map[i - 1][loop] = 0;
			}
		}
		//���ʼƦr
		for (i = 3; i>0; i--)
		{
			for (j = i; j <= 3; j++)
			{
				if (map[j][loop] == 0)
				{
					map[j][loop] = map[j - 1][loop];
					map[j - 1][loop] = 0;
				}
			}
		}

	}
}
/*�V�k����*/
void toward_right()
{
	int loop, i, j;

	for (loop = 0; loop<4; loop++)//�|��
	{
		//���ʼƦr
		i = 2;
		while (i >= 0)
		{
			for (j = i; j<3; j++)
			{
				if (map[loop][j + 1] == 0)
				{
					map[loop][j + 1] = map[loop][j];
					map[loop][j] = 0;
				}
			}
			i--;
		}
		//�X�֬ۦP�Ʀr
		for (i = 2; i >= 0; i--)
		{
			if ((map[loop][i + 1] == map[loop][i]) && (map[loop][i + 1] != 0))
			{
				map[loop][i + 1] = 2 * map[loop][i + 1];
				map[loop][i] = 0;
			}
		}
		//���ʼƦr
		i = 2;
		while (i >= 0)
		{
			for (j = i; j<3; j++)
			{
				if (map[loop][j + 1] == 0)
				{
					map[loop][j + 1] = map[loop][j];
					map[loop][j] = 0;
				}
			}
			i--;
		}

	}
}
/*�}�l�C��*/
void play()
{
	unsigned char key;
	while (1){
		key = getch();
		if (key == 27)break;
		if (key == 13 || times != 0){
			system("cls");                                                               //�M�����e���
			printf("\n\n          �ϥΡ���������ާ@�C��\n");
			show_map();                                                                  //�L�X�Ʀr�M���

			while (1){
				key = getch();                                                           //��J����
				if (key == 27)break;                                                     //��JESC�h���}�C��
				if (key == 13){                                                          //��JENTER�h���s�}�l�s�C��
					printf("\n\t�}�l�s�C���A�����N���~��");
					num = 0;
					times++;
					re();
					break;
				}
				if (key == 0 || key == 0xE0){
					system("cls");                                                       //�M�����e���
					key = getch();                                                       //��J����
					switch (key){
					case 72:toward_up();    CreateRandNumber(); show_map(); break;   //�V�W
					case 80:toward_down();  CreateRandNumber(); show_map(); break;   //�V�U
					case 75:toward_left();  CreateRandNumber(); show_map(); break;   //�V��
					case 77:toward_right(); CreateRandNumber(); show_map(); break;   //�V�k
					default:  break;
					}
				}
			}
			break;
		}
	}
}
/*���ư���*/
void re(){
	if (times == 0)printf("\n\n\t         �Ы�ENTER�}�l");
	init();              //��l�ƼƲ�
	CreateRandNumber();  //�b�Ů�إ��H���ܼ�
	play();              //�}�l�C��
}
/*�D�{��*/
int main()
{
	printf("\n");  //�o...��...�N�L�X2048��
	printf("�@�@�@�������@�@�������@�@���@���@�@������\n");
	printf("�@�@�@�@�@���@�@���@���@�@���@���@�@���@��\n");
	printf("�@�@�@�������@�@���@���@�@�������@�@������\n");
	printf("�@�@�@���@�@�@�@���@���@�@�@�@���@�@���@��\n");
	printf("�@�@�@�������@�@�������@�@�@�@���@�@������\n");
	printf("\n\n\       �C���ާ@�覡�G�ϥΡ���������ާ@�C��\n");
	re();
	printf("\n\n\t�C���Y�N�����A");
	system("pause");
	return 0;
}