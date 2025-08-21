program ejer6;
function aleatorio(A,B:integer):integer;
begin
  aleatorio:=random(B)+A;
 end;

 var
 A,B: integer;
begin
  Writeln('escribe A');
  Readln(A);
  repeat
  Writeln('escribe B');
  Readln(B);
  until B>A;



  Writeln('numero aleatorio:',aleatorio(A,B));
  Readln();
end.

