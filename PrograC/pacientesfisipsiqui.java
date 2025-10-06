//en la clase paciente

public class Paciente implements Cloneable
 @override
    public Object clone() throws CloneNotSupportedException{
        Paciente pacienteclon=null;
        pacienteclon=(Paciente)super.clone();
        return pacienteclon;
        if (pacienteclon!=null){
            pacienteclon.enfermedad=(enfermedad)this.paciente.clone();
        }
        return pacienteclon;
    }

// en enfermedad

 @override
    public Object clone() throws CloneNotSupportedException{
        Enfermedad enfermedadclon=null;
        enfermedadclon=(Enfermedad)super.clone();

    }


// en enfermedad fisica
    @override
        public Object clone(){
            try{
                Enfermedad_fisica enfclon=null;
                enfclon=(Enfermedad_fisica)super.clone;
                return enfclon;
            }
            catch(CloneNotSupportedException e){
                
            }
        }


// en enfermedad psiquica

@override
    public Object clone() throws CloneNotSupportedException{
        throw CloneNotSupportedException;
    }