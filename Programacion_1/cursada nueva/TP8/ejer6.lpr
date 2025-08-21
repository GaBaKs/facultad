program ejer6;
 const
   max=100;
 type
  Tvec= array[1..max] of real;

procedure lectura(var vec: Tvec;var N:byte);
 var
   i:byte;
 begin
   Writeln('datos a ingresar: ');
   Readln(N);
   for i:=1 to N do
    begin
       Writeln('ingrese el dato ',i);
       Readln(vec[i]);
    end;
 end;
procedure incisoa(vec:Tvec;N:byte;X:real;var flag:boolean);
 begin
   if (N=0) and (not flag) then
    Writeln('0')
   else begin
    if X=vec[N] then
     begin
      Writeln('el valor X esta en la posicion ',N);
      flag:=true;
      end;
    if N<>0 then
     incisoa(vec,N-1,X,flag);
     end;
end;

var
  vec:Tvec;
  N:byte;
  X:real;
 flag:boolean;
begin
  flag:=false;
  lectura(vec,N);
  Writeln('ingrese un X');
  Readln(X);
  incisoa(vec,N,X,flag);
  Readln();
end.

