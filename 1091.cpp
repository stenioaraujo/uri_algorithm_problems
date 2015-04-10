#include <stdio.h>
#include <string.h>
/* URI problem 1091 - Division of Nlogonia
 @author stenio.araujo@ccc.ufcg.edu.br */

int main() {
	int K, N, M, X, Y;
	char s[7];
	
	while (true) {
		scanf("%i%*c", &K);
		if (K == 0) break;
		scanf("%i %i%*c", &N, &M);
		for (int i = 0; i < K; i++){
			scanf("%i %i%*c", &X, &Y);
			if (X > N && Y > M) strcpy(s, "NE");
			else if ( X > N && Y < M ) strcpy(s, "SE");
			else if (X < N && Y < M) strcpy(s, "SO");
			else if (X < N && Y > M) strcpy(s, "NO");
			else strcpy(s, "divisa");
			printf("%s\n", s);
		}
	}	

	return 0;
}
