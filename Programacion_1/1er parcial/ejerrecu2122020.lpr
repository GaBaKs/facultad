program ejerrecu2122020;
const
  max=30;
type
  st6=string[6];
  Vst=array[1..max] of st6;
  Vreal=array[1..max]of real;
 procedure leerarchivo(var Vcod:Vst;var Vigg:Vreal;var Vigm:Vreal);
 var
   arch: text;
   letra:char;
   aux:st6;
   aux2:real;
   N:byte;
begin
   Assign(arch,'HISOPADOS.TXT');
   Reset(arch);
   N:=0;
   while not eof(arch) do
     begin
     while letra<>' ' do
       begin
         Read(arch,letra);
         aux:=aux+letra;
       end;
     Read(arch,letra);

     if letra='S' then
      begin
        N:=N+1;
        Vcod[N]:=aux;
        Read(arch,aux2);
        Vigg[N]:=aux2;
        Read(arch,aux2);
        Vigm[N]:=aux2;
        Readln(arch);
        Writeln('codigo: ',Vcod[N],' IGG: ',Vigg[N]:8:2,' IGM: ',Vigm[N]:8:2);
      end
      else readln(arch);
      letra:='0';
      aux:='';
     end;
end;

var
  Vcod:vst;
  Vigg:vreal;
  Vigm:vreal;
begin
  leerarchivo(Vcod,Vigg,Vigm);
  Readln();
end.

