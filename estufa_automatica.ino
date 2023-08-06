
// Projeto estufa
// Criado por: Maxwell T.Romão
// Curo IOT
// Professor Diego Bruno
// Data: 06/08/2023

int led = 13;
int ventilador = 5;
int buzina = 7;
long int sensorTemp  = A0;
long int ValorSensor = 0;
int CalcTemp, Temperatura, alarme = 0;

void setup()
{ 
  Serial.begin(9600);
  pinMode (led, OUTPUT);
  pinMode (ventilador, OUTPUT);
  pinMode (buzina, OUTPUT);
  pinMode (sensorTemp, INPUT);
} 

void loop()
{ 
  ValorSensor = analogRead(sensorTemp);
  CalcTemp = ValorSensor * (5000 / 1000);
  Temperatura = ((CalcTemp-500)/10)-3;
  Serial.println(Temperatura);
  
  if(Temperatura >=30) // Testa se Temperatura é maior ou igual a 30
  { 
     digitalWrite(ventilador, HIGH);// Liga o ventlador
  } 
    if(Temperatura <27) // Testa se Temperatura é menor que 27
       {
        digitalWrite(ventilador, LOW); // Desliga o ventlador
       }
  

  
 if(Temperatura >50) // Testa se a temperatura é maior que 50
 {
   //digitalWrite(led, HIGH);digitalWrite(buzina, HIGH); // Liga led e buzina
   alarme = 1; // Implementação de um se ao final do código
 } 
      if(Temperatura <47) // Testa de temperatura é menor que 47
      {
        //digitalWrite(led, LOW);digitalWrite(buzina,LOW); // Desliga led e buzina
        alarme = 0; // Implementação de um se ao final do código
      } 
 // *************************   alarme com buzina e led intermitentes ***************************
  if (alarme == 1) 
  {
  digitalWrite(led, HIGH);digitalWrite(buzina, HIGH); // Liga led e buzina
    delay(500);
  digitalWrite(led, LOW);digitalWrite(buzina,LOW); // Desliga led e buzina
    delay(500);
  }
  
  
  
} 