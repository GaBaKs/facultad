program ejer23;
 var
   arch:text;
   flag,mayus,minus:boolean;
   long,contdig,continv,contot,maxlong:byte;
   porinv:real;
begin
  Assign(arch,'ejer23.TXT');
  Reset(arch);
  flag=false;
  long:=0;
  contdig:=0;
  mayus:=false;
  minus:=false;
  continv:=0;
  contot:=0;
  While not eof(arch) do
   begin
    repeat
     Read(arch,char);
    until char<>' ';
    While char<>' ' do
     begin
       While not flag do
        begin
           case char of
            'a'..'z':long:=long+1; minus:=true;
            'A'..'Z':long:=long+1; mayus:=true;
            '0'..'9':long:=long+1; contdig:=contdig+1;
            else flag=true
           end;
        end;
       Read(arch,char);
     end;
    if not(flag) and (minus) and (mayus) and (contdig=4) and (long>=8) then
     contot:=contot+1
    else
     begin
      continv:=continv+1;
      contot:=contot+1;
      if maxlong<long then
       maxlong:=long;
     end;
      flag:=false;
      long:=0;
      minus:=false;
      mayus:=false;
      contdig:=0;
   end;
  porinv:=(continv/contot)*100;
  Writeln('El % de contraseñas invalidas es de ',porinv:2:2;
  Writeln('La longitud de la contraseña invalida mas larga es de ',maxlong, ' caracteres.');
  Readln();
end.

