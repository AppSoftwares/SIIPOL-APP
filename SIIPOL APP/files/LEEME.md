# Jefatura SIIPOL · VEN 9-1-1 Zulia

App única en `www/index.html`. Funciona sin internet y sin servicios de pago. Los datos se guardan en el dispositivo.

## Probar en web
Abre `www/index.html` en el navegador (o sírvela con `npx serve www`).

## Convertir a Android e iOS (Capacitor, gratis)
```bash
npm init -y
npm i @capacitor/core @capacitor/cli @capacitor/android @capacitor/ios
npx cap init "SIIPOL Jefatura" com.ven911zulia.siipol --web-dir=www
npx cap add android
npx cap sync
npx cap open android      # abre Android Studio
```
iOS requiere una Mac con Xcode: `npx cap add ios && npx cap open ios`.

## Pendientes antes de publicar
1. Descargar `xlsx.full.min.js` (SheetJS 0.18.5) a `www/` y cambiar la etiqueta `<script>` para que la importación de Excel funcione sin internet.
2. Verificar las fechas institucionales en `DEF.cfg.fechas` (Armada, Ejército, GNB, Día del Policía; agregar CICPC y policías estadales).
3. Para exportar PDF nativo en Android, usar `@capacitor/share` y `@capacitor/filesystem`; `window.print()` funciona en web.
4. Añadir ícono y pantalla de inicio con `@capacitor/assets`.
5. Cifrar o proteger con PIN los datos personales (cédulas, teléfonos, armas): son información sensible.

## Sincronización semanal
Google Sheets → Archivo → Compartir → Publicar en la web → formato CSV. Pega el enlace en Ajustes. La app sincroniza sola al abrirse si pasaron 7 días y hay internet.
