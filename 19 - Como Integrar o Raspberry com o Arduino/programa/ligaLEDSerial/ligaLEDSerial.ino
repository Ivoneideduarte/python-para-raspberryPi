#define pinLED 8

void setup()
{
  Serial.begin(9600);
  pinMode(pinLED, OUTPUT);
}

void loop()
{
  if (Serial.available())
  {
    char lido = char(Serial.read());

    if (lido == '0') digitalWrite(pinLED, LOW);
    if (lido == '1') digitalWrite(pinLED, HIGH);
  }
}
