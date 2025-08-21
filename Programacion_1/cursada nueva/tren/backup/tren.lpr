program tren;
 const
   max=50;
 type
    st8=string[8];
    st4=string[4];
   Tvecst4=array[1..max] of  st4;
   Tvecst8=array[1..max] of st8;
   Tvecbyte=array[1..max] of byte;


 procedure lectura(var Vres:Tvecst4;var Vdni:Tvecst8;var Vedad:Tvecbyte;var N:byte;var Vpeso:Tvecbyte);
  var
    arch:text;
    i,j:byte;
    reserva:st4;
    aux:char;
    verif:st4;
    flag,flag2:boolean;
  begin
   Assign(arch,'CHECKIN.TXT');
   Reset(arch);
   Readln(arch,N);
    i:=1;
    j:=N+1;
    flag:=false;
    flag2:=true;
   Readln(arch,Vres[i],aux,Vdni[i],aux,Vedad[i],aux,Vpeso[i]);
   reserva:=Vres[i];


 //true=i false=j
   While not (eof(arch))do
    begin
     read(arch,verif);
     if flag2 then
         if verif=reserva then
           flag:=true
         else
          flag:=false
     else
       if verif=reserva then
          flag:=false
       else
         flag:=true;
    if flag then
     begin
        i:=i+1;
        Vres[i]:=verif;
        Readln(arch,aux,Vdni[i],aux,Vedad[i],aux,Vpeso[i]);
        reserva:=verif;
        flag2:=true;
      end
     else begin
       j:=j-1;
       Vres[j]:=verif;
       Readln(arch,aux,Vdni[j],aux,Vedad[j],aux,Vpeso[j]);
       reserva:=verif;
       flag2:=false;
     end;

    end;
   Close(arch);
 end;



function incisoa(Vdni:Tvecst8;Vpeso:Tvecbyte;N:byte;x:byte):st8;
 var
   i:byte;
   flag:boolean;
 begin
   i:=1;
   flag:=false;
   While (i<=N) and (not(flag)) do
    begin
     if x<Vpeso[i] then
      begin
         flag:=true;
         incisoa:=Vdni[i];
      end
     else i:=i+1;
     if i=N+1 then
      incisoa:='no hay.';
    end;
 end;
function incisob(N:byte;E1,E2:byte;Vedad:Tvecbyte;Vpeso:Tvecbyte):Real;
 var
   i:byte;
   acum,cont:word;
   aux:real;
 begin
   acum:=0;
   cont:=0;
   for i:=1 to N do
    if Vedad[i] in[E1..E2] then
     begin
      cont:=cont+1;
      acum:=acum+Vpeso[i];
     end;
   if cont<>0 then
    incisob:=acum/cont
    else incisob:=0;
 end;
Procedure incisoc(Vedad:Tvecbyte;N:byte;Vdni:Tvecst8);
var
  i:byte;
  minimo1,minimo2,minimo3:byte;
  dni,dni2,dni3:st8;
 begin
   minimo1:=200;
   minimo2:=200;
   minimo3:=200;
   for i:=1 to N do
     if (minimo1>Vedad[i]) and (Vedad[i]<>0) then
      begin
       minimo1:=Vedad[i];
       dni:=Vdni[i];
      end;
   for i:=1 to N do
      if (minimo2>Vedad[i]) and (dni<>Vdni[i]) and (Vedad[i]<>0) then
       begin
        minimo2:=Vedad[i];
        dni2:=Vdni[i];
        Writeln('el 2 es ',dni2);
       end;
   for i:=1 to N do
     begin
      if (minimo3>Vedad[i]) and (dni<>Vdni[i]) and (dni2<>Vdni[i]) and (Vedad[i]<>0) then
       begin
       minimo3:=Vedad[i];
       dni3:=Vdni[i];
       end;
     end;
   Writeln('el DNI de los 3 pasajeros mas chicos son: ');
   Writeln(dni);
   Writeln(dni2);
   Writeln(dni3);


 end;

 var
   x,E1,E2:byte;
   Vdni:Tvecst8;
   Vpeso:Tvecbyte;
   N:byte;
   Vedad:Tvecbyte;
   Vres:Tvecst4;
begin
  lectura(Vres,Vdni,Vedad,N,Vpeso);
  Writeln('ingrese un peso de equipaje de mano');
  Readln(x);
  Writeln('El dni del primer pasajero encontrado con un equipaje de peso mayor a ',x,' es: ',incisoa(Vdni,Vpeso,N,x));
  repeat
  Writeln('ingrese un rango de edades(E1 es menor que E2)');
  Readln(E1,E2);
  until E1<E2;
  Writeln('el peso promedio del equipaje de mano para el rango de edades seleccionado es de ',incisob(N,E1,E2,Vedad,Vpeso):2:2);
  incisoc(Vedad,N,Vdni);
  Readln();
end.

