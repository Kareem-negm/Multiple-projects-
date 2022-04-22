
// Face tracking using arduino and python

#include<Servo.h>

Servo servoVer; //Vertical Servo
Servo servoHor; //Horizontal Servo

int centerScreenX = 320;
int centerScreenY = 240;
int x;
int y;
int dx;
int dy;

int servoMaxX = 178, servoMinX = 2 ;
int servoMaxY = 150 , servoMinY = 30 ;
int servoX0 = 90;
int servoY0 = 90;
int servoX;
int servoY;

void servowrite(int angleX,int angleY);
void Position();

void setup()
{
  Serial.begin(9600);
  servoVer.attach(5); //Attach Vertical Servo to Pin 5
  servoHor.attach(6); //Attach Horizontal Servo to Pin 6
  servoVer.write(90);
  servoHor.write(90);
}

void loop()
{
  if (Serial.available() > 0)
  {
    if (Serial.read() == 'X')
    {
      x = Serial.parseInt();
      if (Serial.read() == 'Y')
      {
        y = Serial.parseInt();
        Position();
        delay(500);
      }
    }
    while (Serial.available() > 0)
    {
      Serial.read();
    }
  }
}

void servowrite(int angleX,int angleY)
{
  int h =  servoHor.read(),v = servoVer.read() ;
  int pos = 0;
  
  if(angleX > h)
  {
    for (pos = h; pos <=angleX  ; pos += 1){servoHor.write(pos);  delay(8);} 
  }
  if(angleX < h)
  {
    for (pos = h; pos >=angleX ; pos -= 1){servoHor.write(pos);  delay(8);} 
  }

  if(angleY > v)
  {
    for (pos = v; pos <=angleY  ; pos += 1){servoVer.write(pos);  delay(7);} 
  }
  if(angleY < v)
  {
    for (pos = v; pos >=angleY ; pos -= 1){servoVer.write(pos);  delay(8);} 
  }
}

void Position()
{
  dx = x - centerScreenX;
  dy = y - centerScreenY;
  servoX = map(dx, -320, 320,servoX0 + 17,servoX0 - 17);
  servoY = map(dy, -240, 320, servoY0 + 17,servoY0 - 17);

  if (servoX < servoMaxX && servoX > servoMinX && servoY < servoMaxY && servoY > servoMinY)
  {
    servowrite(servoX,servoY);
    servoX0 = servoHor.read();
    servoY0 = servoVer.read();
  }
  else 
  {
    servoX0 = 90;
    servoY0 = 90;
    servowrite(servoX0,servoY0);
  }
}
