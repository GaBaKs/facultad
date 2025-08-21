program ejer3;
 var
   N,i:word;
 function suma (N:word;i:word):word;
  begin
    for i:=N downto 1 do
     suma:=suma+i;
  end;

begin
   Writeln('escriba un numero');
   Readln(N);
   Writeln('el resultado de la suma de N primeros numeros naturales es de ',suma(N,i));
   Readln();
end.

