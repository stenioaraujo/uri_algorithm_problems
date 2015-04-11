#include <stdio.h>
#include <map>

using namespace std;

int main() {
	map<int, int> numbers;
	int N, n;
	
	scanf("%i", &N);
	while (N-- > 0) {
		scanf("%i", &n);
		numbers[n] += 1;
	} 
	
	for (map<int,int>::iterator i = numbers.begin(); i != numbers.end(); i++) {
		printf("%i aparece %i vez(es)\n", (*i).first, (*i).second);
	}
	
	return 0;
}
