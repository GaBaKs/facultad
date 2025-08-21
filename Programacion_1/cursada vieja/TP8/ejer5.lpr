program ejer5;
 type
   vector=array [1..30] of integer;
 procedure leervec(var i:byte;var V:vector);
   var
    sn:char;
    aux:integer;
   begin
   i:=0;
   sn:=' ';
   while (sn<>'n') and (sn<>'N') do
     begin
     i:=i+1;
     Writeln('ingrese un numero entero');
     Readln(aux);
     V[i]:=aux;
     Writeln('desea ingresar otro numero?(n o N para finalizar)');
     readln(sn);
    end;
 end;
 function suma (i:byte;V:vector):integer;
 begin
  if i=1 then
   suma:=V[1]
    else suma:=V[i]+suma(i-1,V);
 end;
procedure mostrar (i:byte;V:vector);
 var
  j:byte;
 begin
 j:=i;
 if j=1 then
  Write(V[1],' ')
 else
  begin
    mostrar(j-1,V);
    Write(V[j],' ');
 end;
 end;
procedure mostraratras (i:byte;V:vector);
var
 j:byte;
 begin
 j:=i;
 if j=1 then
  Write(V[1])
 else
  begin
     Write(V[j],' ');
     mostrar(j-1,V);

 end;
 end;

var
 i:byte;
 V:vector;
begin
leervec(i,V);
Writeln(suma(i,v));
mostrar(i,V);
Writeln();
mostraratras(i,V);
readln();
end.

