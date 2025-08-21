program ejerparcial1;
 const
   max=20;
Type
  st4=string[4];
  vecst=array[1..max] of string;
  vecint=array[1..max] of integer;
  vecreal=array[1..max] of real;
  procedure Leerarchivo(var VCOD:vecst;var VTOT:vecint;var VPROM:vecreal;var N:integer);
   var
     arch: text;
     lts,contdias: integer;
     char1:char;
    begin
     N:=1;
     contdias:=-1;
     Assign(arch,'text.TXT');
     Reset(arch);
     While not eof(arch) do
      begin
       repeat
         Read(arch,char1);
         VCOD[N]:=VCOD[N]+char1;
       until eoln(arch);
      Readln(arch);
      repeat
        Read(arch,lts);
         VTOT[N]:=VTOT[N]+lts;
         contdias:=contdias+1;
         Read(arch);
       until lts=0;
      Readln(arch);
      VPROM[N]:=VTOT[N]/contdias;
      N:=N+1;
      contdias:=-1;
      end;
      Close(arch);
     end;
function Maxleche(VCOD:vecst;VTOT:vecint;N: integer): string;
var
  i,max: integer;
 begin
  max:=1;
  for i:=1 to N-1 do
   begin
   if VTOT[i]>max then
    begin
     max:=VTOT[i];
     Maxleche:=VCOD[i];
    end;
    end;
  end;
function cantpromX(VPROM:vecreal;N:integer;prom:integer): integer;
 var
   i,cont:integer;
 begin
  cont:=0;
  for i:=1 to N-1 do
   begin
    if VPROM[i]>prom then
     cont:=cont+1;
   end;
  cantpromX:=cont
 end;
procedure dadocodigo(VCOD:vecst;VTOT:vecint;VPROM:vecreal;N:integer);
 var
   cod: st4;
   i: integer;
   val:st4;
 begin

  repeat
  i:=1;
  Writeln('ingrese un codigo(4 caracteres)');
  Readln(cod);
  While (cod<>VCOD[i]) and (i<>N) do
    i:=i+1;
  if cod=VCOD[i] then
   Writeln('codigo: ',VCOD[i],'   total: ',VTOT[i],'   promedio diario: ', VPROM[i]:8:2)
  else Writeln('el codigo no pertenece a ningun tambo');
  Writeln('quiere seguir buscando?(escriba no para dejar de buscar');
  Readln(val);
  val:=UPCASE(val);
  until val='NO';
 end;
var
  N,i,prom:integer;
  VCOD:vecst;
  VTOT:vecint;
  VPROM:vecreal;
  cod:st4;
begin  {inicio del programa}
  Leerarchivo(VCOD,VTOT,VPROM,N);
  Writeln('el tambo que mas leche entrego fue ',Maxleche(VCOD,VTOT,N));

  Writeln('coloque un promedio de litros a superar');
  Readln(prom);

  Writeln(cantpromX(VPROM,N,prom),' tambo/s superaron el promedio ',prom);

  dadocodigo(VCOD,VTOT,VPROM,N);
end.
