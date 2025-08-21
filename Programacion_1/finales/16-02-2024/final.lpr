program final;
const
  max=30;
 type
  st3=string[3];
  st4=string[4];
  st15=string[15];
  st8=string[8];
  TR=record
    leg:st4;
    nombre:st15;
    sueldo:real;
  end;
 FTR=file of TR;
 TR2=record
   leg:st4;
   fecha:st8;
   canth:byte;
   codp:st3
 end;
FTR2=file of TR2;
TR3=record
  codigo:st3;
  desc:st15;
  valh:real;
  end;
FTR3=file of TR3;
Tvec=array[1..max] of record
  codigo:st3;
  desc:st15;
  valh:real;
  canth:byte;
  monto:real;
  end;
procedure generarvector(var vec:Tvec;var i:byte;var arch3:FTR3);
 var
  aux:TR3;
 begin
   reset(arch3);
   i:=0;
   While not eof(arch3) do
    begin
      read(arch3,aux);
      i:=i+1;
      vec[i].codigo:=aux.codigo;
      vec[i].desc:=aux.desc;
      vec[i].valh:=aux.valh;
    end;
 end;
procedure cargavector(var vec:Tvec;i:byte);
 var
  j:byte;
  begin
    for j:=1 to i do
     begin
       vec[j].canth:=0;
       vec[j].monto:=0;
     end;
 end;

function busqueda(vec:Tvec;i:byte;codp:st3):byte;
 var
  aux3:TR3;
  j:byte;
 begin
   j:=1;
  While codp<>vec[j].codigo do
    j:=j+1;
   busqueda:=j;
 end;

 procedure proceso(var arch:FTR;var arch2:FTR2;var vec:Tvec;i:byte);
   var
    aux:TR;
    aux2:TR2;
    pos:byte;
    codp:st3;
    erroneo,notrabajo:byte;
    legajo:st4;
   begin
        Reset(arch);
        Reset(arch2);
        read(arch,aux);
        read(arch2,aux2);
        erroneo:=0;
        notrabajo:=0;
       While (not eof(arch)) and (not eof(arch2)) do
        begin
       if aux.leg=aux2.leg then
          begin
            seek(arch,filepos(arch)-1);
            While aux.leg=aux2.leg do
              begin
                codp:=aux2.codp;
                delete(aux2.fecha,1,6);
                if aux2.fecha<='15' then
                 begin
                   vec[busqueda(vec,i,codp)].canth:=vec[busqueda(vec,i,codp)].canth+aux2.canth;
                   vec[busqueda(vec,i,codp)].monto:=vec[busqueda(vec,i,codp)].monto+aux2.canth*vec[busqueda(vec,i,codp)].valh;
                 end;
                aux.sueldo:=aux.sueldo+aux2.canth*vec[busqueda(vec,i,codp)].valh;
                write(arch,aux);
                read(arch2,aux2);
              end;
            read(arch,aux);
           end
          else
           if aux.leg<aux2.leg then
             begin
              notrabajo:=notrabajo+1;
               read(arch,aux);
             end
           else
               if aux.leg>aux2.leg then
                 begin
                   erroneo:=erroneo+1;
                   legajo:=aux2.leg;
                   While aux2.leg=legajo do
                     read(arch2,aux2);
                 end;
        end;
       Writeln(notrabajo,' empleado/s no trabajo/trabajaron.');
       Writeln('hubieron ',erroneo,' legajos erroneos.');
 end;
 procedure listado(vec:Tvec;i:byte);
  var
   j:byte;

  begin
    Writeln('Codigo pozo     Descripcion       Can de horas 1 quin              Monto total 1quin');
    for j:=1 to i do
     Writeln(vec[j].codigo,'             ',vec[j].desc,'                   ',vec[j].canth,'                        ',vec[j].monto:6:2);
  end;

var
 vec:Tvec;
 i:byte;
 arch:FTR;
 arch2:FTR2;
 arch3:FTR3;


begin
  Assign(arch,'EMPLEADOS.DAT');
  Assign(arch2,'HORASTRABAJO.DAT');
  Assign(arch3,'POZOPETROLEO.DAT');
  generarvector(vec,i,arch3);
  cargavector(vec,i);
  proceso(arch,arch2,vec,i);
  listado(vec,i);
  Readln();
end.

