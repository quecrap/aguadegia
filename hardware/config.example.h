/**
 * ============================================================================
 * PROYECTO: AquaResiliencia Tijuana / Agua de GIA
 * REPOSITORIO: aguadegia
 * ARCHIVO: hardware/config.example.h
 * PROPÓSITO: Plantilla de configuración en C++ para el Nodo Centinela IoT (ESP32)
 * ============================================================================
 * INSTRUCCIONES DE USO:
 * 1. Copia este archivo con el nombre "config.h" dentro de esta misma carpeta:
 *    cp hardware/config.example.h hardware/config.h
 * 2. Modifica los parámetros con tus credenciales locales (WiFi, MQTT, etc.).
 * 3. IMPORTANTE: "config.h" se encuentra registrado en .gitignore para evitar
 *    la filtración de contraseñas, tokens y claves privadas en GitHub.
 * ============================================================================
 */

#ifndef CONFIG_H
#define CONFIG_H

#include <Arduino.h>

// ============================================================================
// 1. IDENTIFICACIÓN DEL DISPOSITIVO
// ============================================================================
#define DEVICE_ID             "centinela-tj-001"          // Identificador único del nodo
#define DEVICE_ZONE           "Playas de Tijuana"         // Zona general (sin dirección exacta)
#define FIRMWARE_VERSION      "1.2.0-public"              // Versión del firmware

// ============================================================================
// 2. CONECTIVIDAD WI-FI (ESTACIÓN Y PUNTO DE ACCESO LOCAL)
// ============================================================================
// Modo Estación (Conexión al router local o módem 4G/LTE)
#define WIFI_SSID             "TU_RED_WIFI_AQUI"          // Nombre de red Wi-Fi
#define WIFI_PASSWORD         "TU_PASSWORD_WIFI_AQUI"     // Contraseña de red Wi-Fi
#define WIFI_CONNECT_TIMEOUT  20000                       // Tiempo límite de conexión en ms

// Punto de Acceso de Respaldo / Diagnóstico en Campo (Captive Portal)
#define AP_SSID               "AquaResiliencia_AP"        // SSID transmitido por el ESP32
#define AP_PASSWORD           "agua_centinela_2026"       // Contraseña para técnicos en campo
#define AP_LOCAL_IP           192, 168, 4, 1              // IP fija del portal de diagnóstico

// ============================================================================
// 3. BROKER MQTT & PROTOCOLOS DE TELEMETRÍA ABIERTA
// ============================================================================
#define MQTT_SERVER           "mqtt.aguadegia.org"        // Host o IP del Broker MQTT público/privado
#define MQTT_PORT             1883                        // Puerto estándar (o 8883 para TLS/SSL)
#define MQTT_USER             "usuario_mqtt_ejemplo"      // Dejar en blanco si el broker es anónimo
#define MQTT_PASSWORD         "token_o_password_ejemplo"  // Token de autenticación del dispositivo
#define MQTT_CLIENT_ID        "esp32-nodo-centinela-001"

// --------------------------- TOPICS MQTT (TELEMETRÍA) -----------------------
// Publicación periódica del estado físico del pozo (JSON payload)
#define TOPIC_TELEMETRY       "aguadegia/tijuana/pozo001/telemetria"

// Publicación del estado operativo ("OPERATIVO", "CORTE_PREVENTIVO", "ALARMA")
#define TOPIC_STATUS          "aguadegia/tijuana/pozo001/estado"

// Eventos de alarma y disparos de seguridad inmediatos
#define TOPIC_ALERTS          "aguadegia/tijuana/pozo001/alertas"

// Tópico de suscripción para comandos remotos autorizados (corte de emergencia)
#define TOPIC_COMMANDS        "aguadegia/tijuana/pozo001/cmd"

// ============================================================================
// 4. ASIGNACIÓN DE PINES DE HARDWARE (PINOUT ESP32 DEVKIT V1 - 30 PINES)
// ============================================================================
// Sensor Analógico de TDS / Conductividad Eléctrica (DFRobot Gravity compatible)
#define PIN_TDS               34  // ADC1 Canal 6 (Entrada Analógica 0.0V - 3.3V)

// Caudalímetro de Turbina con sensor de efecto Hall (YF-S201 de 1/2 pulgada)
#define PIN_FLOW_SENSOR       18  // Entrada digital con interrupción externa (RISING)

// Sensor Ultrasónico Impermeable de Nivel Freático (JSN-SR04T / AJ-SR04M)
#define PIN_TRIG              5   // Salida digital (Disparo de pulso ultrasónico 10µs)
#define PIN_ECHO              19  // Entrada digital (Tiempo de retorno del eco)

// Actuador: Módulo Relevador de 1 Canal Optoacoplado (Control de Bomba)
#define PIN_RELAY_PUMP        23  // Salida digital de control (Activo en LOW / Relé cerrado)

// Indicador Visual de Estado
#define PIN_LED_STATUS        2   // LED Onboard / Externo (Verde = Normal, Parpadeo = Alarma)

// ============================================================================
// 5. UMBRALES DE SEGURIDAD Y REGLAS DE CORTE AUTOMÁTICO
// ============================================================================
// Límite de extracción diario de subsistencia comunitaria (en Litros)
// Al alcanzar este valor acumulado en 24h, el sistema apaga la bomba para evitar sobreexplotación.
const float MAX_DAILY_VOLUME_LITERS    = 600.0f;

// Nivel freático mínimo de seguridad sobre la pichancha de la bomba (en metros)
// Previene el agotamiento del estrato aluvial y la cavitación de la bomba.
const float MIN_SAFE_WATER_LEVEL_M      = 2.00f;

// Umbral máximo de TDS permitido (en partes por millón / ppm)
// Detecta anomalías de intrusión marina, ruptura de tuberías negras o contaminantes químicos.
const int   MAX_SAFE_TDS_PPM            = 1800;

// Factor de calibración del caudalímetro YF-S201 (Pulsos por segundo por cada Litro/minuto)
// Frecuencia (Hz) = 7.5 * Caudal (L/min)
const float FLOW_CALIBRATION_FACTOR     = 7.5f;

// ============================================================================
// 6. INTERVALOS DE TIEMPO Y TELEMETRÍA (EN MILISEGUNDOS)
// ============================================================================
const unsigned long TELEMETRY_INTERVAL_MS = 30000;   // Publicar reporte MQTT cada 30 segundos
const unsigned long SENSOR_READ_INTERVAL_MS= 2000;    // Leer sensores físicos cada 2 segundos
const unsigned long FLOW_SAMPLE_WINDOW_MS = 1000;    // Ventana de muestreo para cálculo de caudal

// ============================================================================
// 7. COMPENSACIÓN DE TEMPERATURA Y CALIBRACIÓN ANALÓGICA TDS
// ============================================================================
const float DEFAULT_WATER_TEMP_C        = 20.0f;     // Temperatura media del agua somera en Tijuana
const float ADC_VOLTAGE_REF             = 3.30f;     // Voltaje de referencia ADC del ESP32
const int   ADC_RESOLUTION              = 4095;      // Resolución ADC 12 bits

#endif // CONFIG_H
