#!/bin/bash
# Based on http://openweathermap.org/current
 
API_KEY="b2751e068adb21b093a02dea731b6fc4"
 
# Check on http://openweathermap.org/find
CITY_ID="3446682"

URGENT_LOWER=0
URGENT_HIGHER=35
 
ICON_SUNNY="Ensolarado"
ICON_CLOUDY="Nublado"
ICON_RAINY="Chuvoso"
ICON_STORM="Tempestade"
ICON_SNOW="Neve"
ICON_FOG="Neblina"
 
SYMBOL_CELSIUS="℃"
 
WEATHER_URL="http://api.openweathermap.org/data/2.5/weather?id=${CITY_ID}&appid=${API_KEY}&units=metric"
 
WEATHER_INFO=$(wget -qO- "${WEATHER_URL}")
WEATHER_MAIN=$(echo "${WEATHER_INFO}" | grep -o -e '\"main\":\"[a-Z]*\"' | awk -F ':' '{print $2}' | tr -d '"')
WEATHER_MAX=$(echo "${WEATHER_INFO}" | grep -o -e '\"temp_max\":\-\?[0-9]*' | awk -F ':' '{print $2}' | tr -d '"')
WEATHER_TEMP=$(echo "${WEATHER_INFO}" | grep -o -e '\"temp\":\-\?[0-9]*' | awk -F ':' '{print $2}' | tr -d '"')
WEATHER_MIN=$(echo "${WEATHER_INFO}" | grep -o -e '\"temp_min\":\-\?[0-9]*' | awk -F ':' '{print $2}' | tr -d '"')
WEATHER_CITY=$(echo "${WEATHER_INFO}" | grep -o -e '\"name\":\"[a-Z]*\"' | awk -F ':' '{print $2}' | tr -d '"')
WEATHER_HUMIDITY=$(echo "${WEATHER_INFO}" | grep -o -e '\"humidity\":\-\?[0-9]*' | awk -F ':' '{print $2}' | tr -d '"')
WEATHER_WIND=$(echo "${WEATHER_INFO}" | grep -o -e '\"speed\":\-\?[0-9]*' | awk -F ':' '{print $2}' | tr -d '"')

if [[ "${WEATHER_MAIN}" = *Snow* ]]; then
  echo "${WEATHER_CITY}"
  echo "Temp: ${WEATHER_TEMP}${SYMBOL_CELSIUS}"
  echo "Max: ${WEATHER_MAX}${SYMBOL_CELSIUS}"
  echo "Min: ${WEATHER_MIN}${SYMBOL_CELSIUS}"
  echo "Humidade: ${WEATHER_HUMIDITY}${SYMBOL_PORCENTS}"
  echo "Vento: ${WEATHER_WIND} Km/h"
  echo "${ICON_SNOW} ${WEATHER_TEMP}${SYMBOL_CELSIUS}"
elif [[ "${WEATHER_MAIN}" = *Rain* ]] || [[ "${WEATHER_MAIN}" = *Drizzle* ]]; then
  echo "${WEATHER_CITY}"
  echo "Temp: ${WEATHER_TEMP}${SYMBOL_CELSIUS}"
  echo "Max: ${WEATHER_MAX}${SYMBOL_CELSIUS}"
  echo "Min: ${WEATHER_MIN}${SYMBOL_CELSIUS}"
  echo "Tempo: ${ICON_RAINY}"
  echo "Humidade: ${WEATHER_HUMIDITY}${SYMBOL_PORCENTS}"
  echo "Vento: ${WEATHER_WIND} Km/h"
elif [[ "${WEATHER_MAIN}" = *Cloud* ]]; then
  echo "${WEATHER_CITY}"
  echo "Temp: ${WEATHER_TEMP}${SYMBOL_CELSIUS}"
  echo "Max: ${WEATHER_MAX}${SYMBOL_CELSIUS}"
  echo "Min: ${WEATHER_MIN}${SYMBOL_CELSIUS}"
  echo "Tempo: ${ICON_CLOUDY}"
  echo "Humidade: ${WEATHER_HUMIDITY} %"
  echo "Vento: ${WEATHER_WIND} Km/h"
elif [[ "${WEATHER_MAIN}" = *Clear* ]]; then
  echo "${WEATHER_CITY}"
  echo "Temp: ${WEATHER_TEMP}${SYMBOL_CELSIUS}"
  echo "Max: ${WEATHER_MAX}${SYMBOL_CELSIUS}"
  echo "Min: ${WEATHER_MIN}${SYMBOL_CELSIUS}"
  echo "Tempo: ${ICON_SUNNY}"
  echo "Humidade: ${WEATHER_HUMIDITY}${SYMBOL_PORCENTS}"
  echo "Vento: ${WEATHER_WIND} Km/h"
elif [[ "${WEATHER_MAIN}" = *Fog* ]] || [[ "${WEATHER_MAIN}" = *Mist* ]]; then
  echo "${WEATHER_CITY}"
  echo "Temp: ${WEATHER_TEMP}${SYMBOL_CELSIUS}"
  echo "Max: ${WEATHER_MAX}${SYMBOL_CELSIUS}"
  echo "Min: ${WEATHER_MIN}${SYMBOL_CELSIUS}"
  echo "Tempo: ${ICON_FOG}"
  echo "Humidade: ${WEATHER_HUMIDITY}${SYMBOL_PORCENTS}"
  echo "Vento: ${WEATHER_WIND} Km/h"
else
  echo "${WEATHER_CITY}"
  echo "Temp: ${WEATHER_TEMP}${SYMBOL_CELSIUS}"
  echo "Max: ${WEATHER_MAX}${SYMBOL_CELSIUS}"
  echo "Min: ${WEATHER_MIN}${SYMBOL_CELSIUS}"
  echo "Tempo: ${ICON_MAIN}"
  echo "Humidade: ${WEATHER_HUMIDITY}${SYMBOL_PORCENTS}"
  echo "Vento: ${WEATHER_WIND} Km/h"
fi
 
if [[ "${WEATHER_TEMP}" -lt "${URGENT_LOWER}" ]] || [[ "${WEATHER_TEMP}" -gt "${URGENT_HIGHER}" ]]; then
  exit 0
fi
