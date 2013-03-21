#include <stdio.h>

int main(void) {
  int sum, i = 0;
  for(i; i<=1000; ++i) {
    if (!(i%3) || !(i%5)) {
      sum += i;
    }
  }
  printf("%d", sum);
}
