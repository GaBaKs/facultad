program ejer5;
const
bal = 0.0625;
L = 10;
A = 30;
var
N,M,sup,cantbal : real ;
begin
  repeat
    Writeln('Escriba el largo N');
    Readln(N);
    Writeln('Escriba el ancho M');
    Readln(M);
    until (M<=30) and (N<=10) and (M>0) and (N>0);
   sup := (N*M*100)/(L*A);
   cantbal := round((N*M)/bal) ;
   Writeln('los datos ingresados representan el',sup:7:2,'% de la superficie total y se necesitan',cantbal:5:0,' baldosas');
   Readln;
end.

