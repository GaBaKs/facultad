program ejer1;
 function potencia(X,n:integer):integer;
  begin
    if (n=0) or (n=1) then
    potencia:=1
    else
    potencia:=X*potencia(X,n-1);
  end;
var
  X,n: integer;
begin
   Writeln(potencia(3,4));
   Readln();
end.

