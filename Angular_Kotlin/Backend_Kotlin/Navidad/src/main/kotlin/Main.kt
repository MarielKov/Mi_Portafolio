package ar.edu.unsam.algo2.navidad

import java.time.DayOfWeek
import java.time.LocalDate

object personaMisteriosa{

    var listaDeRegalos : MutableList<Regalo> = mutableListOf()

    lateinit var regaloDeEmergencia : Regalo

    fun crearRegalo(regalo: Regalo) {
        listaDeRegalos.add(regalo)
    }



    fun darRegalo(persona: Persona) {
        if(siSeEncuentraUnElemento(persona)){
            persona.regalar(devolverPrimerElemento(persona))
        }
        else{
            regaloDeEmergencia = Voucher()
            persona.regalar(regaloDeEmergencia)
        }
    }

    fun devolverPrimerElemento(persona: Persona) = listaDeRegalos.first{regalo -> preguntarSiLeGusta(persona,regalo)}

    fun siSeEncuentraUnElemento(persona: Persona) = listaDeRegalos.any{regalo -> preguntarSiLeGusta(persona,regalo)}

    fun preguntarSiLeGusta(persona: Persona, regalo: Regalo) = persona.tipoDePersona.leGusta(regalo)

}

class Persona(val tipoDePersona: TipoDePersona){

    lateinit var obsequio: Regalo

    fun regalar(regalo: Regalo){
        if (condicion(regalo)){
            obsequio = regalo
        }
    }

    fun condicion(regalo: Regalo) = tipoDePersona.leGusta(regalo)
}

interface TipoDePersona{

    fun leGusta(regalo: Regalo) : Boolean

}

class Conformista:TipoDePersona{

    override fun leGusta(regalo: Regalo) = true
}

class Interesada(val precioMinimo : Double):TipoDePersona{

    override fun leGusta(regalo: Regalo) = precioMinimo>=regalo.precio

}

class Exigente:TipoDePersona{

    override fun leGusta(regalo: Regalo) = regalo.esValioso()
}

class Marquera(val marcaPreferida : String):TipoDePersona{

    override fun leGusta(regalo: Regalo): Boolean = marcaPreferida == regalo.marca
}

class Combineta (marcaPreferida : String, precioMinimo : Double):TipoDePersona{

    val listaTipos : List<TipoDePersona> = mutableListOf(Marquera(marcaPreferida),Exigente(),Conformista(),Interesada(precioMinimo))

    override fun leGusta(regalo: Regalo): Boolean = listaTipos.any { t -> t.leGusta(regalo) }

}

interface Regalo{

    val marca : String
    val precio : Double

    fun esValioso() : Boolean = precio >= 5000 && condicionValioso()

    fun condicionValioso() : Boolean

}

class Ropa(override val marca: String, override val precio: Double) : Regalo {

    val marcasValiosas : List<String> = listOf("Jordache","Lee","Charro","Motor Oil")

    override fun condicionValioso(): Boolean = marcasValiosas.any { m -> m == marca }

}

class Perfume(override val marca: String, override val precio: Double, val esExtranjero : Boolean): Regalo {
    override fun condicionValioso(): Boolean = esExtranjero
}

class Juguete(override val marca: String, override val precio: Double,
              val fecha : LocalDate): Regalo {
    override fun condicionValioso(): Boolean = fecha.year < 2000
}

class Experiencia(override val marca: String, override val precio: Double,
                  val fecha : LocalDate): Regalo {
    override fun condicionValioso(): Boolean = fecha.dayOfWeek == DayOfWeek.FRIDAY
}

class Voucher : Regalo{

    override val marca: String = "Papapp"
    override val precio: Double = 2000.00

    override fun condicionValioso(): Boolean = false
}




