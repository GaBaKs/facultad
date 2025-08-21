program ejer1;
 var
  car:char;
 function letrasn(car:char):boolean;
  begin
    case car of
    'a'..'z': letrasn:=true;
    'A'..'Z': letrasn:=true;
    else letrasn:=false;
    end;
  end;

begin
  Writeln('ingrese un caracter');
  Readln(car);
  if letrasn(car) then
   Writeln('el caracter ingresado es una letra')
  else Writeln('el caracter ingresado no es una letra');
  readln();
end.

