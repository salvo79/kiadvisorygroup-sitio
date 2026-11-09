# Valores del modelo · KI Advisory & Strategy Group

> El modelo no solo dice qué hacer; también dice cuánto vale cambiar cada cosa. Con un solo ejemplo (una crema y un gel) vemos el valor óptimo, la actividad, la holgura, el valor sombra, el valor marginal, el break-even y la elasticidad.

Planeación · cómo leer los resultados

# Qué significan los números que da el modelo [← Todas las perspectivas](https://kiadvisorygroup.com/perspectivas/index.html)

InfinityWorkflow  [← Regresar a Cómo decide el plan de ventas](https://kiadvisorygroup.com/perspectivas/como-decide-el-plan-de-ventas.html)

Planeación · cómo leer los resultados

# Qué significan los números que da el modelo

El modelo no solo dice **qué hacer**; también dice **cuánto vale cambiar** cada cosa. Con un solo ejemplo (una crema y un gel) vemos el valor óptimo, la actividad, la holgura, el valor sombra, el valor marginal, el break-even y la elasticidad.

Mueve los controles: los números cambian como en el modelo.

### Crema hidratante

Precio$100

Costo$40

Margen por pieza$60

El mercado compra hasta600 pz

Hay en inventario500 pz

### Gel exfoliante

Precio$40

Costo$45

Margen por pieza−$5

El mercado compra hasta200 pz

Hay en inventario300 pz

## 1 · Valor óptimo y actividad también: **función objetivo (Z)** · **solución primal** · **valor de la variable**

¿Qué es lo mejor que se puede lograr, y haciendo qué?

El modelo prueba todas las combinaciones y elige la de mayor margen: Crema: vende **500** pz × $60 = **$30,000** Gel: vende **0** pz (cada pieza pierde $5) Z = $30,000

El **valor óptimo** es la mejor utilidad posible con las reglas del negocio. La **actividad** es cuánto hace el plan de cada cosa: 500 piezas de crema y 0 de gel. Ninguna otra combinación deja más.

## 2 · Restricción activa y holgura también: **límite** · **actividad de la restricción** · **slack**

¿Qué regla está frenando el plan?

Inventario de crema: usa **500** de **500** → holgura **0** activa: frena Demanda de crema: usa **500** de 600 → holgura **100** no frena

Una restricción está **activa** cuando se usa completa (holgura 0): es la que impide ganar más. La que tiene holgura no estorba. Aquí manda el inventario, no el mercado.

## 3 · Valor sombra también: **precio sombra** · **valor dual** · **valor marginal de una restricción**

Si tuviera una pieza más de inventario, ¿cuánto ganaría?

Inventario de crema 500 pz

Valor sombra del inventario $60 por pieza Cada pieza más se vende y deja $60. Vale la pena comprar hasta que el mercado se llene (600 pz).

El **valor sombra** (o **dual**) es la pendiente de la utilidad: cuánto sube Z si una restricción se afloja una unidad. Solo las restricciones activas lo tienen. Ojo: **vale dentro de un rango**. Pasando 600 piezas el que manda es el mercado y una pieza más de inventario ya vale $0; ahora el valor sombra lo tiene la demanda.

## 4 · Valor marginal y break-even también: **costo reducido** (de una variable) · **valor de equilibrio** · **precio de equilibrio**

¿Por qué no vende gel, y a qué precio sí convendría?

Precio del gel $40

Valor marginal (costo reducido) de vender gel −$5 por pieza Break-even (precio de equilibrio): **$45** Si se obligara a vender una pieza, la utilidad bajaría $5. Por eso el modelo lo deja en cero.

El **valor marginal** de una variable que el plan deja en cero dice cuánto costaría forzarla. El **break-even** es el precio (o costo) a partir del cual empieza a convenir: aquí $45. Una variable que ya conviene (como la crema) tiene valor marginal 0 y no tiene break-even.

## 5 · Elasticidad precio también: **elasticidad de la demanda** · **sensibilidad al precio**

Si subo el precio de la crema, ¿cuánto dejo de vender?

Elasticidad de la crema −2.0

Cambio de precio +10 %

Demanda elástica Piezas: **−17 %** · Ingreso: **−9 %** · Margen: **−10 %** Precio que maximiza el margen: **$80**

La **elasticidad** es cuánto cambian las piezas por cada 1 % que sube el precio (−2: subir 1 % baja 2 %). Si es **elástica** (más de 1 en valor absoluto), bajar el precio sube el ingreso; si es **inelástica**, subirlo lo sube. El modelo la mide con la historia de cada producto y, si la activas, la demanda de un escenario responde a su precio.

Sobre las decisiones (variables)

### ¿Cuánto hacer de cada cosa?

- **Actividad**: cuánto hace el plan (piezas a vender, comprar, tener).

- **Mín. / Máx.**: entre qué valores puede moverse.

- **Valor marginal** (costo reducido): cuánto costaría forzar una unidad más de algo que no conviene.

- **Break-even**: el precio o costo con el que empezaría a convenir.

Sobre las reglas (restricciones)

### ¿Qué frena el plan y cuánto vale aflojarlo?

- **Actividad**: cuánto se usa del límite.

- **Holgura**: cuánto sobra; 0 = está activa y frena.

- **Valor sombra / dual**: cuánto ganaría el plan si el límite creciera una unidad.

- **Rango**: hasta dónde vale ese valor antes de que mande otra regla.

## En una tabla

ConceptoOtros nombresRespondeEn el ejemploDónde se ve

Valor óptimoFunción objetivo, Z¿Qué es lo mejor posible?$30,000Resultados › encabezado

ActividadPrimal, valor de la variable¿Cuánto hacer?500 pz de crema, 0 de gelReporte de actividad › Variables

HolguraSlack¿Cuánto sobra del límite?Inventario 0 · demanda 100Reporte de actividad › Restricciones

Valor sombraPrecio sombra, valor dual¿Cuánto vale aflojar una regla?$60 por pieza de inventarioRestricciones · Inventarios

Valor marginalCosto reducido¿Cuánto cuesta forzar algo?−$5 por pieza de gelReporte de actividad › Variables

Break-evenValor o precio de equilibrio¿Desde qué precio conviene?Gel a $45Variables · Productos

ElasticidadSensibilidad al precio¿Cuánto cae la venta si sube el precio?−2 → +10 % precio = −17 % piezasProductos · Gantt · Excel

## La idea en una frase

El **valor óptimo** dice cuánto se puede ganar; la **actividad**, qué hacer; el **valor sombra**, qué límite conviene ampliar; el **valor marginal** y el **break-even**, qué no conviene y a qué precio convendría; y la **elasticidad**, cómo reacciona el mercado al precio.  [← Regresar a Cómo decide el plan de ventas](https://kiadvisorygroup.com/perspectivas/como-decide-el-plan-de-ventas.html)

---

Fuente: https://kiadvisorygroup.com/perspectivas/valores-del-modelo.html · KI Advisory & Strategy Group · contact@kiadvisorygroup.com
