#define pinLDR A0

unsigned long delayEnvio;

void setup() 
{
  Serial.begin(9600);
}

void loop() 
{
  if((millis() - delayEnvio) > 50)
  {
    Serial.println(analogRead(pinLDR));
    delayEnvio = millis();
  }
}
