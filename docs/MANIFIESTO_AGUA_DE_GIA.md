# 💧 AquaResiliencia Tijuana (Agua de Gia)
## Código Abierto, Telemetría y Pozos Someros

> *"Entre más estudio sobre el agua y la humanidad, más fascinado estoy de nuestra capacidad de resiliencia."*  
> **— Pablo Campos / Colectivo 1, 2, 3 por Tijuana**

---

### Entre más estudio sobre el agua y la humanidad, más fascinado estoy de nuestra capacidad de resiliencia

Entre más estudio sobre el agua y la humanidad, más fascinado estoy de nuestra capacidad de resiliencia. Ya que esto que estamos proponiendo es de código abierto.

Para quien no esté familiarizado con eso, bueno, **código abierto** es cuando está ahí a la vista el funcionamiento, no es algo privado y todos pueden colaborar creando lo mejor que tenemos como humanos, ¿no? Por ejemplo, Linux, Android... ¿quién no ha interactuado con esas plataformas?

Y si nos vamos a la antigüedad, una de las primeras cosas de código abierto que hubo fue un sistema para aprovechar el agua de pozos someros de los **persas**, en los que hicieron un reloj que era el que repartía el agua entre los pobladores, pues tenían una red de túneles (*qanats*). Este reloj que la repartía era un cuenco de bronce (*fenjan*), y lo que tardaba en hundirse era una unidad de tiempo de agua. Había dos personas elegidas por la comunidad que custodiaban el reloj a plena luz del día, y todo el pueblo veía cómo se iba llenando para uno y para otro. Y así todo era parejo, ¿no? Además de que la tecnología estaba ahí para cualquiera.

Los **romanos** mencionaron:  
> *«Por ley natural, estas cosas son comunes a toda la humanidad: el aire, el agua corriente, el mar y las costas del mar».*

Nadie podía ser dueño del agua que corría por un arroyo o de un manantial superficial. Se podía usar el flujo, sí, pero no apropiarse del recurso ni privar al vecino de abajo del mismo derecho. *Agua pasa por mi casa, cate de mi corazón.*

Y bueno, acá en **América**, antes de la llegada de los españoles, también existían cosas de código abierto. Había trabajo comunal que no se pagaba y eran las obras hidráulicas de la ciudad; eran faenas colectivas obligatorias y rotativas, algo así como servicio social (*tequio*).

Otro dato curioso es el **Premio Nobel de Economía del 2009** (Elinor Ostrom). La economista que ganó el premio demostró que los sistemas de agua comunitarios tradicionales, cuando son quienes diseñan sus propias reglas, miden abiertamente el recurso y tienen mecanismos transparentes de sanciones entre vecinos, gestionan el agua subterránea de forma mucho más sostenible y duradera que el Estado burocrático o que el mercado privado.

Así que el corazón de **AquaResiliencia Tijuana** es de alma vieja. Y es una técnica de bajo costo para perforar y llegar al agua que está a menos de 10 metros. No en todas partes de la ciudad se puede, pero sí hay ya un mapa que hicimos de todos los lugares donde podría ser probable tener éxito. Hicimos una capa, así como las capas de Google Maps, ¿no?, que te da la capa de tráfico o la capa de lluvia; bueno, hicimos una con los datos que hay, que no son muchos. Incluso a nuestra capa le pusimos los registros de árboles como los álamos, que se sabe que sus raíces llegan a 5 o 6 metros de profundidad.

---

### El cuerpo del proyecto y la realidad de Tijuana

Así que vayamos desmenuzando AquaResiliencia. Su corazón ya lo conocimos, pero ¿qué me dicen de su cuerpo?

Su cuerpo es una **perforación de 2 pulgadas en el piso**, en el que se le conecta un **ESP32 con Arduino**, con WiFi si quieres, que les va a dar información tan vital a los científicos del **CICESE**, o del **COLEF**, o de **Conagua** o de la **CESPT**. Porque, ¿se imaginan tener una red de estos datos?

Y pues yo creo que ya ha de saber, o si no también le comparto, que ya hace como un año salió una nueva ley de las aguas y apenas hace como junio, julio, salieron ya algunos mecanismos que tenía que dar de alta la Conagua para todo lo referente a los pozos y demás. La extracción del agua y de muchas otras cosas.

Entre ellas —y ahí es donde le pregunto a usted qué sabe de eso— está que, si bien hay que registrar un pozo para uso doméstico, si cumple con ciertas características de volumen y demás, ya no necesita un registro y todo un estudio, y ya no es penado, o sea, **ya no te meten al bote**. Simplemente podrían cerrártelo porque no lo registraste, ¿no?

Pero bueno, ya que me metí en ese tema, me fui bien recio y hay cosas bien interesantes. Como investigador... es que, perdón, está del nabo que se va el agua a cada rato, no hay luz, y esto no se va a poner mejor. Cada vez hay menos agua llegando al Río Colorado, nos mandan menos, y **el 35% del agua que se bombea para Tijuana se pierde en la red de la CESPT**: o no la pagan, o se la roban, o fugas, y la CESPT lo acepta.

¿Y quiere saber algo curioso? La capacidad de recarga o lo que se recarga el acuífero de Tijuana es justo esa cantidad. O sea, que ahora, gracias a la CESPT, **tenemos doble recarga anual**. Pero ahí vienen las inconsistencias, porque entonces no debería de medirse igual el agua que hay en el subsuelo, ¿no?

Y hay varias cosas ahí que son controversiales y que el gobierno nunca lo va a aceptar porque sería aceptar su propia ineficiencia, pero que para efectos reales y prácticos, **hasta es ventajoso para la ciudad extraer agua en ciertos puntos, porque eso va a evitar más deslizamientos y problemas que hemos tenido**. Eso es por el lado meramente científico, de protección civil y demás.

Por el lado científico de investigador de CICESE, de la UABC y de El Colef, pues está la parte de que **no existe una red de telemetría**: no sabemos qué hay allá abajo, no sabemos qué está pasando. Estuvo tanto tiempo en veda y era tan tabú que no tenemos realmente datos buenos, y mucho se hace con modelos matemáticos. Entre esos, ya se pudo comprobar que haberle puesto cemento al Alamar le dio en la madre al acuífero.

Eso por ese lado. Por el otro lado, por el lado del gobierno: la red morada con la que siempre soñamos, que siempre quisimos tener y que dijimos «esto va a estar bien chingón, reúso del agua», pues no es viable porque ¿quién va a mandar tuberías tan caras por todos lados, romper piso, concreto y demás? ¿Pero qué cree? **Ya hay una red morada abajo a 3, 4, 5, 8 metros de profundidad que nos hizo la naturaleza y que no sabemos casi nada de ella.** Y ahí es donde entra este proyecto.

Si no lo he mareado o ya lo perdí y todavía sigue escuchándome, pues bueno, habría que analizar esto a lo mejor de una perspectiva más global. Tal vez suena a una locura extraer micropozos... ¿Dónde más estará pasando esto en el mundo? En **Berlín**, sí, en la capital; o aquí a un lado en **California**; o en **Ciudad del Cabo** en Sudáfrica... De hecho ya sucede en varias partes y está bien regulado y hay leyes que sirven para lo que son las leyes, ¿no?

Y el alma de AquaResiliencia es generar, mediante esta perforación somera, una **red de datos: nodos con sensores para telemetría**. ¿Qué es esto? Para medir las condiciones del subsuelo.

---

### Agua para el futuro (El origen: Gia)

Y bueno, ahora que entiendes un poco más qué es AquaResiliencia o **Agua de Gia**, quiero compartirte que este proyecto empezó hace 4 años.

Exactamente desde el día que me enteré que iba a ser padre por primera vez.

No, no... desde el día que me enteré que iba a ser padre de una hermosa niña que se llama **Gia, en honor a la Tierra**.

> **Agua de Gia: agua para el futuro, agua para los que apenas llegan y agua para la tierra y para la posteridad.**

---

## 📚 Referencias y Sustento Técnico

1. **Gobernanza de Bienes Comunes (Premio Nobel 2009)**  
   *Ostrom, Elinor. Governing the Commons: The Evolution of Institutions for Collective Action.*  
   Investigación empírica sobre cómo la gestión comunitaria con reglas transparentes supera la centralización estatal y la privatización en recursos subterráneos.

2. **Historia Hidráulica y Código Abierto**  
   * **Persia (*Qanats* y *Fenjan*):** El cuenco de bronce flotante perforado como reloj hidrométrico público para la asignación comunitaria del agua subterránea.
   * **Derecho Romano (*Institutas de Justiniano*):** Principio de *res communes omnium* («Por derecho natural son comunes a toda la humanidad: el aire, el agua corriente, el mar y las costas»).
   * **Mesoamérica:** La figura comunal del *tequio* y faenas rotativas obligatorias para el mantenimiento de obras hidráulicas urbanas.

3. **Marco Normativo y Legal de Aguas en México**  
   * **Ley de Aguas Nacionales y Artículo 27 Constitucional:** Disposiciones sobre libre alumbramiento para uso doméstico y mecanismos de registro simplificado ante Conagua. Las omisiones de registro en uso doméstico menor corresponden a faltas administrativas/clausura y no a sanciones penales.

4. **Pérdidas de Red y Recarga Urbana en Tijuana**  
   * **CESPT (Agua No Contabilizada):** Registros operativos de pérdida de agua entre el 30% y el 36% en la red de distribución por fugas crónicas y tomas no reguladas.
   * **Balance Hidrogeológico:** El volumen de agua potable perdida hacia el subsuelo equivale o supera la tasa de recarga natural anual del acuífero local, funcionando como recarga artificial inducida.

5. **Geotecnia y Riesgos de Deslizamiento (Protección Civil)**  
   * En las formaciones geológicas de Tijuana con presencia de arcillas, la saturación del nivel freático somero reduce la resistencia de los taludes; el monitoreo y abatimiento freático controlado ayuda a mitigar riesgos de deslizamiento.

6. **Impacto Ambiental en el Acuífero del Alamar**  
   * Estudios de El Colef y CICESE sobre la pérdida de capacidad de infiltración y recarga al acuífero somero provocada por el encementado del Arroyo Alamar.

7. **Precedentes Internacionales de Pozos Someros Domésticos**  
   * **Berlín (*Gartenbrunnen*):** Extensa red de micropozos domésticos someros registrados para usos secundarios.
   * **California:** Regulación de pozos domésticos someros bajo la ley SGMA (*Sustainable Groundwater Management Act*).
   * **Ciudad del Cabo:** Proliferación y marco normativo de pozos someros (*wellpoints*) tras la crisis hídrica del "Day Zero".
