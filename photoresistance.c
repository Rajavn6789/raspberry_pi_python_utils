/*
* Compiling: gcc -Wall -o photoresistance photoresistance.c -lwiringPi
* Run: sudo ./photoresistance
* NOTE
* A2D Conversion
* 1) Sampling rate should be 10 times than the frequency of the signal
* 2) 8bit A2D - (value * 5V)/2**8 = (value * 5000)/255
* 3) More the bits more the accuracy is.
*/
#include <wiringPi.h>
#include <pcf8591.h>
#include <stdio.h>

#define BUZZER_PIN 1

#define Address 0x48
#define BASE 64
#define A0 BASE+0
#define A1 BASE+1
#define A2 BASE+2
#define A3 BASE+3

/* function that ons and offs BUZZER_PIN */
void ledWarning(int num){
  for(int count = 0; count < num; ++count)
  {
    digitalWrite(BUZZER_PIN, HIGH);
    delay(100);
    digitalWrite(BUZZER_PIN, LOW);
    delay(100);
  }
}

int main(void)
{
  int value, intensity;

  // Initialize wiringPi
  wiringPiSetup();

  // Initialize pcf8591
  pcf8591Setup(BASE, Address);

  // Initialize Buzzer
  pinMode (BUZZER_PIN, OUTPUT);
  digitalWrite(BUZZER_PIN, LOW);

  while(1)
  {
    value = analogRead(A0);
    intensity = (value * 5000)/255;
    printf("Current light intensity: %dmv\n", intensity);
    if (intensity > 1000)
    {
      ledWarning(3);
    }
    else
    {
      delay(200);
    }
  }

  return 0;
}
