program parcialnashe;
const
  max=30;
 type
   st10=string[10];
   st4=string[4];
   tvecr=array[1..max]of record
     tipo:st10;
     precio:word;
   end;
   tvec=array[1..max]of st4;
   tm=array[1..max,1..max] of byte;
   end;


 procedure lecturaventas(var vec:tvecs;var n:byte);
   var
   arch1:text;
   i:byte;
 begin
  Assign(arch1,'Ventas.TXT');
  Reset(arch1);
  Readln(arch,N);
  i:=0;
  while not eof(arch1) do
   begin
    i:=i+1;
    readln(arch,vec[i].tipo,vec[i].precio);
   end;
 end;
procedure lecturacombustible(var mat:tm;var vec2:tvec;i:byte)
 var
  m:byte;
  arch2:text;
begin
 i:=0;
 m:=0;
 Assign(arch2,'combustibles.TXT');
 reset(arch2);
 while not eof(arch2) do
  begin
   i:=i+1;
   read(arch2,vec2);
  while not eoln(arch) do
   begin
    m:=m+1;
    read(arch2,mat[i,m]);
   end;
   readln(arch2);
   m:=0;
   end;
 end;
function masl(mat:tm;n:byte;i:byte):st10;
var
 maxim:byte;
 begin
  if n>0 then
   begin
     maxim:=masl(mat,n-1,i);
     if maxim< masl[i,n]; then
      maxim:=mat[i,n];
 procedure auxmax(i:byte;vec2:tvec)
   var
    c:st4;
   s:byte;
   begin
   repeat
    Writeln('ingrese un codigo de surtidor');
    Readln(C);
    While s<=i and vec2[s]<>C do
     s:=s+1;
    until s<i;
    Writeln('en el surtidor ',vec2[s],'el combustible mas vendido fue ',masl


var
 C:st4;
 mat:tm;
 vec2:tvec;
 vec:tvecs;
 n:byte;
begin

end.

