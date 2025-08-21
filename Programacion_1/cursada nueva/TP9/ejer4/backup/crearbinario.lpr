program crearbinario;
 type
   st4=string[4];
   TR=record
     codart:st4;
     talle:char;
     color:byte;
     cantp:byte;
     precio:real;
   end;
 FTR=file of TR;
var
  arch:text;
  arch2:FTR;
  aux:TR;
begin
  Assign(arch,'STOCK.TXT');
  Assign(arch2,'STOCK.DAT');
  Reset(arch);
  Reset(arch2);
  While not eof(arch) do
   begin
     Readln(arch,aux.codart);
     Readln(arch,aux.talle);
     Readln(arch,aux.color);
     Readln(arch,aux.cantp);
     Readln(arch,aux.precio);
     Write(arch2,aux);
   end;
  aux.codart:='ZZZZ';
  Read(arch2,aux);
  Readln();
 Close(arch);
 Close(arch2);

end.

