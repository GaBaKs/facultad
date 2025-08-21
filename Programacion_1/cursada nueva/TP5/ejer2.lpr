program ejer2;
type
  Tvec= array[1..100] of integer;
 procedure lectura(var vpar:Tvec;var vimp:Tvec;var i:byte;var j:byte);
 var
  arch:text;
  aux:integer;
 begin
   Assign(arch,'ejer2.TXT');
   Reset(arch);
   i:=1;
   j:=1;
   Read(arch,aux);
   While not eof(arch) do
    begin
      While (aux=0) and (not eof(arch)) do
       Read(arch,aux);
      if not eof(arch) then
      if (aux mod 2)=0 then
       begin
        vpar[i]:=aux;
        i:=i+1;
       end
       else
        begin
         vimp[j]:=aux;
         j:=j+1;
        end;
        Read(arch,aux);
    end;
 end;
var
 vpar,vimp:Tvec;
 k:byte;
 i,j:byte;
begin
  lectura(vpar,vimp,i,j);
  for k:=1 to i do
   Write(' ',vpar[k]);
  Writeln();
  for k:=1 to j do
   Write(' ',vimp[k]);
Readln();
end.

