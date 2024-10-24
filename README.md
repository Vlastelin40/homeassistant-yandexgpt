See [description in English](#yandexgpt-integration-for-home-assistant) below 👇
<br>
<br>

# Интеграция YandexGPT для Home Assistant

[![Добавить репозиторий в HACS](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=black-roland&repository=homeassistant-yandexgpt&category=integration) [![Настроить интеграцию с YandexGPT](https://my.home-assistant.io/badges/config_flow_start.svg)](https://my.home-assistant.io/redirect/config_flow_start/?domain=yandexgpt_conversation)

Ассистент на основе YandexGPT для Home Assistant:

- Интеграция позволяет «общаться» с ассистентом из интерфейса Home Assistant.
- У ассистента можно узнавать показания датчиков, состояние света и других устройств. То есть ассистент на базе YandexGPT знает все про умный дом и устройства в нем.
- С помощью приложения Home Assistant, установленного на смартфоне или умных часах, можно общаться с ассистентом голосом.
- Интеграция может служить «мозгом» для создания DIY-умной колонки на базе ESPHome, если помимо YandexGPT добавить в Home Assistant синтез и распознавание речи.
- YandexGPT можно использовать в автоматизациях, например, для создания чат-бота в Telegram.
- Кроме того, интеграция позволяет генерировать изображения с помощью YandexART.

YandexGPT — это облачный сервис, плата за который взимается в соответствии с тарифами Yandex Cloud.

## Установка и настройка

Инструкции по получению ключа API и настройке интеграции можно найти в [wiki](https://github.com/black-roland/homeassistant-yandexgpt/wiki).

TLDR: Добавьте интеграцию, используя голубые кнопки выше, а затем получите [идентификатор каталога](https://yandex.cloud/ru/docs/resource-manager/operations/folder/get-id) и [ключ API](https://yandex.cloud/en/docs/iam/operations/api-key/create).

## Примеры использования

Примеры использования можно найти в [моем блоге](https://mansmarthome.info/tags/yandexgpt/). Кроме того, про первую версию интеграции я рассказывал на [YouTube](https://www.youtube.com/watch?v=C1KcW--vnUo).

<p>
  <img src="https://github.com/user-attachments/assets/c4f2520d-a1e7-433b-99d6-9db29b2c99f1" height="340px" alt="Assist" />
  <img src="https://github.com/user-attachments/assets/3739e48b-97ac-4069-954d-f770c4fad7d3" height="340px" alt="Morning digests" />
</p>

## Спонсорство

Интеграция оказалась полезной? Хотите сказать спасибо? Кофе автору — ваша благодарность. <kbd>[☕ На кофе](https://mansmarthome.info/donate#donationalerts)</kbd>

Укажите в комментарии свой никнейм на GitHub, чтобы я мог упомянуть вас в README 🙂

Также буду рад помощи с документацией и кодом. Спасибо!

---

# YandexGPT integration for Home Assistant

[![Add custom repository to HACS](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=black-roland&repository=homeassistant-yandexgpt&category=integration) [![Set up YandexGPT integration](https://my.home-assistant.io/badges/config_flow_start.svg)](https://my.home-assistant.io/redirect/config_flow_start/?domain=yandexgpt_conversation)

The assistant based on YandexGPT for Home Assistant:

- The integration allows you to chat with the assistant from the Home Assistant UI.
- You can ask the assistant about sensor readings, status of lights and other devices. So the assistant knows everything about your smart home and the devices in it.
- You can chat with the assistant using Home Assistant app on a watch or smartphone.
- Integration can be the «brain» of a DIY smart speaker based on ESPHome if in addition to YandexGPT you would add speech synthesis and recognition to Home Assistant.
- YandexGPT can be used in automations. For example, this way you can create a chatbot for Telegram or any other supported messenger.
- In addition to YandexGPT, the integration provides image generation using YandexART.

YandexGPT is a cloud service. Fees are charged according to Yandex Cloud tariffs.

## Set up

Use My Home Assistant buttons above to install and configure the integration. Please check out the official documentation on how to retrieve [folder ID](https://yandex.cloud/en/docs/resource-manager/operations/folder/get-id) and [API key](https://yandex.cloud/en/docs/iam/operations/api-key/create).
