program parcial;
type
  Tvecint=array[1..100] of byte;
 procedure lectura(var contN:byte;var veclong:Tvecint;var contNmax:byte;var contval:byte);
  var
   arch:text;
   car:char;
  flag: boolean;
  begin
  flag:=false;
  contNmax:=0;
  contN:=0;
  contval:=0;
  car:=' ';
   Assign(arch,'parcial.TXT');
   Reset(arch);
  While car<>':' do
   begin
    Read(arch,car);
    if car='@' then
     flag:=true;
    While (car<>'@') and (not(flag)) do
     begin
      if (car in['a'..'z']) or (car in['A'..'Z']) or (car in['0'..'9']) then
       contN:=contN+1
      else flag:=true;
      if not flag then
      Read(arch,car);
     end;
    if not flag then
    read(arch,car);
    if car='.' then
     flag:=true;
    While (car<>'.') and (not (flag)) do
     begin
      if (not (car in['a'..'z'])) and (not (car in['A'..'Z'])) and (not (car in['0'..'9'])) then
       flag:=true;
      if not flag then
      read(arch,car);
     end;
    if not flag then
    read(arch,car);
    if car=';' then
     flag:=true;
    While (car<>';') and (car<>':') and (not(flag)) do
     begin
      if (not (car in['a'..'z'])) and (not (car in['A'..'Z'])) and (not (car in['0'..'9'])) then
       flag:=true;
      if not flag then
      Read(arch,car);
     end;
    if not flag then
     begin
       veclong[contN]:=veclong[contN]+1;
       if contN>contNmax then
        contNmax:=contN;
       contval:=contval+1;
     end
    else
     While (car<>';') and (car<>':') do
      read(arch,car);
    flag:=false;
    contN:=0;

   end;
  close(arch);
 end;
function insisoa(N:byte;veclong:Tvecint):byte;
 begin
   insisoa:=veclong[N];
 end;
procedure insisob(N:byte;veclong:Tvecint;contNmax:byte;contval:byte);
 var
  i:byte;
  porcentaje:Real;
  longitudusada,cuantosusos:byte;
 begin
  cuantosusos:=0;
  porcentaje:=0;
  for i:=1 to contNmax do
   if cuantosusos<veclong[i] then
    begin
     longitudusada:=i;
     cuantosusos:=veclong[i];
    end;
   if contval<>0 then
    porcentaje:=((cuantosusos/contval)*100);

    if porcentaje<>0 then
  Writeln('la longitud de nombre de usuario mas usada es de ',longitudusada,' y representa un ',porcentaje:3:2,'% del total de las validas')
  else Writeln('No hay correos ingresados para poder calcular la longitud del nombre de usuario mas usado');

 end;

var
  N:byte;
  veclong:Tvecint;
  contN,contNmax:byte;
  contval:byte;
begin
  repeat
  Writeln('ingrese un valor de N entre 1 y 30');
  Readln(N);
  until (N>=1) and (N<=30);
  lectura(contN,veclong,contNmax,contval);
  Writeln('la cantidad de nombres de usuarios que tienen exactamente ',N,' caracteres es de ',insisoa(N,veclong));
  insisob(N,veclong,contNmax,contval);
  readln();

end.

