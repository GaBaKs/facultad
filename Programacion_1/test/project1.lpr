program project1;
type
  st30=string[30];
  Tchar=file of text;
  var
    arch:text;
    aux:char;
begin
  Assign(arch,'asdasd.DAT');
  reset(arch);
  While not eof(arch) do
   begin
    read(arch,aux);
    Write(aux,' ');
   end;
  Readln();
end.

