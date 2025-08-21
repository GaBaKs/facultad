program ejer1;
 function bolean(letra:char):boolean;
  begin
    case letra of
     'a'..'z':bolean:=true;
     'A'..'Z':bolean:=true;
     else bolean:=false;
    end;
  end;
 var
   letra:Char;
begin
  Writeln('ingrese un caracter');
  Readln(letra);
  If bolean(letra)=true then
   Writeln('el caracter ingresado es una letra')
  else Writeln('el caracter ingresado no es una letra');
  Readln();
end.

