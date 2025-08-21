program ejer23;
 var
   arch:text;
   flag:boolean;
   long,contdig:byte;
begin
  Assign(arch,'ejer23.TXT');
  Reset(arch);
  While not eof(arch) do
   begin
    Read(arch,char);
   end;
end.

