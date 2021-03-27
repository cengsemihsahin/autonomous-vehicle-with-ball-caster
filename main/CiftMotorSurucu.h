/*
	@cengsemihsahin
*/

#ifndef CiftMotorSurucu_H
#define  CiftMotorSurucu_H

#include "Arduino.h"

class CiftMotorSurucu{
  public:
    CiftMotorSurucu();
    void motor(int motorSec, int yon, int motorHizi);
    void ileri(int hiz);
    void geri(int hiz);
    void sag(int hiz);
    void sol(int hiz);
    void dur();
  private:
    int M1AB;
    int M2AB;
};

#endif
