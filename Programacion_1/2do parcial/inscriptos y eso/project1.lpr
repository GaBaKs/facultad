program project1;
 const
   max=30
 type
  st30=string[30];
  st2=string[2];
  tvec=array[1..max]of st2;
  tmat=array[1..max,1..max] of byte;
 procedure leerinscriptos(var codprov:tvec;var mret:tmat;
 var
  arch:text;
  edad:byte;
  cod:st2;
  doc:word;
 aux:char;
 i:byte
 begin
 assign(arch,'inscriptos.TXT');
 reset(arch);
 Readln(arch,doc,edad,,
 mret[edad]:=mret[edad]+1;
begin
end.

