# Pronosticar u optimizar · KI Advisory & Strategy Group

> Las series temporales miran el pasado para decir cuánto se va a vender. El modelo LP toma eso y decide cuánto conviene vender y comprar para ganar más sin romper las reglas del negocio. No compiten: una predice y el otro decide.

Dos formas de planear

# Pronosticar u optimizar [← Todas las perspectivas](https://kiadvisorygroup.com/perspectivas/index.html)

InfinityWorkflow  [← Regresar a Cómo decide el plan de ventas](https://kiadvisorygroup.com/perspectivas/como-decide-el-plan-de-ventas.html)

Dos formas de planear

# Pronosticar u optimizar

Las **series temporales** miran el pasado para decir **cuánto se va a vender**. El **modelo LP** toma eso y decide **cuánto conviene vender y comprar** para ganar más sin romper las reglas del negocio. No compiten: una predice y el otro decide.

El pronóstico es el reporte del clima. El LP es decidir qué hacer con ese clima.

El clima te dice que mañana probablemente llueve. No te dice si conviene cancelar la entrega, mover la ruta o llevar más paraguas a la tienda: eso depende de tus camiones, tus costos y tu inventario. Esa segunda parte es la que resuelve el modelo LP.

Series temporales (pronóstico)

"¿Cuánto vamos a vender?"

Busca la **tendencia** y la **temporada** en lo que ya pasó y las alarga hacia adelante (media móvil, regresión, ARIMA). Entrega una cifra por mes y qué tan segura es: la banda se abre porque entre más lejos, menos certeza.

no sabe cuánto hay en el almacén ni cuánto deja cada pieza   Modelo LP (optimización)

"¿Cuánto nos conviene vender?"

Toma la demanda como un **techo** y combina todo a la vez: margen, inventario, compras, tiempos de entrega, presupuesto y metas. Entrega **decisiones**: qué vender, dónde, cuándo y cuánto comprar, y qué regla frena la utilidad.

necesita saber cuánto pide el mercado: ahí entra el pronóstico

El mismo mes, planeado de las dos formas

## El pronóstico pide 130 piezas, pero solo hay 100

Crema A: el pronóstico dice 70 piezas y deja $80 cada una. Sérum B: el pronóstico dice 60 y deja $50. En el almacén hay 100 piezas.

Cómo se arma el planCrema ASérum B¿Se puede?Margen

Copiar el pronóstico tal cual7060No: faltan 30 piezas—

Recortar el pronóstico parejo5446Sí$6,620

Modelo LP7030Sí$7,100

Con el pronóstico solo, el plan es imposible o deja dinero en la mesa. El LP usa el mismo pronóstico y elige el reparto que más deja.

Diferencias, punto por punto

## Qué hace cada uno

Series temporalesModelo LP

La pregunta¿Cuánto se va a vender?¿Cuánto conviene vender y comprar?

Qué miraSolo la historia de la variable (y su temporada)Todo junto: demanda, margen, inventario, compras, entregas, presupuesto, metas

Qué entregaUna cifra por mes con su rango de confianzaDecisiones por producto, zona y mes, y el valor de cada restricción

Reglas del negocioNo las conoceLas respeta todas; un plan que rompe una regla no existe

DineroNo distingue lo que deja más margenPrioriza lo que más margen deja

Si algo cambiaSe vuelve a ajustar con datos nuevosSe cambia el dato (precio, costo, almacén) y recalcula en segundos

Su punto débilSupone que el futuro se parece al pasadoEs tan bueno como la demanda que le damos

En Infinity WorkflowAnalítica de datos › Diseño de casos (tendencias, ARIMA y ARMA)Planeación › Optimización de venta LP

Lo mejor es usar los dos

## Uno alimenta al otro

**1 · Pronosticar**Las series temporales estiman cuánto pide el mercado cada mes.

---

Fuente: https://kiadvisorygroup.com/perspectivas/pronosticar-u-optimizar.html · KI Advisory & Strategy Group · contact@kiadvisorygroup.com
