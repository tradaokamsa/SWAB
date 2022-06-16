#define SensorPin A0            
#define Offset 0.70            
unsigned long int avgValue;     
void setup()
{
  pinMode(13,OUTPUT);  
  Serial.begin(9600);  
}
void loop()
{
  //do ph
  int buf[10];                
  for(int i=0;i<10;i++)       
  { 
    buf[i]=analogRead(SensorPin);
    delay(10);
  }
  for(int i=0;i<9;i++)        
  {
    for(int j=i+1;j<10;j++)
    {
      if(buf[i]>buf[j])
      {
        int temp=buf[i];
        buf[i]=buf[j];
        buf[j]=temp;
      }
    }
  }
  avgValue=0;
  for(int i=2;i<8;i++)                      
    avgValue+=buf[i];
  float do_Ph=(float)avgValue*5.0/1024/6; 
  do_Ph=2.0*do_Ph+Offset; 
  int do_duc = analogRead(A1); 
  String do_duc_string;
  do_duc_string.concat(do_duc);
  String do_Ph_string;
  do_Ph_string.concat(do_Ph);
  String url = "http://swabteam.herokuapp.com/";
  url = url + "?" +"do_Ph=" + do_Ph + "&" + "do_duc=" + do_duc;
  Serial.print(url);
  delay(3000);
                      
}
