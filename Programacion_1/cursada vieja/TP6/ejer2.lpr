program ejer2;
type
  st20=string[20];
  vec=array[1..20] of st20;
  mat=array[1..20,1..20] of real;
 procedure leerarch(var vecN:vec;var notas:mat;var i:byte;var K:byte);
  var
    nota:real;
    bool: boolean;
    j: byte;
    arch:text;
    nom:st20;
    car:char;
  begin
    nom:='';
    bool:=false;
    i:=1;
    j:=1;
    Assign(arch,'ejer2.TXT');
    Reset(arch);
    while not(eof) do
     begin
     if bool=false then
     begin
      read(arch,car);
      if car=' ' then
         bool:=true
      else
        while car<>' ' do
         begin
          nom:=nom+car;
          Read(arch,car);
         end;
         vecN[i]:=nom;
         while not (eoln) do
          begin
           Read(arch,nota);
           if (nota<0) or (nota>10) then
            bool:=true;
           notas[i,j]:=nota;
           j:=j+1;
          end;
         K:=j;
         i:=i+1;
         j:=1;
         Readln(arch,nom);
         end;
     end;
    if bool=true then
     Writeln('uno de los datos ingresados es incorrecto');
    end;
    var
    vecN:vec;
    notas:mat;
    K,i:byte;
    begin
     leerarch(vecN,notas,i,K);
     Writeln('nashe');
     readln();
    end.


