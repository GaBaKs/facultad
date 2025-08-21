program parcial752021;
 const
   max=30;
 type
   vecst=array[1..max]of string;
   vecint=array[1..max]of word;

 procedure leerarchivo(var VNom:Vecst;var VApuntes:vecint;var VTareas:vecint;var VForos:vecint;var N:byte);
 var
  Arch: text;
  nombre: string;
  letra,aux: char;
  x,cant: integer;
begin
   Writeln('escriba X');
 Readln(X);
  Assign(Arch,'encriptado.TXT');
  Reset(Arch);
  N:=0;
  While not eof(arch) do
   begin
    While letra<>'.' do
     begin
      Read(Arch,letra);
      if letra in ['A'..'Z'] then
        nombre:=nombre+letra;
       end;

      Read(arch,cant);

      if cant<X then
       begin
        N:=N+1;
        Read(Arch,VApuntes[N]);
        Read(Arch,VTareas[N]);
        Read(Arch,VForos[N]);
        VNom[N]:=nombre;

       end;
    Readln(arch,aux);
    letra:=' ';
    nombre:='';
   end;
  close(arch);
  end;
 procedure portareas(VNom:Vecst;VApuntes:vecint;VTareas:vecint;VForos:vecint;N:byte);
  var
   i:byte;

  begin
    for i:=1 to N do
    begin
    Writeln('alumno: ',VNom[i],' cantidad total de accesos: ',VApuntes[i]+VTareas[i]+VForos[i]);
    Writeln('porcentaje correspondientes a tareas: ',Vnom[i],' ',(100*VTareas[i]/(VApuntes[i]+VTareas[i]+VForos[i])):8:2,'%');
    end;
    end;
 function rango(VApuntes:vecint;VTareas:vecint;VForos:vecint;N:byte;E1:word;E2:word):real;
 var
  i:byte;
  suma,acum,cont:word;
  begin
    cont:=0;
    acum:=0;
    for i:=1 to N do
     begin
     suma:=0;
    suma:=VApuntes[i]+VTareas[i]+VForos[i];
     if (suma<=E2) and (suma>=E1) then
      begin
      cont:=cont+1;
      acum:=acum+VTareas[i];
      end;
     end;
    if cont<>0 then
    rango:=(acum/cont)
    else rango:=0;
  end;



function actareas(VNom:Vecst;VApuntes:vecint;VTareas:vecint;VForos:vecint;N:byte):string;
var
 i,max: word;
 test:byte;
  begin
    max:=0;
    for i:=1 to N do
     begin
     if VForos[i]=0 then
      begin
      test:=VTareas[i];
     if test>max then
     begin
     max:=test;
     actareas:=VNom[i];
     end;
      end;
      end;
  end;

var
  E1,E2:word;
  Vnom:vecst;
  vapuntes:vecint;
  vtareas:vecint;
  vforos:vecint;
  N:byte;
begin
 leerarchivo(VNom,VApuntes,VTareas,VForos,N);
 portareas(VNOM,VAPUNTES,VTAREAS,VFOROS,N);
 Writeln('escribir rango(escribir un numero, enter y luego el siguiente)');
 Readln(E1,E2);
 Writeln('el promedio general de acceso a las tareas es de ',rango(VAPUNTES,VTAREAS,VFOROS,N,E1,E2):8:2);
 Writeln('el alumno con max acceso a tareas sin entrar al foro es ',actareas(VNom,VApuntes,VTareas,VForos,N));
 Readln();
end.

