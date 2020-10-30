/*2048遊戲*/
#include <stdio.h>
#include <memory.h>
#include <stdlib.h>
#include <time.h>
#include<conio.h>
#define MAX 4
int num = 0;         //移動次數
int times = 0;       //遊戲次數
int map[MAX][MAX] = { 0 }, history_str[MAX][MAX] = { 0 }; // 遊戲數字座標陣列 & 歷史最高數字
void re();  //重複執行的副程式

/*初始化數組*/
void init(){
	memset(map, 0, sizeof(map));
}
/*在某一個空的位置創建隨機數 & 辨認遊戲是否結束*/
void CreateRandNumber()
{
	int flag = 0, pos = 0;
	int str[MAX][MAX] = { 0 };
	int x, y, i, j, row, col;
	int r[MAX*MAX];
	int c[MAX*MAX];
	int k = 0,l;

	/*判斷哪些位置可空*/
	for (row = 0; row<MAX; row++)
	{
		for (col = 0; col<MAX; col++)
		{
			if (map[row][col] == 0)  //若map[row][col]為空，依次存入:
			{                        //k = 0 → map[r][c] 、
				r[k] = row;          //k = 1 → map[r][c] ...
				c[k] = col;          //...以此類推
				k++;
			}
		}
	}
	/*如果沒空格可以創建隨機變數，執行下列程式*/
	if (k == 0)
	{    /*當所有相鄰數皆不相等時，遊戲結束(GAME OVER)*/
		if ((map[0][0] != map[0][1]) && (map[0][0] != map[1][0]) && (map[0][1] != map[0][2]) && (map[0][1] != map[1][1]) && (map[0][2] != map[0][3]) && (map[0][2] != map[1][2]) && (map[0][3] != map[1][3]) &&
			(map[1][0] != map[1][1]) && (map[1][0] != map[2][0]) && (map[1][1] != map[1][2]) && (map[1][1] != map[2][1]) && (map[1][2] != map[1][3]) && (map[1][2] != map[2][2]) && (map[1][3] != map[2][3]) &&
			(map[2][0] != map[2][1]) && (map[2][0] != map[3][0]) && (map[2][1] != map[2][2]) && (map[2][1] != map[3][1]) && (map[2][2] != map[2][3]) && (map[2][2] != map[3][2]) && (map[2][3] != map[3][3]) &&
			(map[3][0] != map[3][1]) && (map[3][1] != map[3][2]) && (map[3][2] != map[3][3])  //辨認所有相鄰數是否皆不相等
			){
			for (i = 0; i < 4; i++){
				for (j = 0; j < 4; j++){
					if (str[MAX][MAX] < map[i][j]){
						str[MAX][MAX] = map[i][j]; //計算本次最高數字
					}
				}
			}
			if (str[MAX][MAX] > history_str[MAX][MAX]){
				history_str[MAX][MAX] = str[MAX][MAX];  //辨認本次最高數字是否為歷史最高數字。若是，則取代
			}
			printf("\n");   //就...顯示 GAME OVER 啊...
			printf("　▓▓▓　　▓　　▓　▓　▓▓▓　　▓▓▓　▓　▓　▓▓▓　▓▓▓\n");
			printf("　▓　　　▓　▓　▓▓▓　▓　　　　▓　▓　▓　▓　▓　　　▓　▓\n");
			printf("　▓　▓　▓▓▓　▓　▓　▓▓▓　　▓　▓　▓　▓　▓▓▓　▓▓▓\n");
			printf("　▓　▓　▓　▓　▓　▓　▓　　　　▓　▓　▓　▓　▓　　　▓▓　\n");
			printf("　▓▓▓　▓　▓　▓　▓　▓▓▓　　▓▓▓　　▓　　▓▓▓　▓　▓\n");
			printf("\n\n\t     最高移動次數：%d\n\t     本次最高數字：%d\n\t     歷史最高數字：%d\n\tENTER重新開始遊戲，ESC離開遊戲\n\n", num - 1, str[MAX][MAX], history_str[MAX][MAX]);
		}
		/*仍然有相鄰數列相等，但移動錯誤，則僅顯示移動無效提示*/
		else  printf("\n\n\t  此移動無效(已移動%d次)\a\n", num - 1);
	}
	/*如果有空格可以創建隨機變數，執行下列程式*/
	else {
		printf("\n");
		srand(time(0));
		pos = rand() % k;  //隨機選擇空格位
		x = r[pos];
		y = c[pos];
		l = rand() % 10;
		if (l == 0)map[x][y] = 4;
		else map[x][y] = 2;    //從空的位置中產生一個隨機數2或4
		num++;                               //增加移動次數
		if (num != 1)printf("\n\t        移動第%d次\n", num - 1);  //最開始不印出移動次數
		else printf("\n\n");
	}
}
/*顯示遊戲表格*/
void show_map()
{
	int loop = 0, row, col;


	for (row = 0; row<4; row++){
		if (loop == 0){
			printf("\t╔══╦══╦══╦══╗\n"); //表格上橫框
		}
		else {
			printf("\t╠══╬══╬══╬══╣\n"); //表格中橫框
		}

		loop++;

		for (col = 0; col<4; col++)
		{
			if (col == 0)printf("\t║");          //最左邊的一排豎框
			if (map[row][col] == 0){              // map[row][col]內沒有任何數，只印出豎框
				printf("　　║");
			}
			else{                                 // map[row][col]內有數，印出數字和豎框
				printf("%-4d║", map[row][col]);
			}
		}
		printf("\n");
	}
	printf("\t╚══╩══╩══╩══╝"); //表格下橫框
	if (num == 1 && times == 0){ printf("\n\t輸入ENTER則重新開始新遊戲"); }
}
/*向左移動*/
void toward_left()
{
	int loop, i, j;

	for (loop = 0; loop<4; loop++)
	{
		/*移動數字*/
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
		/*合併相同數字*/
		for (i = 1; i <= 3; i++)
		{
			if ((map[loop][i] == map[loop][i - 1]) && (map[loop][i - 1] != 0))
			{
				map[loop][i - 1] = 2 * map[loop][i - 1];
				map[loop][i] = 0;
			}
		}
		/*移動數字*/
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
/*向上移動*/
void toward_up()
{
	int loop, i, j;

	for (loop = 0; loop<4; loop++)
	{
		//移動數字
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
		//合併相同數字
		for (i = 1; i <= 3; i++)
		{
			if ((map[i - 1][loop] == map[i][loop]) && (map[i - 1][loop] != 0))
			{
				map[i - 1][loop] *= 2;
				map[i][loop] = 0;
			}
		}
		//移動數字
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
/*向下移動*/
void toward_down()
{
	int loop, i, j;

	for (loop = 0; loop<4; loop++)
	{
		//移動數字
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
		//合併相同數字
		for (i = 3; i>0; i--)
		{
			if ((map[i][loop] == map[i - 1][loop]) && (map[i][loop] != 0))
			{
				map[i][loop] *= 2;
				map[i - 1][loop] = 0;
			}
		}
		//移動數字
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
/*向右移動*/
void toward_right()
{
	int loop, i, j;

	for (loop = 0; loop<4; loop++)//四排
	{
		//移動數字
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
		//合併相同數字
		for (i = 2; i >= 0; i--)
		{
			if ((map[loop][i + 1] == map[loop][i]) && (map[loop][i + 1] != 0))
			{
				map[loop][i + 1] = 2 * map[loop][i + 1];
				map[loop][i] = 0;
			}
		}
		//移動數字
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
/*開始遊戲*/
void play()
{
	unsigned char key;
	while (1){
		key = getch();
		if (key == 27)break;
		if (key == 13 || times != 0){
			system("cls");                                                               //清除先前表格
			printf("\n\n          使用↑↓←→鍵操作遊戲\n");
			show_map();                                                                  //印出數字和表格

			while (1){
				key = getch();                                                           //輸入按鍵
				if (key == 27)break;                                                     //輸入ESC則離開遊戲
				if (key == 13){                                                          //輸入ENTER則重新開始新遊戲
					printf("\n\t開始新遊戲，按任意鍵繼續");
					num = 0;
					times++;
					re();
					break;
				}
				if (key == 0 || key == 0xE0){
					system("cls");                                                       //清除先前表格
					key = getch();                                                       //輸入按鍵
					switch (key){
					case 72:toward_up();    CreateRandNumber(); show_map(); break;   //向上
					case 80:toward_down();  CreateRandNumber(); show_map(); break;   //向下
					case 75:toward_left();  CreateRandNumber(); show_map(); break;   //向左
					case 77:toward_right(); CreateRandNumber(); show_map(); break;   //向右
					default:  break;
					}
				}
			}
			break;
		}
	}
}
/*重複執行*/
void re(){
	if (times == 0)printf("\n\n\t         請按ENTER開始");
	init();              //初始化數組
	CreateRandNumber();  //在空格建立隨機變數
	play();              //開始遊戲
}
/*主程式*/
int main()
{
	printf("\n");  //這...恩...就印出2048啊
	printf("　　　▓▓▓　　▓▓▓　　▓　▓　　▓▓▓\n");
	printf("　　　　　▓　　▓　▓　　▓　▓　　▓　▓\n");
	printf("　　　▓▓▓　　▓　▓　　▓▓▓　　▓▓▓\n");
	printf("　　　▓　　　　▓　▓　　　　▓　　▓　▓\n");
	printf("　　　▓▓▓　　▓▓▓　　　　▓　　▓▓▓\n");
	printf("\n\n\       遊戲操作方式：使用↑↓←→鍵操作遊戲\n");
	re();
	printf("\n\n\t遊戲即將結束，");
	system("pause");
	return 0;
}