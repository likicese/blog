int pin = 3;

void setup() {
  // put your setup code here, to run once:
  // Serial.begin(9600);
  pinMode(pin, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  // Serial.println("hello world");
  digitalWrite(pin, 1);
  delay(500);
  digitalWrite(pin, 0);
  delay(500);
}
