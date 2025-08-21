program ejer10;
 var
   Arch: text;
   A,ant,cont: integer;
begin
  cont:=1;
  assign(Arch,'ejer10.TXT');
  Reset(Arch);
  Readln(Arch,ant);
  While not eof(Arch) do
   begin
   Readln(Arch,A);
   if ant=A then
   cont:=cont+1
   else
     begin
       Writeln('el numero ',ant,' aparece ',cont,' veces.');
       cont:=1;
       end;
   ant:=A;
   end;
   Writeln('el numero ',ant,' aparece ',cont,' veces.');
   Readln();
end.

