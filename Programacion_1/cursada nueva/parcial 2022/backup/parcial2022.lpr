program parcial2022;
const
  max=100;
type
  st8=string[8];
  st30=string[30];
  Tvecst8=array[1..max]of st8;
  st2=string[2];
  Tvecst2=array[1..max] of st2;
  Tvecbyte=array[1..max] of byte;
  Tvecword=array[1..max]of word;
  Tvecst30=array[1..max]of st30;
  Tvechar=array[1..max] of char;
  Tvecreal=array[1..max] of real;
 procedure lectura1(var Vcod:Tvecst2;var Vcanth:Tvecbyte;var Vingre:Tvecword;var N:byte);
  var
   arch:text;
   sn:char;
  aux:char;
 begin
  N:=1;
  Assign(arch,'CENSO.TXT');
  Reset(arch);
  While not eof(arch) do
   begin
    Read(arch,aux,aux,aux,aux,aux,aux,Vcod[N],aux,sn);
    If upcase(sn)='S' then
     begin
      Readln(arch,aux,Vcanth[N],aux,Vingre[N]);
      N:=N+1;
     end
    else Readln(arch);
   end;
 Close(arch);
 end;

 procedure lectura2(var Vcodprov:Tvecst2;var Vnomprov:Tvecst30;var Vcodreg:Tvechar;var Vcanth2010:Tvecbyte;var i:byte);
 var
  arch:text;
  aux:char;
  restpal:st30;
 begin
 i:=1;
  Assign(arch,'PROVINCIAS.TXT');
  Reset(arch);
  While not eof(arch) do
   begin
     Read(arch,Vcodprov[i],aux,Vnomprov[i],aux);
     Read(arch,aux);
     Writeln(Vnomprov[i]);
     if aux<>' ' then
     begin
      Read(arch,restpal);
      Vnomprov[i]:=Vnomprov[i]+' '+aux+restpal;
     end;
      While (upcase(aux)<>'C') and (upcase(aux)<>'S') and (upcase(aux)<>'N') do
       Read(arch,aux);
      Vcodreg[i]:=aux;
      Writeln(Vcodreg[i]);
      Readln(arch,aux);
      i:=i+1;
   end;
   Close(arch);
 end;

 procedure incisoa(Vcod:Tvecst2;Vcanth:Tvecbyte;N:byte;Vcodprov:Tvecst2;Vcodreg:Tvechar;i:byte);
 var
  j,k:byte;
  conthabC,conthabN,conthabS:word;
  flag:boolean;
 begin
 flag:=false;
 k:=1;
 conthabC:=0;
 conthabN:=0;
 conthabS:=0;
  for j:=1 to N do
   begin
    While (not(flag)) and (k<=i)do
     begin
      if Vcod[j]=Vcodprov[k] then
       begin
        case upcase(Vcodreg[k]) of
         'C':conthabC:=conthabC+Vcanth[j];
         'N':conthabN:=conthabN+Vcanth[j];
         'S':conthabS:=conthabS+Vcanth[j];
         else Writeln('algo mal hiciste flaco');
        end;
        flag:=true;
       end;
      K:=K+1;
     end;
     flag:=false;
     K:=1;
   end;
 Writeln('La cantidad de habitantes censados en cada region es de: ');
 Writeln('Centro: ',conthabC);
 Writeln('Norte: ',conthabN);
 Writeln('Sur: ',conthabS);
 end;

function incisob(Vcod:Tvecst2;Vingre:Tvecword;N:byte;Vcodprov:Tvecst2;Vnomprov:Tvecst30;i:byte;Vacum:Tvecbyte;Vsuma:Tvecword):st30;
var
 j,k:byte;
 flag:boolean;
 maximo:real;
 espacio:byte;
 Vpromedios:Tvecreal;
begin
k:=1;
maximo:=0;
flag:=false;
 for j:=1 to N do
  begin
   While (not(flag)) and (k<=i) do
    begin
     if Vcod[j]=Vcodprov[k] then
      begin
       Vsuma[k]:=Vsuma[k]+Vingre[j];
       Vacum[k]:=Vacum[k]+1;
       flag:=true
      end
      else k:=k+1;
    end;
   flag:=false;
   k:=1;
   end;
//calc de promedios
  for k:=1 to i do
   begin
    if Vacum[k]<>0 then
     Vpromedios[k]:=Vsuma[k]/Vacum[k]
    else Vacum[k]:=0;
   if maximo<Vpromedios[k] then
    begin
     maximo:=Vpromedios[k];
     espacio:=k;
    end;
   end;
   incisob:=Vnomprov[espacio];
 end;
 var
  Vcod,Vcodprov:Tvecst2;
  Vcanth:Tvecbyte;
  Vingre:Tvecword;
  N,i:byte;
  Vnomprov:Tvecst30;
  Vcodreg:Tvechar;
  Vcanth2010:Tvecbyte;
  Vacum:Tvecbyte;
  Vsuma:Tvecword;
begin
 lectura1(Vcod,Vcanth,Vingre,N);
 Writeln('hola');
 lectura2(Vcodprov,Vnomprov,Vcodreg,Vcanth2010,i);
 incisoa(Vcod,Vcanth,N,Vcodprov,Vcodreg,i);
 Writeln('el nombre de la provincia con mayor ingreso promedio por vivienda es: ',incisob(Vcod,Vingre,N,Vcodprov,Vnomprov,i,Vacum,Vsuma));
 Readln();
end.
