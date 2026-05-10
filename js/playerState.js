/**
 * playerState.js — минимальный API для игрового состояния AWARA
 *
 * Ключ хранения: awara_v258_state (новый)
 * Миграция с: awara_v255_state (легаси, index.html / dashboard.html)
 *
 * Экспортируемые функции:
 *   getState()          — прочитать текущее состояние
 *   saveState(state)    — сохранить состояние
 *   migrate(legacy)     — привести легаси-объект к новому формату
 *
 * Никакой игровой логики — только I/O.
 */

(function(root) {
  'use strict';

  var KEY_NEW    = 'awara_v258_state';
  var KEY_LEGACY = 'awara_v255_state';

  var DEFAULTS = {
    totalLight:   0,
    sphereData:   {},
    spirit:       null,
    elements:     {},
    activeSystem: {},
    journey:      []
  };

  function deepCopy(obj) {
    return JSON.parse(JSON.stringify(obj));
  }

  function ensureFields(state) {
    var out = {};
    var keys = Object.keys(DEFAULTS);
    for (var i = 0; i < keys.length; i++) {
      var k = keys[i];
      out[k] = (state && state[k] !== undefined) ? state[k] : deepCopy(DEFAULTS[k]);
    }
    return out;
  }

  /**
   * migrate(legacyState) — приводит легаси-объект (v255) к формату v258
   */
  function migrate(legacy) {
    if (!legacy || typeof legacy !== 'object') {
      return deepCopy(DEFAULTS);
    }
    return ensureFields(legacy);
  }

  /**
   * getState() — прочитать текущее состояние из localStorage
   *
   * Приоритет: awara_v258_state > awara_v255_state > DEFAULTS
   * При миграции с v255 автоматически сохраняет в v258.
   */
  function getState() {
    try {
      var raw = localStorage.getItem(KEY_NEW);
      if (raw) {
        return ensureFields(JSON.parse(raw));
      }

      var legacy = localStorage.getItem(KEY_LEGACY);
      if (legacy) {
        var migrated = migrate(JSON.parse(legacy));
        saveState(migrated);
        return migrated;
      }
    } catch (e) {
      console.warn('playerState.getState:', e);
    }

    return deepCopy(DEFAULTS);
  }

  /**
   * saveState(state) — сохранить состояние в localStorage (awara_v258_state)
   */
  function saveState(state) {
    try {
      var clean = ensureFields(state);
      localStorage.setItem(KEY_NEW, JSON.stringify(clean));
    } catch (e) {
      console.warn('playerState.saveState:', e);
    }
  }

  // Экспорт
  var api = {
    getState:  getState,
    saveState: saveState,
    migrate:   migrate
  };

  if (typeof module !== 'undefined' && module.exports) {
    module.exports = api;
  } else {
    root.PlayerState = api;
  }

})(typeof globalThis !== 'undefined' ? globalThis : this);
