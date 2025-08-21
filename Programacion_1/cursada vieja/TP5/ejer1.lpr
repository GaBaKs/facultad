program ejer1;
type
   TVec=array[1..100] of integer;
Var
  N: integer;
  vec:TVec;
 procedure LeerVector(var vec: TVec;var N: integer);
  var
    i: integer;
    begin
  Writeln('cuantos numeros va a ingresar(<=100)');
  Readln(N);
  for i:=1 to N do
   begin
    Writeln('ingrese el numero que va en el espacio ',i);
    Readln(vec[i]);
    end;
    end;
Function suma(vec:TVec;N:integer):integer;
  var
    i,sum: integer;
 begin
 sum:=0;
  for i:=1 to N do
   sum:=sum+vec[i];
  Suma:=Sum;
  end;
procedure pares(vec:Tvec;N:integer);
 var
  i: integer;
   begin
    for i:=1 to N do
     begin
     if  not odd(i) then
      Writeln(vec[i]);
    end;
end;
function max(vec:Tvec;N:integer):integer;
var
 maximo,i:integer;
   begin
    maximo:=0;
    for i:=1 to N do
     if maximo<vec[i] then
      maximo:=vec[i];
    max:=maximo;
    end;
function min(vec:Tvec;N:integer):integer;
var
 minimo,i:integer;
   begin
    minimo:=100000000;
    for i:=1 to N do
     if minimo>vec[i] then
      minimo:=vec[i];
    min:=minimo;
    end;
procedure arregloB(vec:TVec;N:integer);
 var
  vecB: TVec;
  i,aux:integer;
    begin
     aux:=N;
     for i:=1 to N do
      begin
      vecB[i]:=vec[aux];
     aux:=aux-1;
     end;
     Write('El arreglo permutado es ');
     for i:=1 to N do
      Write(vecB[i],',');
 end;

 begin {programa principal}
  Leervector(vec,N);
  Writeln('la suma de sus elementos es ',Suma(vec,N));
  Writeln('los elementos en posiciones pares son ');pares(vec,N);
  Writeln('el maximo es ',max(vec,N));
  Writeln('el minimo es ',min(vec,N));
  arregloB(vec,N);
  Readln();
 end.
