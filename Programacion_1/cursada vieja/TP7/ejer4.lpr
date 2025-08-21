program ejer4;
const
  max=30;
  type
    st8=string[8];
    st30=string[30];
    reg=array[1..max] of record
     nombre:st8;
     partidos:byte;
     resultado:st30;
     puntaje:word;
    end;
 procedure lectura(var registro:reg;var s:byte);
 var
   arch:text;
  i:byte;
 aux:char;
 begin
 s:=1
   Assign (arch,'equipos.TXT');
   Reset(arch);
   while not eof(arch) do
   begin
    with registro[s] do
     begin
      Read(arch,nombre,partidos);
      for i:=1 to partidos do
       read(arch);
       read(arch,aux)
      case aux of
       'G':resultado:=resultado+aux;
           puntaje:=puntaje+3;
       'E':resultado:=resultado+aux;
           puntaje:=puntaje+1;
       'P':resultado:=resultado+aux;
      end;
     end;
     Readln(arch);
     s:=s+1;
    end;
 end;
 procedure ejercicioa(s:byte;registro:reg);
 var
 i:byte
 begin
   for i:=1 to s do
     Writeln('nombre del club: ',registro[i].nombre,' puntos obtenidos: ',registro[i].puntaje);
 end;

 function maximo(i:byte;registro:reg;s:byte):st8;
 var
 max:byte;
 maxnom:st8;
 begin
   max:=0;
  for i:=1 to s do
   if max<registro[i].puntaje then
    begin
    max:=registro[i].puntaje;
    maxnom:=registro[i].nombre;
    end;
  maximo:=maxnom;


begin
end.

