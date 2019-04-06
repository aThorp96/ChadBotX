void setup() {
  Serial.begin(115200);
}

int i = 0;
void loop() {
  Serial.write(i);
  i = i == 255 ? 0 : i + 1;
}
