program ejer10;
 var
   num,aux:byte;
   frec:byte;
   arch:text;
begin
  frec:=0;
  Assign(arch,'EJER10.TXT');
  Reset(arch);
  read(arch,aux);
  while not eof(arch) do
   begin
     repeat
     frec:=frec+1;
     Read(arch,num);
     until aux<>num;
     Writeln('numero: ',aux,' ,frecuencia: ',frec);
     frec:=0;
     aux:=num;
   end;
  Readln();
end.

