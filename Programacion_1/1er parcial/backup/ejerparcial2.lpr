program parcial752021;
 const
   max=30;
 type
   vecst=array[1..max]of string;
   vecint=array[1..max]of word;

 procedure leerarchivo(var VNom:Vecst;var VApuntes:vecint;var VTareas:vecint;var VForos:vecint;X:word;var N:byte);
 var
  Arch: text;
  nombre: string;
  letra: char;
  dias: integer;
begin
  Assign(Arch;encriptado.TXT);
  Reset(Arch);
  While not eof(arch) do
   begin
    N:=1;
    While arch<>'.' do
     begin
      Read(Arch,letra);
      if letra in ['A'..'Z'] then
       begin
        nombre:=nombre+letra;
       end;
        Read(Arch);
        Read(arch,dias);
       end;
      if dias<X then
       begin
        Read(arch);
        Read(Arch,VApuntes[N]);
        Read(arch);
        Read(Arch,VTareas[N]);
        Read(arch);
        Read(Arch,VForos[N];
        VNom[N]:=nombre;
        N:=N+1;
       end;
    Readln(arch);
   end;
  end;
 procedure portareas(VNom:Vecst;VApuntes:vecint;VTareas:vecint;VForos:vecint;N:byte);
  var
   i:byte;

  begin
    for i:=1 to N do
    Writeln('alumno: ',VNom[i],' cantidad total de accesos: ',VApuntes[i]+VTareas[i]+VForos[i]);
    Writeln('porcentaje correspondientes a tareas: ',(VTareas[i]/(VApuntes[i]+VTareas[i]+VForos[i])*100):8:2,'%');
  end;
 function rango(VNom:Vecst;VApuntes:vecint;VTareas:vecint;VForos:vecint;N:byte;E1:word;E2:word):real;
 var
  i:byte;
  suma,acum,cont:word;
  begin
    cont:=1;
    acum:=0;
    for i:=1 to N do
     begin
    suma:=VApuntes[i]+VTareas[i]+VForos[i];
     if (suma<E2) and (suma>E1) then
      cont:=cont+1;
      acum:=acum+VTareas[i];
     end;
    rango:=(acum/cont)*100;
  end;



var
  x,E1,E2:word;
begin
 Writeln('escriba X');
 Readln(X);
 leerarchivo(VNOM,VAPUNTES,VTAREAS,VFOROS,X);
 portareas(VNOM,VAPUNTES,VTAREAS,VFOROS,N);
 Writeln('escribir rango(escribir un numero, enter y luego el siguiente)');
 Readln(E1,E2);
 Writeln('el promedio general de acceso a las tareas es de ',rango(VNOM,VAPUNTES,VTAREAS,VFOROS,N,E1,E2),'%');
end;

