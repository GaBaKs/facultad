program ejer4;
const
  max=100;
 type
   st20=string[20];
   reg=array[1..max] of record
     nombre:st20;
     res:word;
     per:boolean;
   end;


procedure lectura(var registro:reg;var cont:byte);
 var
  nom:st20;
  i,j:byte;
 car:char;
 suma:byte;
 begin
   Writeln('ingrese un nombre de equipo(000 para fin de datos): ');
   Readln(nom);
   cont:=0;
 While nom<>'000' do
  begin
  suma:=0;
  cont:=cont+1;
  registro[cont].nombre:=nom;
  registro[cont].per:=false;
   Writeln('cantidad de partidos jugados: ');
   Readln(i);
   Writeln('resultado de cada encuentro: ');
   for j:=1 to i do
    begin
    repeat
     Writeln('encuentro nro ',j);
     Readln(car);
    until (upcase(car)='G') or (upcase(car)='E') or (upcase(car)='P');
     case upcase(car) of
      'G': suma:=suma+3;
      'E': suma:=suma+1;
      'P': registro[cont].per:=true;
     end;
   end;
   registro[cont].res:=suma;
   Writeln('valor de suma', registro[cont].res);
  Writeln('ingrese un nombre de equipo(000 para fin de datos)');
  Readln(nom);
  end;
 end;

procedure incisoa(registro:reg;cont:byte);
 var
  i:byte;
 begin
  for i:=1 to cont do
   Writeln('nombre del club: ',registro[i].nombre, ' puntaje obtenido: ',registro[i].res);
 end;
procedure incisob(registro:reg;cont:byte);
 var
  i,j:byte;
  max:word;
  nomax:st20;
 begin
 max:=0;
  for i:=1 to cont do
   begin
    if max<=registro[i].res then
     if max=registro[i].res then
      nomax:=nomax+','+registro[i].nombre
     else
      begin
       max:=registro[i].res;
       nomax:=registro[i].nombre;
      end;
 end;
  Writeln('el/los punteros de la tabla son: ', nomax);
 end;

procedure incisoc(registro:reg;cont:byte);
 var
  i,j:byte;
  porc:real;
 begin
 j:=0;
  for i:=1 to cont do
   if not(registro[i].per) then
    j:=j+1;
  porc:=j/cont*100;
  Writeln('El porcentaje de los que no perdieron ningun partido con respecto al total es de ',porc:2:2,'%');
 end;
 var
  registro:reg;
  cont:byte;
begin
  lectura(registro,cont);
  incisoa(registro,cont);
  incisob(registro,cont);
  incisoc(registro,cont);
  Readln();
end.

