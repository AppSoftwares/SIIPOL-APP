# SIIPOL Jefatura · VEN 9-1-1 Zulia 🛡️

![SIIPOL Banner](https://img.shields.io/badge/SIIPOL-VEN%209--1--1-6b1425?style=for-the-badge)
![Platform](https://img.shields.io/badge/Plataformas-Android%20%7C%20iOS%20%7C%20Web-blue?style=for-the-badge)
![License](https://img.shields.io/badge/Licencia-Oficial%20%2F%20Reservado-gold?style=for-the-badge)

Sistema Integrado de Información Policial (**SIIPOL**) desarrollado para la **Sala Situacional y Jefatura del Servicio del VEN 9-1-1 Zulia**. Aplicación multiplataforma (Web, Android, iOS) orientada a la gestión operativa, control de personal, parte del servicio diario, estadísticas institucionales y emisión de expedientes confidenciales.

---

## 📋 Características Principales

### 👨‍✈️ 1. Gestión de Personal y Filtros por Organismo
- Búsqueda inteligente e instantánea por **nombre, cédula de identidad, número de credencial/placa o rango**.
- Filtro unificado por organismos policiales y militares del Estado Zulia:
  - **FANB** (Armada, Ejército, GNB)
  - **CPBEZ**
  - **Polimaracaibo**, **Polimara**, **Poliguajira**, **Polilagunillas**, **Policabimas**, **Polisur**, **Poliurdaneta**, **Policon**
  - **CICPC**

### 📁 2. Expediente Confidencial de Personal (Ficha A4/PDF)
- Generación de **Ficha de Expediente Oficial** estilizada tipo carpeta clasificada (*TOP SECRET / CONFIDENCIAL*).
- Secciones estructuradas:
  1. **I. Filiación y Datos Personales** (Cédula, Fecha de nacimiento, Edad calculada, Grupo sanguíneo).
  2. **II. Información Institucional** (Organismo, Rango/Jerarquía, Credencial/Placa, Oficina/Adscripción, Arma asignada/Porte, Estatus operativo).
  3. **III. Sistema y Contacto** (Usuario SIIPOL, Teléfono, Correo institucional/personal).
  4. **IV. Observaciones y Notas de Campo**.
- **Diseño impreso A4/Carta completo** con sellos oficiales, número de folio único (`EXP-CI-AÑO`) y código de barras.
- Exportación a **PDF / Imprimir**, texto plano para **WhatsApp**, correo electrónico o copia en portapapeles.

### 📅 3. Control de Vacaciones y Parte del Servicio
- Registro de permisos y vacaciones con fecha de salida y fecha estimada de retorno.
- Alertas en pantalla de funcionarios que regresan en los próximos 7 días.
- **Generador de Parte del Servicio Diario** por fecha seleccionable: totales de personal activo, en vacaciones y desglose por organismo.

### 📊 4. Estadísticas y Comparativa Mensual
- Gráficos visuales de distribución de funcionarios por cuerpo policial/militar.
- Comparación de efectividad y vacaciones respecto al mes anterior.

### 🎂 5. Próximos Cumpleaños y Fechas Institucionales
- Alertas de cumpleaños del día y listado de los próximos 25 cumpleaños.
- Mensajes institucionales de felicitación pre-redactados para envío en un toque vía WhatsApp o correo.
- Registro de Aniversarios de la Armada (24/07), Ejército (24/06), GNB (04/08) y Día del Policía (25/11).

### ⚖️ 6. Módulo Jurídico y Planillas Modelo
- Consulta de los 10 artículos de la **Resolución N.º 196 (Gaceta Oficial N.º 40.422)** sobre el uso del SIIPOL.
- Espacio para notas y precedentes jurídicos personales.
- Modelos de planillas editables/imprimibles:
  - Solicitud de Usuario SIIPOL.
  - Compromiso de Confidencialidad.
  - Bienvenida a Nuevo Usuario.

### 🔌 7. Funcionamiento 100% Offline y Sincronización Gratis
- Almacenamiento local seguro en el dispositivo sin necesidad de servidores o bases de datos pagas.
- Importación directa de archivos Excel (`.xlsx`, `.xls`, `.csv`) utilizando la librería empaquetada `xlsx.full.min.js`.
- Sincronización semanal automática con **Google Sheets** publicado como CSV.

---

## 🛠️ Tecnologías Utilizadas

- **Frontend Core**: HTML5, CSS3 (Variables CSS, Flexbox, Grid Layout), JavaScript (ES6+).
- **Mobile Engine**: [Capacitor 8](https://capacitorjs.com/) (`@capacitor/core`, `@capacitor/cli`, `@capacitor/android`).
- **Excel Parser**: SheetJS (`xlsx.full.min.js`).
- **Web Server**: `serve` (Desarrollo local).

---

## 🚀 Instalación y Ejecución

### 1. Requisitos Previos
- [Node.js](https://nodejs.org/) (Versión 18 o superior).
- [Android Studio](https://developer.android.com/studio) (Para compilar APK/AAB de Android).

### 2. Clonar el Repositorio e Instalar Dependencias
```bash
git clone https://github.com/AppSoftwares/SIIPOL-APP.git
cd SIIPOL-APP
npm install
```

### 3. Probar en Navegador Web
```bash
npm run dev
# Abre http://localhost:3000
```

### 4. Compilar y Abrir en Android Studio
```bash
# Sincronizar archivos web a la plataforma nativa
npx cap sync

# Abrir el proyecto en Android Studio
npx cap open android
```

---

## 📂 Estructura del Proyecto

```
SIIPOL APP/
├── android/                    # Proyecto nativo Android (Capacitor)
├── www/                        # Código fuente de la app web empaquetada
│   ├── index.html              # Aplicación principal
│   └── xlsx.full.min.js        # Librería de lectura Excel offline
├── capacitor.config.json       # Configuración global de Capacitor
├── package.json                # Scripts y dependencias npm
├── LEEME.md                    # Instrucciones en español
└── README.md                   # Documentación oficial del repositorio
```

---

## 🔒 Nota de Confidencialidad y Seguridad

Este software maneja datos de filiación y registro policial/militar. Se recomienda no distribuir ejecutables sin activar protección por PIN o cifrado de almacenamiento local.

**Jefatura del Servicio SIIPOL · VEN 9-1-1 Estado Zulia, Venezuela.**
