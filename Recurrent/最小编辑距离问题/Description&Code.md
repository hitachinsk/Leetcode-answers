# Description
给定两个字符串,只允许以下三中操作:
- 插入一个字符
- 删除一个字符
- 替换一个字符

求:**把a转换成b的最小操作次数,也就是所谓的最小编辑距离.**

**Example:**
```
"xy"=>"xz"只需要把y替换成z,所以最小的编辑距离为1
"xyz"=>"xy"只需要删除z,所以最小编辑距离为1
```

# Code
- Recurrent
```c
#include<stdio.h>

int main() {
	int recursion(char* a, char* b, int i, int j) ;
	char *a = "FreshMeat" ;
	char *b = "FishAndMeat" ;
	int ret = recursion(a, b, 9, 11) ;
	printf("%d\n", ret) ;
}


int recursion(char* a, char* b, int i, int j) {
    if (j == 0) {
        return i ;
    } else if (i == 0) {
        return j ;
    } else if (a[i - 1] == b [j - 1]) {
        return recursion(a, b, i - 1, j - 1) ;
    } else {
        int m1 = recursion(a, b, i - 1, j) + 1 ;
        int m2 = recursion(a, b, i, j - 1) + 1 ;
        int m3 = recursion(a, b, i - 1, j - 1) + 1 ;
        int ret = m1 < m2 ? m1 : m2 ;
        return ret < m3 ? ret : m3 ;
    }
}
```
- DP
```c
#include<stdio.h>
#include<stdlib.h>

int main() {
	int dp(char *a, char *b, int aLength, int bLength) ;
	char *a = "FreshMeat" ;
	char *b = "FishAndMeat" ;
	int ret = dp(a, b, 9, 11) ;
	printf("%d\n", ret) ;
}

int dp(char *a, char *b, int aLength, int bLength) {
	int lenA = aLength ;
	int lenB = bLength ;
	int **d ;
	int i, j ;
	d = (int**)malloc(lenA * sizeof(int*)) ;
	for (j = 0; j < lenA; j ++) {
		d[j] = (int*)malloc(lenB * sizeof(int)) ;
	}
	for (j = 0; j < lenB; j ++) {
		d[0][j] = j ;
	}
	for (j = 0; j < lenA; j ++) {
		d[j][0] = j ;
	}
	for (i = 1; i < lenA; i ++) {
		for (j = 1; j < lenB; j ++) {
			if (a[i-1] == b[j-1]) {
				d[i][j] = d[i-1][j-1] ;
			} else {
				int m1 = d[i-1][j] + 1 ;
				int m2 = d[i][j-1] + 1 ;
				int m3 = d[i-1][j-1] + 1 ;
				int temp = m1 < m2 ? m1 : m2 ;
				d[i][j] = temp < m3 ? temp : m3 ;
			}
		}
	}
	int ret = d[lenA-1][lenB-1] ;
	for (i = 0; i < lenA; i ++) {
		free(d[i]) ;
		d[i] = NULL ;
	}
	free(d) ;
	d = NULL ;
	return ret ;
}
```
