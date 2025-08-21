program ejer7;
 const
   max=100;

 type
   Tmat=array [1..max,1..max] of word;

procedure lectura(var N:byte;var M:byte;var matas:Tmat;var matdes:Tmat);
 var
   arch:text;
   i,j:byte;
 begin
 N:=0;
 M:=0;
   Assign(arch,'ejer7.TXT');
   Reset(arch);
   While not eof(arch) do
   begin
    Read(arch,i,j);
    Readln(arch,matas[i,j],matdes[i,j]);
    if i>N then
     N:=i;
    if j>M then
     M:=j;
   end;
   Close(arch);
 end;

function incisoa(matdes:Tmat;N,M:byte):byte;
 var
 i,j:byte;
 suma,sumamax:word;

 begin
   suma:=0;
   sumamax:=0;
   for i:=1 to N do
    begin
    for j:=1 to M do
    suma:=suma+matdes[i,j];
    if suma>sumamax then
     begin
       incisoa:=i;
       sumamax:=suma;
     end;
    suma:=0;
    end;
 end;
   function incisob(matas:Tmat;N,M:byte):byte;
    var
    i,j:byte;
    suma,sumamin:word;

    begin
      suma:=0;
      sumamin:=0;
      for j:=1 to M do
       begin
       for i:=1 to N do
       suma:=suma+matas[i,j];
       if suma<sumamin then
        begin
          incisob:=j;
          sumamin:=suma;
        end;
       suma:=0;
       end;
 end;

  var
  matas,matdes:Tmat;
  N,M:byte;
 begin
   lectura(N,M,matas,matdes);
   Writeln('la parada donde mas pasajeros bajan es ',incisoa(matdes,N,M));
   Writeln('la linea con menos cantidad de pasajeros que subieron es ',incisob(matas,N,M));
   Readln();
end.

