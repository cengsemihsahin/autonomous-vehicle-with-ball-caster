/*
	Arduino UNO icin yazilmistir. Pinleri degistirebilirsiniz.
	@cengsemihsahin
*/

#include "Arduino.h"
#include "CiftMotorSurucu.h"

CiftMotorSurucu::CiftMotorSurucu() {
	pinMode(M1AB, OUTPUT);
	pinMode(M2AB, OUTPUT);
}

void CiftMotorSurucu::motor(int motorSec, int yon, int motorHizi) {

  switch(motorSec) {
	case 1:
		M1AB = 9;
		M2AB = 5;
		break;
	case 2:
		M1AB = 10;
		M2AB = 6;
		break;
	default:
		break;
  }

  switch(yon){
	case 1:
		analogWrite(M1AB, motorHizi);
		analogWrite(M2AB, 0);
		break;
	case 2:
		analogWrite(M1AB, 0);
		analogWrite(M2AB, motorHizi);
		break;
	case 3:
		analogWrite(M1AB, 0);
		analogWrite(M2AB, 0);
		break;
	default:
		break;
  }
}

void CiftMotorSurucu::ileri(int hiz){
	motor(1, 1, hiz);
	motor(2, 2, hiz);
}

void CiftMotorSurucu::geri(int hiz){
	motor(1, 2, hiz);
	motor(2, 1, hiz);
}

void CiftMotorSurucu::sag(int hiz){
	motor(1, 1, hiz);
	motor(2, 1, hiz);
}
void CiftMotorSurucu::sol(int hiz){
	motor(1, 2, hiz);
	motor(2, 2, hiz);
}

void CiftMotorSurucu::dur(){
	motor(1, 3, 0);
	motor(2, 3, 0);
}
