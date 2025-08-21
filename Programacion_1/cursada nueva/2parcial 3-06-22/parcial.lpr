program parcial;
uses
 sysutils;
 const
   max=100;
   tri=4;
   esc=6;
  type
    st15=string[15];
    Tmat=array[1..max,1..max] of word;
    Tvecr=array[1..max] of record
      anios:word;
      total:real;
    end;
    Tvecr2=array[1..max] of record
      nombre:st15;
      cant:real;
    end;

 procedure lecturaturistas(var matmayores:Tmat;var matmenores:Tmat;var N:byte);
  var
   arch:text;
   i,j:byte;
   aux:word;
  begin
   Assign(arch,'TURISTAS.TXT');
   Reset(arch);
   Readln(arch,N);
   for i:=1 to N do
    begin
     for j:=1 to tri do
       Read(arch,matmayores[i,j]);
     for j:=1 to tri do
      Read(arch,matmenores[i,j]);
     Readln(arch);
    end;
   close(arch);
end;
procedure lecturaescalas(var vecescalas:Tvecr2);
 var
   i:byte;
   arch:text;
 begin
  Assign(arch,'ESCALAS.TXT');
  Reset(arch);
  for i:=1 to esc do
    begin
     Readln(arch,vecescalas[i].nombre,vecescalas[i].cant);
     vecescalas[i].nombre:=trim(vecescalas[i].nombre);
    end;
  Close(arch);
 end;

 function buscarescala(X:st15;vecescalas:Tvecr2):real;
  var
   i:byte;
  begin
   i:=0;
   While (i<esc) and (vecescalas[i].nombre<>X) do
   begin
     i:=i+1;
     if vecescalas[i].nombre=X then
      buscarescala:=vecescalas[i].cant;
   end;
   if i>esc then
    buscarescala:=0;
  end;
 procedure generararregloa(matmayores,matmenores:Tmat;N:byte;vecescalas:Tvecr2;var vectotx:Tvecr;Var H:byte);
  var
   X:st15;
   maxx:real;
   cont:byte;
   acum:real;
   i,j:byte;
 begin
  cont:=0;
  H:=0;
  acum:=0;
  Writeln('ingrese una escala');
  Readln(X);
  maxx:=buscarescala(X,vecescalas);
if maxx<>0 then
 begin
  for i:=1 to N do
   begin
    for j:=1 to tri do
     begin
      acum:=acum+(matmayores[i,j]+matmenores[i,j])*1000;
      if (matmenores[i,j]+matmayores[i,j])*1000>=maxx then
       cont:=cont+1;
     end;
    if cont>=2 then
     begin
      H:=H+1;
      vectotx[H].anios:=2022-i;
      vectotx[H].total:=acum;
     end;
   acum:=0;
   cont:=0;
   end;
end
else Writeln('el codigo X ingresado no es valido');
end;

 procedure mostrararregloa(vectotx:Tvecr;H:byte);
 var
  i:byte;
 begin
  for i:=1 to H do
   Writeln('ANIO: ',vectotx[i].anios,' Cantidad de turistas: ',vectotx[i].total:2:2);
end;

 procedure trimestremenb(matmayores,matmenores:Tmat;i,j,N:byte;var imin:byte;var jmin:byte;trimin:real);

  begin
   if j>0 then
     if i>0 then
      begin
       if matmayores[i,j]+matmenores[i,j]<trimin then
        begin
         imin:=i;
         jmin:=j;
         trimin:=matmayores[i,j]+matmenores[i,j];
        end;
       trimestremenb(matmayores,matmenores,i-1,j,N,imin,jmin,trimin);
       end
       else trimestremenb(matmayores,matmenores,N,j-1,N,imin,jmin,trimin);
 end;

 function regfam(matmayores,matmenores:Tmat;i,j:byte):byte;

  begin
   if i=0 then
    regfam:=0
   else
      begin
           if i>0 then
             if matmenores[j,i]>=matmayores[j,i] then
              begin
              regfam:=1+regfam(matmayores,matmenores,i-1,j)
              end
            else regfam:=regfam(matmayores,matmenores,i-1,j);
       end;
 end;

 procedure incisoc(matmayores,matmenores:Tmat;N:byte);
  var
   K:word;
   porcentaje:real;

  begin
   Writeln('ingrese un Anio K');
   Readln(K);
   if (K<=2021) and (K>=2022-N) then
    begin
      porcentaje:=(regfam(matmayores,matmenores,tri,2022-K)/tri)*100;
      Writeln('el porcentaje de registros de tipo familiar en el anioo ',K,' es de ',porcentaje:2:2,'%');
    end
   else Writeln('el anio ingresado no es valido');
  end;


 var
  matmayores,matmenores:Tmat;
  N,H:byte;
  X:st15;
  vecescalas:Tvecr2;
  vectotx:Tvecr;
  i,j,imin,jmin:byte;
  trimin:real;
  aniotri:word;

begin
  lecturaturistas(matmayores,matmenores,N);
  lecturaescalas(vecescalas);
  generararregloa(matmayores,matmenores,N,vecescalas,vectotx,H);
  mostrararregloa(vectotx,H);
  trimestremenB(matmayores,matmenores,N,tri,N,imin,jmin,100000);
  aniotri:=2022-imin;
  Writeln('el trimestre con menor asistencia es el ',jmin,' del anio ',aniotri);
  incisoc(matmayores,matmenores,N);
  Readln();

end.

