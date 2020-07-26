# Aplicación del método Newton-Raphson para resolver ecuaciones no lineales

## Planteamiento del problema (Caso Ingeniería Mecánica)

Para hacer el punto de apoyo (Figura 1) de un puente basculante, un eje de acero largo y hueco llamado muñón se ajusta por contracción en un cubo de acero. El ensamblaje resultante del muñón de acero del cubo se ajusta por contracción en la viga del puente.

<p align="center">
  <img src="http://solodatascience.com/wp-content/uploads/2020/07/newton-raphson-figura-01-trunnion.jpg" />
  Figura 1: Montaje de muñón-cubo-viga
</p>

Esto se hace sumergiendo primero el muñón en un medio frío, como una mezcla de hielo seco/alcohol. Después de que el muñón alcanza la temperatura de estado estable del medio frío, el diámetro exterior del muñón se contrae. El muñón se saca del medio y se desliza por el orificio del cubo (Figura 2).

![Figura 2: El muñón se desliza por el centro después de contraerse](http://solodatascience.com/wp-content/uploads/2020/07/newton-raphson-figura-02-trunnion.jpg)

Cuando el muñón se calienta, se expande y crea un ajuste de interferencia con el cubo. En 1995, en uno de los puentes en Florida, este procedimiento de ensamblaje no funcionó como fue diseñado. Antes de que el muñón se pudiera insertar completamente en el cubo, el muñón se atascó. Por lo tanto, se tuvo que pedir un nuevo muñón y un centro a un costo de $ 50,000. Junto con los retrasos en la construcción, la pérdida total fue de más de cien mil dólares. ¿Por qué se atascó el muñón? Esto se debía a que el muñón no se había contraído lo suficiente como para deslizarse a través del agujero.

Para este nuevo puente, se necesita colocar un muñón hueco de diámetro exterior 12.363" en un cubo de diámetro interior 12.358". Su plan es poner el muñón en la mezcla de hielo seco/alcohol (la temperatura del fluido - la mezcla de hielo seco/alcohol es -108°F) para contraer el muñón de modo que pueda deslizarse a través del orificio del cubo.

Para deslizar el muñón sin pegarse, también ha especificado una separación diametral de al menos 0.01" entre el muñón y el cubo. Suponiendo que la temperatura ambiente es 80°F, ¿es una decisión correcta sumergirlo en una mezcla de hielo seco / alcohol? ¿Qué temperatura? ¿necesita enfriar el muñón para obtener la contracción deseada?
