program ejer15;
 var
   i: integer;
   letra,letrarch: char;
   Arch: text;
begin
  i:=0;
  Assign(Arch,'ejer15.TXT');
  Writeln('escriba una letra');
  Readln(letra);
  Reset(Arch);
While not eof(Arch) do
begin
  Read(Arch,letrarch);
  if letra=letrarch then
      i:=i+1;
  repeat
   Read(Arch,letrarch);
   if letrarch=' ' then
    begin
    Read(Arch,letrarch);
     if letra=letrarch then
      i:=i+1
     end;
    until letrarch='.';
end;
Writeln('la cantidad de palabras iniciadas con la letra ',letra,' es de ',i);
Readln();
end.

