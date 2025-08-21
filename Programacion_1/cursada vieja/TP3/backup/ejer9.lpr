program ejer9;
  var
    Arch: text;
    A,ant,cont,test:integer;
begin
  Assign(Arch,'ejer9.TXT');
  Reset(Arch);
  Readln(Arch,ant);
  Writeln(ant);
  While not eof (Arch) do
   begin
        Readln(Arch,A);
        Writeln(A);
        if A<ant then
        cont:=cont+1;
        ant:=A;
   end;
  If cont=0 then
  Writeln('los numeros estan ordenados de forma ascendente')
  else Writeln('los numeros no estan ordenados de forma ascendente');
  Readln();
end.

