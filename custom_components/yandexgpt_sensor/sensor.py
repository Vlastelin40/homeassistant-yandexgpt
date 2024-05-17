# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import logging

import voluptuous as vol
from homeassistant.components.sensor import PLATFORM_SCHEMA, SensorEntity
from homeassistant.const import (
    CONF_NAME,
)
from homeassistant.core import HomeAssistant, CoreState
from homeassistant.helpers import config_validation as cv
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType
from yandex_gpt import YandexGPT, YandexGPTConfigManagerForAPIKey

# from sqlalchemy.util import LRUCache
# from functools import lru_cache

_LOGGER = logging.getLogger(__name__)

DEFAULT_NAME = "YandexGpt response"

CONF_CATALOG_ID = "catalog_id"
CONF_API_KEY = "api_key"

CONF_SYSTEM_PROMPT = "system_prompt"
CONF_USER_PROMPT = "user_prompt"

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Optional(CONF_NAME, default=DEFAULT_NAME): cv.string,
        vol.Required(CONF_CATALOG_ID): cv.string,
        vol.Required(CONF_API_KEY): cv.string,
        vol.Required(CONF_SYSTEM_PROMPT): cv.string,
        vol.Required(CONF_USER_PROMPT): cv.template,
    }
)


def setup_platform(
        hass: HomeAssistant,
        config: ConfigType,
        add_entities: AddEntitiesCallback,
        discovery_info: DiscoveryInfoType | None = None,
) -> None:
    name = config.get(CONF_NAME)

    system_prompt = config.get(CONF_SYSTEM_PROMPT)
    user_prompt = config.get(CONF_USER_PROMPT)

    # TODO: Change sensor configuration to make it look like the new template sensor configuration
    #       so this should be initialized only once
    yandexgpt_config = YandexGPTConfigManagerForAPIKey(model_type="yandexgpt-lite",
                                                       catalog_id=config.get(CONF_CATALOG_ID),
                                                       api_key=config.get(CONF_API_KEY))
    yandexgpt = YandexGPT(config_manager=yandexgpt_config)

    device = YandexGptSensor(yandexgpt, name, system_prompt, user_prompt)

    add_entities([device], True)


class YandexGptSensor(SensorEntity):
    _attr_should_poll = False

    def __init__(self, yandexgpt, name, system_prompt, user_prompt):
        self._name = name
        self._state = None
        self._state_attributes = None

        self._yandexgpt = yandexgpt
        self._system_prompt = system_prompt
        self._user_prompt_tpl = user_prompt
        # self._cache = LRUCache(1000)
        self._increment = 0
        self._completion = None

        self._yandexgpt = yandexgpt

    @property
    def name(self):
        return self._name

    @property
    def native_value(self):
        return self._completion

    async def async_update(self) -> None:
        # Ignore update on HASS restart to reduce API requests count
        if self.hass.state == CoreState.not_running:
            return

        # TODO: Render system prompt as template
        user_prompt = self._user_prompt_tpl.async_render()

        completion = await self._yandexgpt.get_async_completion(
            messages=[
                {"role": "system", "text": self._system_prompt},
                {"role": "user", "text": user_prompt},
            ],
            max_tokens=255,
            timeout=30,
        )
        self._completion = completion[:255]
