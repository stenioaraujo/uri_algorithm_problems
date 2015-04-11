#include <stdio.h>

using namespace std;

int main(){
	//technique using array;
	int mag[10099], N, a, b, c, peaks;
	
	while (true) {
		scanf("%i", &N);
		if (N == 0) break;
		
		for (int i = 0; i < N; i++) {
			scanf("%i", mag + i);
		}
		mag[N] = mag[0];
		mag[N+1] = mag[1];
		
		peaks = 0;
		for (int i = 0; i < N; ++i) {
			a = mag[i];
			b = mag[i+1];
			c = mag[i+2];
			if (a<b && b > c || a>b && b<c)
				peaks += 1;
		}
		
		printf("%i\n", peaks);
	}
	return 0;
}
