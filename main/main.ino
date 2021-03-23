#include <CiftMotorSurucu.h>

#define echo 11
#define trigger 3
#define lazer 12

CiftMotorSurucu arac;


int maxMesafe = 30;
int minMesafe = 0;
int motorHizi = 255;

int mesafeOlc(int enAz, int enFazla);

void setup() {
  Serial.begin(9600);
  pinMode(echo, INPUT);
  pinMode(trigger, OUTPUT);
  pinMode(lazer, OUTPUT);
}

void loop() {
  int mesafe = mesafeOlc(minMesafe, maxMesafe, echo, trigger);
  
  if (mesafe != -1) { // veri geldi
    digitalWrite(lazer, HIGH); // lazeri yak
    arac.dur();
    delay(200);
    analogWrite(9, motorHizi);
    analogWrite(5, motorHizi);
    analogWrite(10, 0);
    analogWrite(6, 0);
    delay(750);
  }
  else {
    digitalWrite(lazer, LOW); // lazeri sondur
    arac.geri(motorHizi); // motor konumuna gore aslinda ileri gider 
    delay(150);
  }
  
}


int mesafeOlc(int enAz, int enFazla, int echoPin, int trigPin) {
  long geriGelmeSuresi, uzaklik;
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  geriGelmeSuresi = pulseIn(echoPin, HIGH);
  uzaklik = geriGelmeSuresi / 58.2;
  if (uzaklik > enFazla || uzaklik <= enAz)
    return -1;
  else
    return uzaklik;
}
