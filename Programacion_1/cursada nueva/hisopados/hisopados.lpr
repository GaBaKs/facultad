program hisopados;
 const
   max=40;
 type
   st6=string[6];
   Tvecst=array[1..max] of st6;
   Tvecr=array[1..max] of real;
 procedure lectura(var vecod:Tvecst;var vecigg:Tvecr;var vecigm:Tvecr;var i:byte);
  var
    arch:text;
    aux,sn:char;
  begin
    i:=1;
    Assign(arch,'HISOPADOS.TXT');
    Reset(arch);
    While not eof(arch)do
     begin
      read(arch,vecod[i],aux,sn);
      if upcase(sn)='S' then
       begin
        readln(arch,aux,vecigg[i],vecigm[i]);
        i:=i+1;
        end
      else readln(arch);
  end;
    i:=i-1;
  Close(arch);
end;

function incisoa1(x:real;vecigg:Tvecr;i:byte):byte;
var
  j,cont:byte;
 begin
 cont:=0;
  for j:=1 to i do
    if vecigg[j]>x then
     cont:=cont+1;
  incisoa1:=cont;
 end;

function incisoa2(y:real;vecigm:Tvecr;i:byte):byte;
var
  j,cont:byte;
 begin
 cont:=0;
  for j:=1 to i do
    if vecigm[j]>y then
     cont:=cont+1;
  incisoa2:=cont;
 end;

procedure incisob(vecod:Tvecst;vecigg:Tvecr;vecigm:Tvecr;i:byte);
 var
   j:byte;
   K:shortstring;
 begin
  repeat
  Writeln('ingrese un codigo de paciente');
  Readln(K);
  until Length(K)=6;
  j:=0;
  While (vecod[j]<>K) and (j<=i) do
   begin
    j:=j+1;
    if k=vecod[j] then
     Writeln('El igg del paciente ',K,' es de ',vecigg[j]:2:2,' y su igm es de ',vecigm[j]:2:2);
    end;
  if j>i then
   Writeln('no existe ningun paciente con el codigo ',K);
 end;

function incisoc(vecigg,vecigm:Tvecr;i:byte):real;
 var
  j:byte;
  cont:byte;
  porcentaje:real;
 begin
 cont:=0;
 for j:=1 to i do
  if vecigm[j]>vecigg[j] then
   cont:=cont+1;
  porcentaje:=((cont/i)*100);
  incisoc:=porcentaje;
 end;


var
  x,y:real;
  vecod:Tvecst;
  vecigg,vecigm:Tvecr;
  i:byte;
begin
Writeln('ingrese un valor de IGG a superar');
Readln(x);
Writeln('ingrese un valor de IGM a superar');
Readln(y);
lectura(vecod,vecigg,vecigm,i);
Writeln('la cantidad de pacientes que tuvieron un IGG superior a ',x:2:2,' es de ',incisoa1(x,vecigg,i));
Writeln('la cantidad de pacientes que tuvieron un IGG superior a ',y:2:2,' es de ',incisoa2(y,vecigm,i));
incisob(vecod,vecigg,vecigm,i);
Writeln('El porcentaje de pacientes que obtuvieron un IGM superior a su IGG es de ',incisoc(vecigg,vecigm,i):2:2,'%');
Readln();
end.

