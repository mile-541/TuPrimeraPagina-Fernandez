# 🏥 Sistema de Gestión Veterinaria - Veterinaria "Las patitas"

Un sistema completo de gestión para veterinarias desarrollado con Django, que permite administrar dueños, mascotas y turnos de manera eficiente.

## ✨ Características Principales

### 🏠 **Dashboard Principal**
- Menú de navegación
- Vista general con estadísticas de la veterinaria
- Contador de dueños, mascotas y turnos
- Accesos rápidos a todas las funcionalidades

### 👥 **Gestión de Dueños**
- Registro de dueños con datos de contacto
- Búsqueda por nombre o apellido
- Visualización de mascotas asociadas

### 🐾 **Gestión de Mascotas**
- Registro detallado de mascotas
- Asociación automática con dueños
- Búsqueda por nombre o especie

### 📅 **Gestión de Turnos**
- Programación de citas veterinarias
- Selección automática de mascotas según dueño
- Validación de fechas futuras
- Estado de turnos (pendiente/completado)

### 📌 **Otras características**
- Diseño moderno y responsive
- Formularios modales (pop-ups) para nuevos registros
- Guardado en base de datos asociada

## 🚀 Instalación y Configuración

### Prerrequisitos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Pasos de Instalación

1. **Clonar o descargar el proyecto**
   ```bash
   cd TuPrimeraPagina-Fernandez
   ```

2. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

3. **Aplicar migraciones**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Ejecutar el servidor**
   ```bash
   python manage.py runserver
   ```

5. **Acceder al sistema**
   - **Sitio principal**: http://127.0.0.1:8000/

## 📱 Uso del Sistema

### Navegación Principal
- **Inicio**: Dashboard con estadísticas generales
- **Dueños**: Gestión de propietarios
- **Mascotas**: Gestión de animales
- **Turnos**: Programación de citas

### Funcionalidades por Sección

#### 🔍 **Búsqueda**
- Cada sección incluye un buscador funcional
- Filtros en tiempo real
- Resultados paginados

#### ➕ **Creación de Registros**
- Botones "Nuevo" en cada sección
- Validación automática de datos
- Asociación entre entidades vinculadas
- Guardado en base de datos SQLite3

#### 👁️ **Visualización**
- Tarjetas informativas con diseño moderno
- Iconos intuitivos para cada tipo de dato
- Estados visuales (pendiente/completado)
- Información relacionada entre entidades

## 🗄️ Estructura de la Base de Datos

### Modelo `Dueño`
- **nombre**: Nombre del propietario
- **apellido**: Apellido del propietario
- **telefono**: Número de contacto
- **email**: Correo electrónico

### Modelo `Mascota`
- **dueño**: Relación con el propietario
- **nombre**: Nombre de la mascota
- **especie**: Tipo de animal
- **sexo**: Género (M/F)
- **edad**: Edad en años

### Modelo `Turno`
- **dueño**: Propietario de la mascota
- **mascota**: Animal para la consulta
- **fecha**: Fecha y hora del turno
- **motivo**: Razón de la consulta

## �� Tecnologías Utilizadas

- **Backend**: Django 5.2
- **Base de Datos**: SQLite3
- **Frontend**: HTML5, CSS3, JavaScript
- **Framework CSS**: Bootstrap 5.3
- **Iconos**: Font Awesome 6.0
- **Responsive**: Mobile-first design

## 🔧 Personalización

### Colores y Estilos
- Gradientes personalizados para cada sección
- Paleta de colores coherente
- Transiciones y animaciones suaves
- Hover effects en elementos interactivos

### Funcionalidades Extensibles
- API endpoints para integraciones futuras
- Estructura modular para nuevas características
- Sistema de permisos Django integrado

## 📊 Funcionalidades Avanzadas

### Dashboard Inteligente
- Contadores en tiempo real
- Estadísticas automáticas
- Indicadores visuales de estado

### Relaciones Inteligentes
- Carga dinámica de mascotas por dueño
- Validación de dependencias
- Integridad referencial automática

### Búsqueda Avanzada
- Filtros múltiples
- Búsqueda por texto libre
- Resultados paginados
- Limpieza de filtros

## 🚨 Consideraciones Importantes

### Seguridad
- CSRF protection habilitado
- Validación de formularios
- Sanitización de datos
- Permisos de acceso controlados

### Rendimiento
- Consultas optimizadas a la base de datos
- Paginación automática
- Carga lazy de datos relacionados
- Cache de consultas frecuentes

## 🆘 Soporte y Mantenimiento

### Logs y Debugging
- Mensajes de error descriptivos
- Logs de operaciones críticas
- Validación de datos en tiempo real

### Backup y Recuperación
- Base de datos SQLite3 portable
- Migraciones versionadas
- Scripts de respaldo automático

## 🔮 Futuras Mejoras

- [ ] Admin personalizado con filtros avanzados
- [ ] Calendario visual de turnos
- [ ] Reportes y estadísticas avanzadas
- [ ] API REST completa
- [ ] Aplicación móvil
- [ ] Historial médico completo
- [ ] Sistema de vacunas y recordatorios

## 👨‍💻 Desarrollador

**Milena Fernández** - Estudiante de Python en Coderhouse

---

## 📝 Licencia

Este proyecto es parte de la Tercera Entrega del curso de Python en Coderhouse.

---

**¡Gracias por usar el Sistema de Gestión Veterinaria "Las patitas"!🐾🐈‍⬛**